import pdfkit
import requests

''' Note ID is taken from inkdrop.app '''
res = requests.get('https://couchdb.myvnc.com/db-inkdrop/' + 'note:XFhz43AsJ')
if not res:
  print('Response Failed')  
  pdfkit.from_url('https://www.digitalocean.com/asdasd/', '404.pdf')

json = res.json()
strPrefix = "/app/download/" + json["title"]
strLines = json["body"].splitlines()
for url in strLines:
  print(url)
  if url[-1] == "/":
    url = url[:-1]
  strName = strPrefix + "-" + url.split("/")[-1] + ".pdf"
  print(strName)
  pdfkit.from_url(url, strName)
