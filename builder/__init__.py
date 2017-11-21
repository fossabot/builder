import opster


@opster.command()
def rpm_build(spec=('s', 'spec-file', 'spec file for rpm build process')):
    """ Build rpm """
    return True


def cli():
    opster.dispatch()
