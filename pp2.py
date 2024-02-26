f = open("game.txt").readlines()
a = list()
d = list()
c = dict()
u = list()

for i in f:
    a.append(i[:-1])

for j in range(1,len(a[1:])):
    b = a[j].split("$")
    
    if b[0] in c:
        c[b[0]] += 1
    else:
        c[b[0]] = 1
    
    a[j] = '$'.join(b)


for j in range(1,len(a[1:])):
    b = a[j].split("$")
    
    if b[0] not in u:
        b.append(str(c[b[0]]))
        d.append('$'.join(b))
        u.append(b[0])

for i in range(len(d)):
    print(d[i])
    
        
