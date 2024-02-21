import urllib.request

try:
    site = urllib.request.urlopen('http://www.pudim.com')
except:
    print('Deu erro')
else:
    print('Tudo OK')
    print(site.read())
