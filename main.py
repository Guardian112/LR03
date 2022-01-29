list=[]

def input_num():
    x = float(input())
    if x % 1 == 0:
        if x > 1:
            collatz(x)
        else:
            input_num()
    else:
        input_num()


def x2(x):
    x = x / 2
    list.append(int(x))
    return collatz(x)

def x3_1(x):
    x = x*3+1
    list.append(int(x))
    return collatz(x)
  
def collatz(x):
    while x != 1:
        if x % 2 == 0:
            return x2(x)
        else:
            return x3_1(x)
    print("Список:", list)
    
input_num()