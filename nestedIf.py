a=eval(input("enter the value of a : "))
b=eval(input("enter the value of b : "))
c=eval(input("enter the value of c : "))
if (a>b): 
    if(b>c):  
        print(a,"is greater than ", b, " and ", c)
    else:
        print(c,"is greater than ", b, " and ", a)
else:
     print(b,"is greatoe than ", a, " and ", c)
