import requests
from bs4 import BeautifulSoup as BS 
import os
import shutil
import read

from openpyxl import Workbook


workbook = Workbook()
sheet = workbook.active
# тут мы передаем из файл read.py все переменные которые мы взяли из документа
folder = read.folders
site_link = read.site_link
shell = read.Shell
Title = read.Title
price = read.Price
max_page = read.MaxPages
pages = []
stars = read.Stars

# Проверяем наличие папки
if os.path.exists(read.folders):
    # Если нашли папку то выводим текст об этом в консоль
    print("I'm find and delate")
    # Удалаяем папку и все что в ней есть
    shutil.rmtree(read.folders)
else:
    # Если не нашли папку то пишем что ее нет...
    print("I'm not find")
# создаем папку и файл в этой папке
os.mkdir(folder + '/')
# Создаем и открываем файл в который мы записываем
f = open(folder+'/text.txt', "w")

# цикл для проверки количества
for x in range(1, max_page +1):
    # каждую страницу которую мы получили записываем в pages лист
    pages.append( requests.get(site_link +str(x)) )
    


# this function write our date
def writer(a,b,c):
    # цикл который переберает каждый элемент
    
    for el in html.select(a):
        x +=1
        # вытаскываем Название
        title = el.select(b)
        # Записываем в файл
        price = el.select(c)
        f.write(title[0].text)
        f.write("           ")
        f.write(price[0].text)
        f.write("\n")
        # записываем в Excel
        sheet['A'+str(x)] = x
        sheet['B'+str(x)] = title[0].text
        sheet['C'+str(x)] = price[0].text
        #

for r in pages:
    x = 0
    # получем весь контент
    html = BS(r.content, 'html.parser')
    # запускаем нашу функцию записи
    writer(str(shell), str(Title), price)

workbook.save(filename= folder+"/input.xlsx")
f.close()