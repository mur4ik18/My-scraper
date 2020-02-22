import requests
from bs4 import BeautifulSoup as BS 
import os
import shutil
import read
from read import tx


# var's
folder = 'pepsy'
site_link = 'https://rozetka.com.ua/mobile-phones/c80003/page='
shell = '.goods-tile'
Title = '.goods-tile__heading > .goods-tile__title'
unnecessary_title = "Мобильный телефон "
price = 1
max_page = 1
pages = []

# Folder checker 

if os.path.exists(folder):
    print("I'm find and delate")
#    os.rmdir('pepsy')
    shutil.rmtree(folder)
else:
    print("I'm not find")

os.mkdir('pepsy/')
f = open('pepsy/text.txt', "w")


for x in range(1, max_page +1):
    pages.append( requests.get(site_link +str(x)) ) 



# this function write our date
def writer(a,b,t):
    for el in html.select(a):
        title = el.select(b)
        f.write(title[0].text.replace(t, ''))
        f.write("\n")
        


for r in pages:
    html = BS(r.content, 'html.parser')
    writer(str(shell), str(Title),unnecessary_title)


        

tx('text')




f.close()