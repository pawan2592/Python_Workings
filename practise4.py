#For loop

#in For loop we dont mention condition, we mention sequence like list, tuple, set

x= ['pawan',65,2.5]
print(x)

#to print the values individually

for i in x:
    print(i)
#individual character in string
X='Pawan'
for i in X:
    print(i)

for i in [2,6,'pawan']:
    print(i)





#print the number from 11 to 20 by increment of 1
for i in range(11,21,1):
    print(i)
    #print in reverse

for i in range (20,10,-1):
    print(i)

#values not divisble by 5

for i in range(1,21):
    if (i%5!=0):
        print(i)


#perfect square numbers

for i in range(0,500):
    for j in range (0,500):
        if (i==j):
            print(i*j, "is a perfect square number")


for i in range (1,500):
        k= i*i
        if(k/i==i):
            print(k)





