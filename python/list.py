#empty list
l=list()
print(l)
#int elements
l1=list([12,45,77,21])
print(l1)
l2=["hello", "hi"] #strings 
print(l2)
l3=["hello", 'h', 56,76.9]
print(l3)
l4=[1,2,3,4,5]
print(l4)
l5=list(range(1,100)) #range function
print(l5)
print(l5[67])
print(l5[-4]) #accessing index
print(l5[50:70]) #slicing
l6=l2+l3  #join two list using +
print(l6)
l7=l4*3  #repeating elements using *
print(l7)
ll=[1,2,3]
ll1=[1,2,3]
print(ll is ll1)  #is operator
ll2=[10,20,30,40,50]   #list comprehension
ll2=[x+22 for x in ll2]
print(ll2)
a=[23,45,11,22,44,66]
a=[x for x in a if x%2==1]
print(a)
ss="welcome to python class"
b=ss.split()
b[0]="hello"
print(b)
def listfn(l):   #list function
    for x in l:
        print(x, end=" ")
l9=[3,12,55,88,99]
listfn(l9)