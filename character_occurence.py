"""display the most frequent characters from a file"""
import collections
import matplotlib.pyplot as plt
import operator


plt.rcParams['font.family'] = ['Heiti TC']#to have the cjk characters shown correctly, we have to change the font
f = open("trad_v1.txt", "r")
string = ''
for name in f:
    string+=name[0:len(name)-1]
c = collections.Counter(string)
d = dict(c)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
sorted_d.reverse()#egt the dict, ordered by the value descendingly
l1 = []
l2 = []
for i in sorted_d:
    if i[1]> 15:
        l1.append(i[0])
        l2.append(i[1])
plt.bar(l1,l2)
plt.show()
