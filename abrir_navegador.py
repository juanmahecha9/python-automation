import webbrowser

navegador = 'chrome'
url = 'https://www.facebook.com/'

c = webbrowser.get(navegador)
c.open(url)