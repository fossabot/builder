import getpass

class Aws(object):

    __identifier__ = 'aws'

    def get_credentials(self):
        secret_key = getpass.getpass('Please enter your secret key (will be hidden): ')
        access_key = getpass.getpass('Please enter your access key (will be hidden): ')

        credentials = {
                ('%s_secret_key' % self.__identifier__): secret_key,
                ('%s_access_key' % self.__identifier__): access_key
        }

        return credentials
