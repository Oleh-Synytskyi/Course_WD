from datetime import datetime
import time
import sys


open_file = sys.argv[1]

f = open(open_file, 'r')
Sequential_search = f.read()
f.close()
print("INFO", Sequential_search)
Sequential_search = Sequential_search.split(' ')
print(Sequential_search)
for i in range(0, len(Sequential_search)):
    Sequential_search[i] = int(Sequential_search[i])
print(type(Sequential_search))
print(Sequential_search)
print("Before: ", Sequential_search)




def search(a,x): # a - что ищем, x - где ищем
    res=[]
    for i in range(len(x)):
        if x[i]==a:
            res+=[i]
    if len(res)>0:
        print("Результат пошуку:"+str(res))
    else:
        print("Не знайдено")

Sequential_search =[1,2,3,1,2,3,1,2,3]
search(2, Sequential_search)

for i in range(0, len(Sequential_search)):
    Sequential_search[i] = str(Sequential_search[i])
result =  ' '.join(Sequential_search)
f = open("result.txt", "w")
f.write(result)
f.close()
input("press enter>>>>>>")