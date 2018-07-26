import xml.etree.ElementTree as ET
import urllib.request
import os

urllib.request.urlretrieve('http://nswdb.com/xml.php', 'db.xml')
tree = ET.parse('db.xml')
root = tree.getroot()

count = 0
loop1=True
loop2=True

while loop1 == True:
    filename = input("do you want to set a custom name for the title id list \nor leave it as the default (eNXhop.txt for use with eNXhop) \ncustom or default:")
    if filename == "custom":
        filename = input("please enter a name for the output including a file extension: ")
        loop1=False
    if filename == "default" or not filename:
        filename = "eNXhop.txt"
        loop1=False
    else:
        print("please enter custom or default\n")

while loop2 == True:
    langCode = input("Do you only want to pull titles that have a specific language code? If so, enter that language code (for example, en)?")
    if langCode:
        loop2=False
    if not langCode:
        langCode = ""
        loop2=False

file = open(filename,"w")
file = open(filename,"r+")
for release in root:
  isCorrectLangCode=False
  for child in release:
    if child.tag == "languages":
      if langCode == "" or langCode in child.text:
        isCorrectLangCode=True
        lang= str(child.text)
        print(lang)
      else:
        isCorrectLangCode=False
    if child.tag == "titleid" and isCorrectLangCode:
      tid= str(child.text)
      print(tid)
      file.write(tid)
      file.write("\n")
    
file.close()
os.remove("db.xml")
