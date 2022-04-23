import re

temp = open('Harry.txt', 'r', encoding="utf8")

res = str(temp.readlines())

finder = re.findall('Harry', res)


print(finder)
print(finder.__len__())

temp.close()
