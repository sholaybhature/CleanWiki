from kivy.app import App
from kivy.uix.rst import RstDocument
import re
from bs4 import BeautifulSoup
import requests
import os
import shutil

link = str(input("Enter the Wikipedia link to clean: "))
url = requests.get(link)
soup = BeautifulSoup(url.content, 'html.parser')
match = soup.findAll('p')
match = str(match)
tags = re.compile(r'<[^>]+>')
match = tags.sub('', match)
pattern = re.compile(r'\[\d+]+')
match = pattern.sub('', match)
match = match.replace('\n,', '\n')
match = match.replace('[', '')
match = match.replace(']', '')
file = open("result.txt", "w", encoding="utf-8")
path = os.path.realpath(file.name)
file.write(match)
file.close()
location = str(input('Do you want to change the default location of the saved file? Type YES or NO.'))
if location == 'YES':
    path_loc = str(input('Enter the path of desired location: '))
    shutil.move(path, path_loc)
else:
    print(f'File saved at {path}.')

class WikiApp(App):

    def build(self):
        text = 'Hello ThIS IS ME'
        document = RstDocument(text=match)
        return document

if __name__ == "__main__":
    WikiApp().run()