list=[]

def input_num():
    pass #я

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