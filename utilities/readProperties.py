import configparser  # this is a packeg in python

# inside this configpurser, there is a method "Rawconfig..."
# we are creating the object for that
config = configparser.RawConfigParser()

config.read("C:\\Users\\DIPANKAR\\PycharmProjects\\OrangeHRM\\Configurations\\config.ini")


class ReadConfig():
    @staticmethod
    def get_application_url():
        url = config.get('common info', 'baseURL')
        return url

    @staticmethod
    def get_username():
        username = config.get('common info', 'user_email')
        return username

    @staticmethod
    def get_password():
        password = config.get('common info', 'user_password')
        return password
