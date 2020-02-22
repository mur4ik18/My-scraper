import requests
from bs4 import BeautifulSoup as BS 
import os
import shutil
import read



# var's
folder = read.folders
site_link = read.site_link
shell = read.Shell
Title = read.Title
unnecessary_title = read.unnecessary_title
price = read.Price
max_page = read.MaxPages
pages = []

# Folder checker 

if os.path.exists(read.folders):
    print("I'm find and delate")
#    os.rmdir('pepsy')
    shutil.rmtree(read.folders)
else:
    print("I'm not find")

os.mkdir(read.folders + '/')
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



print()

f.close()