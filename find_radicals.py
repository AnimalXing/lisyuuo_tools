
import collections
import matplotlib.pyplot as plt
import operator
from hanzi_chaizi import HanziChaizi


hc = HanziChaizi()




plt.rcParams['font.family'] = ['Heiti TC']
f = open("trad_v1.txt", "r")
string = ''
for name in f:
    string+=name[0:len(name)-1]
c = collections.Counter(string)
d = dict(c)
sorted_d = sorted(d.items(), key=operator.itemgetter(1))
sorted_d.reverse()#get the dict, ordered by the value descendingly
l1 = []
l2 = []
for i in sorted_d:
    print(i)
    try:
        radicals = hc.query(i[0])
    except TypeError:
        print("can't find the radical for " + i[0])
        continue
    if (("宀" in radicals) and  i[1]> 0):
        l1.append(i[0])
        l2.append(i[1])
plt.bar(l1,l2)
plt.show()
