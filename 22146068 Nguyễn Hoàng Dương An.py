'''
Nhập dữ liệu đưa vào
xoá các khoảng trắng vô nghĩa
viết hoá chữ cái đầu tiên và không thay đổi các dữ liệu khác
'''
from math import*
# this code help input
a=input('Full name: ')
#this code help del space
b=len(a)
for i in range(0,b):
    a=a.replace("  ", " ")
a=a.strip(' ')
# this code help Upper case the first letter
akt=a.find(' ')
a1=a[0:akt+1].capitalize()
a2=a[akt+1:]
c=a1+a2
# ouput
print(a)
print(c)
