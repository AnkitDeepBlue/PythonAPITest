import configparser


config = configparser.ConfigParser()
config.read('utilities/properties.ini')
url = config['API']['endpoint']
ang=config['API']['newone']
print(ang)

config.read('porp/prop.ini')

url_a=config['AP']['point']
print(url_a)

#print(url)