list=[]

def input_num():
    pass

def x2(x):
    pass

def x3_1():
    pass

def collatz(x):
    while x != 1:
        if x % 2 == 0:
            return x2(x)
        else:
            return x3_1(x)
    print("Список:", list)
input_num()