import random as r
import time

print("Think any number between 0-100 and keep it with you, let me find out!!")
time.sleep(6)

min = 0
max = 100
attempt = 0

while 1:
    comp = r.randint(min,max)
    print ("\nIsn't it %d ?"%comp)
    user = input("Enter the option \n a.high \n b.low \n c.Bingo \n")
    attempt += 1
    if user == "low" or user == "b":
        min = comp + 1
        continue
    elif user == "high" or user == "a":
        max = comp - 1
        continue
    elif user == "bingo" or user == "c":
        print ("\nThe number is in your mind is %d and computer took %d attempts"%(comp,attempt))
        break
    else:
        print ("\nPlease enter the valid option")
