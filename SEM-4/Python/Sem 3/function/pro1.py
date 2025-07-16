# without arg
def pro():
    a=1
    b=2
    c = a+b
    print(c)
pro()
def pro1():
    a=1
    b=2
    c = a-b
    print(c)
pro1()
def pro2():
    a=1
    b=2
    c = a*b
    print(c)
pro2()
def pro3():
    a=1
    b=2
    c = a/b
    print(c)
pro3()
def pro4():
    a=1
    b=2
    c = a**b
    print(c)
pro4()
def pro5():
    a=1
    b=2
    c = a//b
    print(c)
pro5()
def pro6():
    a=1
    b=2
    if (a==b):
        print("Equal")
    else:
        print("Not equal")
pro6()

# with arg
def pro7(a,b):
    print(a+b)
pro7(10,20)

def pro8(a,b):
    print(a-b)
pro8(10,20)

def pro9(a,b):
    print(a*b)
pro9(10,20)

def pro10(a,b):
    print(a/b)
pro10(10,20)

def pro11(a,b):
    print(a**b)
pro11(10,20)

def pro12(a,b):
    print(a//b)
pro12(10,20)

def pro13(a,b):
    if (a==b):
        print("Equal")
    else:
        print("not equal")
pro13(10,20)

#return value 

def pro14():
    a = 10
    b = 20
    return(a+b)
print("Return value :",pro14())

def pro15():
    a = 10
    b = 20
    return(a-b)
print("Return value :",pro15())

def pro16():
    a = 10
    b = 20
    return(a*b)
print("Return value :",pro16())

def pro17():
    a = 10
    b = 20
    return(a/b)
print("Return value :",pro17())

def pro18():
    a = 10
    b = 20
    return(a**b)
print("Return value :",pro18())

def pro19():
    a = 10
    b = 20
    return(a//b)
print("Return value :",pro19())

def pro20():
    a = 10
    b = 20
    if(a<b):
        return("Equal")
print("Return value :",pro20())