import getpass


class Aws(object):

    __identifier__ = 'aws'

    __target__ = 'instance'

    __ssh__user__ = 'ec2-user'

    def get_credentials(self):
        """
            Get credentials for AWS

            AWS use a secret and an access key
        """
        secret_key = getpass.getpass(
            'Please enter your secret key (will be hidden): ')
        access_key = getpass.getpass(
            'Please enter your access key (will be hidden): ')

        credentials = {
            ('%s_secret_key' % self.__identifier__): secret_key,
            ('%s_access_key' % self.__identifier__): access_key
        }

        return credentials
