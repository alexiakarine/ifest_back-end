import requests

url = 'http://127.0.0.1:5000/send'
myobj = {'destinatarios': ['secondizzy@gmail.com', 'bsegundo2001@gmail.com']}

x = requests.post(url, json = myobj)

print(x.text)