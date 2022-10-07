import configparser

config=configparser.RawConfigParser()
config.read("../Configurations/config.ini")
"""
print(config.sections())
print(config.get('common info','baseURL'))
print(config.get('common info','username'))
print(config.get('common info','password'))
"""
class ReadConfig():
    @staticmethod
    def getAppicationURL():
        url=config.get('common info', 'baseURL')
        return url
    @staticmethod
    def getUsername():
        username=config.get('common info','username')
        return username
    @staticmethod
    def getPassword():
        password=config.get('common info','password')
        return password
