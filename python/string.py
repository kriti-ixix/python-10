s=str("HELLO")
s1="hello"
print(s)
print(s1)
print(len(s))
print(max(s))
print(min(s))
print(s[-2])
for x in s:
    print(x)
for c in range(0,len(s),4):
    print(s[c])
index=1
while index<3:
    print(s[index])
    index=index+1
str1="i love python"
print(str1[7:13])
print(str1[::-1])
s2="python "
s3="programming"
print(s2+s3)
print(4*s2)
print("u" in str1)
print(len(str1))
a=s1==s
print(a)
b=s1.upper()==s
print(b)
print(str1.split())
print(str1[::-1])
x=str1.split()
print(x)
x[0]="u"
print(x)