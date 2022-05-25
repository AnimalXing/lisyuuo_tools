"""display the most frequent characters from a file"""
import collections
import matplotlib.pyplot as plt


plt.rcParams['font.family'] = ['Heiti TC']#to have the cjk characters shown correctly, we have to change the font
f = open("trad_v1.txt", "r")
string = ''
for name in f:
    string+=name[0:len(name)-1]
c = collections.Counter(string)
d = dict(c)
l1 = []
l2 = []
for i in d:
    if d[i]> 15:
        l1.append(i)
        l2.append(d[i])

plt.bar(l1,l2)
plt.show()

