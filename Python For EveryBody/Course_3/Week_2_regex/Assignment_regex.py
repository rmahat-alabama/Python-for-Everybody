import re

name = input("Enter filename: ")
handle = open(name)
lst = list()
for line in handle:
     values = re.findall('[0-9]+', line)
     lst = lst+values

sum=0
for item in lst:
    sum = sum + int(item)

print(sum)
