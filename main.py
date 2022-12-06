import os
import xml.etree.ElementTree as ET
import sys

if len(sys.argv)>4:
    filepath = r"C:\Users\User\Downloads\xml_test"
    new_file = 'test_new.xml'
    old_file = 'test_old.xml'
else:
    filepath = sys.argv[1]
    new_file = sys.argv[2]
    old_file = sys.argv[3]


os.chdir(filepath)

tree = ET.parse(new_file)
root = tree.getroot()

dict_new = {}

for i in range(0, 2691):
    try:
        dict_new[root[0][64][0][i][2].attrib["value"]]=root[0][64][0][i][49].attrib["value"]
    except IndexError:
        print(i)
        break
print(dict_new)
for i in dict_new.items():
    print(i)


tree = ET.parse(old_file)
root = tree.getroot()

dict_old = {}

for i in range(0, 2691):
    try:
        dict_old[root[0][64][0][i][2].attrib["value"]]=root[0][64][0][i][49].attrib["value"]
    except IndexError:
        print(i)
        break
print(dict_old)
values_were_unchanged = []
values_were_changed = {}
systems_did_not_exist_in_the_old_file = []

for k, v in dict_new.items():
    try:
        if dict_old[k] == v:
            values_were_unchanged.append({k: v})
        elif dict_old[k] != v:
            values_were_changed[k] = "Value now is {0}, and was {1} in the old file".format(v, dict_old[k])
    except KeyError:
        systems_did_not_exist_in_the_old_file.append({k: v})


with open("values_were_unchanged.csv", "w")  as file:
    for i in range(len(values_were_unchanged)):
        for k,v in values_were_unchanged[i].items():
            file.write('"{}",  {}'.format(k,v) + '\n')

with open("values_were_changed.csv", "w")  as file:
    for k,v in values_were_changed.items():
        file.write('"{}",  {}'.format(k,v) + '\n')

with open("systems_did_not_exist_in_the_old_file.csv", "w")  as file:
    for i in range(len(systems_did_not_exist_in_the_old_file)):
        for k,v in systems_did_not_exist_in_the_old_file[i].items():
            file.write('"{}",  {}'.format(k,v) + '\n')

# print(values_were_unchanged)
# print('\n'*3)
# print(values_were_changed)
# print('\n'*3)
# print(systems_did_not_exist_in_the_old_file)
