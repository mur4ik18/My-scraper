fil = open('input.txt')

# necessary text
#foldn 
#linkn 
#shelln 
#Titlen 
#unnen 
#max_page 
x = 0
dd = []
for line in fil:
    x+=1
    dd.append(line.replace('\n', ''))
dd[4].replace('Price : ', '')
def price():
    if dd[4] == '':
        return ''
    else:
        return dd[4].replace('Price : ', '')

print(dd)
folders = dd[0].replace('Folder : ', '')
site_link = dd[1].replace('Site link : ', '')
Shell = dd[2].replace('Shell : ', '')
Title = dd[3].replace('Title : ', '')
Price = price()
unnecessary_title = dd[5].replace('Unnecessare title : ', '')
MaxPages = dd[6].replace('Max pages : ', '')
print(Price)