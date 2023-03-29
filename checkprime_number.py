import math



def checkprime(x):
    for i in range (2,x):
        if x % i == 0 :
            return False
        return True
for i in range(1,101):
    if checkprime(i):
        print(i)
