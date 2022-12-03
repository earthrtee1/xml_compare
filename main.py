import os
import xml.etree.ElementTree as ET

os.chdir(r"C:\Users\User\Downloads")

tree = ET.parse('test_new.xml')
x = ET.Element("Items").findall("./TDM_Item_AbutmentKit/M-BASE direct")
print(x)
