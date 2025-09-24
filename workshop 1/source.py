
def performSub(x, y):
    return x - y 

def performAdd(x, y): 
    return x + y 

def performMult(x, y):
    return x * y

def performDiv(x, y):
    if y <= 0:
        print("Cannot divide by 0.")
    else:
        x / y    