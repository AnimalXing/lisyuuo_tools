import pandas
df = pandas.read_excel('words1.xltx')
pinyin = df[["pinyin"]]
trad = df[["trad"]]
detail = df[["detail"]]
length = len(df)
for i in range(length):
    pinyin['pinyin'].values[i] = pinyin['pinyin'].values[i][:-1]#remove the last character of the the string (the tone)
word = []
f = open("raw.txt", "w")
for j in range(length):
    print(j)
    word.append(str(trad['trad'].values[j])+"\t"+str(pinyin['pinyin'].values[j])+"\n")
    f.write(word[j])
f.close()
