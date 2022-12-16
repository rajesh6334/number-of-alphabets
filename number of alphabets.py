#number of alphabets
n=input("enter the string:")
a=len(n)
ch=0
for i in range(a):
    if n[i].isalpha()==1:
        ch=ch+1
print("number of elements in string",ch)        
