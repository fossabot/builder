import opster


@opster.command()
def register(provider=('p', 'aws', 'provider to register')):
    """ Register provider credentials """

    # Import provider method

    import importlib

    try:
        module = importlib.import_module('providers.%s' % provider)
    except ModuleNotFoundError:
        raise RuntimeError('No such provider')
        import sys
        sys.exit(1)

    class_name = provider.capitalize()
    cls = getattr(module, class_name)
    instance = cls()
    credentials = instance.get_credentials()

    # Write configuration file

    import configparser
    import os

    config = configparser.ConfigParser()
    config[provider] = credentials

    with open(os.path.expanduser('~/.config/builder.cfg'), 'w') as configfile:
        config.write(configfile)

    return True


@opster.command()
def rpm_build(spec=('s', 'spec-file', 'spec file for rpm build process'), identifier=('i', 'os-identifier', 'Target identifier (will help choose the cloud provider)')):
    """ Build rpm """
    if identifier.startswith('ami'):
        provider = 'aws'
    else:
        raise RuntimeError('Unsupported provider')
        import sys
        sys.exit(1)

    import configparser
    import os
    import pystache

    config = configparser.ConfigParser()
    config.read(os.path.expanduser('~/.config/builder.cfg'))
    try:
        credentials = config.items(provider)
    except KeyError:
        raise RuntimeError('Unregistered provider')
        import sys
        sys.exit(1)

    current_directory = os.path.dirname(os.path.realpath(__file__))
    template = os.path.join(current_directory, '..',
                            'templates', ('%s.tf' % provider))
    tf_config = pystache.render(open(template).read(), {
        'credentials': dict(credentials), 'command': {'identifier': identifier}})

    import tempfile
    d = tempfile.mkdtemp()
    with open(os.path.join(d, 'main.tf'), 'w') as tf_file:
        tf_file.write(tf_config)

    import python_terraform as tf
    tf = tf.Terraform(working_dir=d)

    try:
        return_code, stdout, stderr = tf.init()
    except FileNotFoundError:
        raise RuntimeError('Terraform not found')
        import sys
        sys.exit(1)

    try:
        return_code, stdout, stderr = tf.plan(d)
    except FileNotFoundError:
        raise RuntimeError('Terraform not found')
        import sys
        sys.exit(1)

    try:
        return_code, stdout, stderr = tf.apply(d)
    except FileNotFoundError:
        raise RuntimeError('Terraform not found')
        import sys
        sys.exit(1)

    return True


def cli():
    opster.dispatch()
