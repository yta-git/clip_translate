import pyperclip
from googletrans import Translator
from sys import argv, exit

src = 'en'
dest = 'ja'
trans = Translator(['translate.google.co.jp' ,'translate.google.com'])

old = ''
while True:
    query = pyperclip.paste().replace('\n', '')
    if old != query:        
        try:
            print(trans.translate(query, src=src, dest=dest).text)
        except:
            print('error')
    old = query