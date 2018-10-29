import xml.etree.ElementTree as ET
import urllib.request
import os

urllib.request.urlretrieve('http://nswdb.com/xml.php', 'db.xml')
tree = ET.parse('db.xml')
root = tree.getroot()

count = 0
loop=True

while loop == True:
    filename = input("do you want to set a custom name for the title id list \nor leave it as the default (eNXhop.txt for use with eNXhop) \ncustom or default (you can also just leave it empty for default):")
    if filename == "custom":
        filename = input("please enter a name for the output including a file extension: ")
        loop=False
    if filename == "default" or not filename:
        filename = "eNXhop.txt"
        loop=False
    else:
        print("please enter custom or default\n")

file = open(filename,"w")
file = open(filename,"r+")
for titleid in root.iter('titleid'):
    if count >= 1:
        file.write("\n")
    else:
        count+=1
    tid= titleid.text
    print(tid)  
    file.write(tid)
    
file.close()
os.remove("db.xml")
