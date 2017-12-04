import getpass


class DigitalOcean(object):

    __identifier__ = 'do'

    """
        The name of cloud instance for the provider
    """

    __target__ = 'droplet'

    def get_credentials(self):
        """
            Get credentials for Digital Ocean

            Credentials is only a token
        """
        token = getpass.getpass(
            'Please enter your token (will be hidden): ')

        credentials = {
            ('%s_token' % self.__identifier__): token
        }

        return credentials
