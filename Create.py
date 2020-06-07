import random
value = 300
name_file = "random.txt"


Num = [random.randint(0, value) for i in range(value)]
for i in range(0, len(Num)):
    Num[i] = str(Num[i])
numbers =  ' '.join(Num)
handle = open(name_file, "w")
handle.write(numbers)
handle.close()
print("Done")
input("press enter>>>>>>>>")