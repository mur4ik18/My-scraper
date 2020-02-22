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
    

print(dd)
folders = dd[0].replace('Folder : ', '')
site_link = dd[1].replace('Site link : ', '')
Shell = dd[2].replace('Shell : ', '')
folders = dd[0].replace('Folder : ', '')
folders = dd[0].replace('Folder : ', '')
folders = dd[0].replace('Folder : ', '')