#code to print all the values from 1 to 100 skip the numbers which are divisble by 3 or 5


        loopcount = 1
        while(loopcount<=100):
            if(loopcount%3==0):
                loopcount=loopcount+1
            elif(loopcount%5==0):
                loopcount=loopcount+1
            else:
                print(loopcount)
            loopcount=loopcount+1
            print()


# Code to pint # pattern


        x2 = 1
        while (x2 <= 5):
            print("#", end="")
            x3 = 1
            while (x3 <= 4):
                print("#", end="")
                x3 += 1
            x2 += 1
            print()



