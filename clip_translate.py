import pyperclip
from googletrans import Translator

src = 'en'
dest = 'ja'
trans = Translator(['translate.google.co.jp' ,'translate.google.com'])

old = ''
pyperclip.copy('')

while True:
    try:
        query = pyperclip.paste().replace('\n', '')    
        if old != query:        
            print(trans.translate(query, src=src, dest=dest).text)
            print()
    except:
        print('error')
    old = query
