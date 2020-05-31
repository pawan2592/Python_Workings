if True:
    print("Im Right")

if False:
    print("Im Right")
    #if is basically block or suit, "if block of code is written by indentation
    #4 spaces

print("bye")

#evaluating the expression on condition
if 3<8:
    print("3 is less than 8")
else:
    print("3 is greater than 8")

print("bye")

x=8

r =x%2
if r==0:
    print("8 is even ")
    if(x>5):
        print("5 is greater than 2")
else:
    print("8 is odd")

print("bye")

#if elif, else

#if user enters 1, our program should print ONE


x = int(input("enter a number"))

if(x==1):
    print("One")
elif(x==2):
    print("Two")
elif(x==3):
    print("Three")
elif(x==4):
    print("Four")
else:
    print("Enter Number between 1-4")


    #Loops

    #print a statement multiple times
    #while loop, specify the condition (no of times the loop runs)
    #Initialization, condition, increment, decrement
i = 1
x1 = int(input("Enter the loop count"))
while(i<=x1):
    print("I am a python programmer",i,x1)
    i+=1

# print two sentence in same line with give number of iterations
i = 1
x1 = int(input("Enter the loop count"))
j = 1
while(i<=x1):
    print("I am a python programmer",end="")
    while(j<=4):
        print("Python ROCKS!!!",end="")
        j += 1
    i+=1

#correction
    i = 1
    x1 = int(input("Enter the loop count"))

    while (i <= x1):
        print("I am a python programmer", end="")
        j = 1
        while (j <= 4):
            print("Python ROCKS!!!", end="")
            j += 1
        i += 1
        print() # for print in new line



