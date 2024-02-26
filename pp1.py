f = open("game.txt").readlines()
a = list()

for i in f:
    a.append(i[:-1])

for j in range(1,len(a[1:])):
    b = a[j].split("$")
    
    if b[2].split(":")[1] == "55":
        print(f"У персонажа\t{b[1]}\tв игре\t{b[0]}\tнашлась ошибка с кодом:\t 55.\tДата фиксации:\t {b[3]}")
        b[2] = "Done"
        b[3] = "0000-00-00"
    a[j] = '$'.join(b)

for i in range(len(a)):
    print(a[i])
    
        
