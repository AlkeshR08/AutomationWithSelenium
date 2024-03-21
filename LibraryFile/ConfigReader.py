import configparser

def readConfigData(section, key):
    config = configparser.ConfigParser()
    config.read("./Configurationfile/Config.cfg")
    return config.get(section, key)


def fetchElementLocators(section, key):
    config = configparser.ConfigParser()
    config.read("./Configurationfile/Element.cfg")
    return config.get(section, key)

#print(readConfigData('Details','Application_URL'))