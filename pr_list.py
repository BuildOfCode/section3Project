f = open('./gameslist.txt','r')
li = f.readlines()
f.close()

left_li = []
right_li = []

for i in li:
    i = i.replace('https://store.steampowered.com/app/', '')
    left_li.append(i)

for i in left_li:
    r = i.split('/')
    right_li.append(r[0])

with open('After_gameslist.txt','w',encoding='UTF-8') as f:
    for name in right_li:
        f.write(name+'\n')

