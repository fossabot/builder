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
def rpm_build(spec=('s', None, 'spec file for rpm build process')):
    """ Build rpm """
    return True


def cli():
    opster.dispatch()
