
a=2.5
b=5.4
add = a+b
print (add)

# taking input from user
x = input("Enter the value of a:")
y = input("Enter the value of b:")
z = int(x)+int(y)
print("addition of numbers {0} and {1} is {2}".format(x,y,z))

#if else loop and logical operation like and, or
q = 50
w = 100
e = 50
if (q>w):
    print("q is greater than w")
    if(e > q):
        print("e is greater")   
elif(q == w and w == e):
    print("q is equal to w")
else:                
    print("q is smaller that w")

#While loop
i=0
while(i<5):
    print(i)
    i+=1
   

#for loop
print("for loop")    
for i in range(10):
    print(i)
print("for loop with start and end range")
for i in range(10,15):
    print(i)
for i in range(50,40,-2):
    print(i)

#Function
print("Function ")
def addition(l,k):
    j=l+k
    return j
     

l=10
k=50
ans = addition(l,k)
print("Ans is {0}".format(ans))

#FILE HANDLING
print("File handling")
#Create a text file
a = open("AICLASS.txt","r") #"r" for open the file in reading mode
print(a.read())
a.close
    
