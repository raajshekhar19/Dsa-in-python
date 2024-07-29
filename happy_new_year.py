#import the time librARY
import time
#creating the count down fir in loop
print("And here it goes..")
for seconds in range(10,0,-1):
    print(seconds)
    time.sleep(1)#this freezes the program for a second
                 #and ten let it continue
print("Wish you a happy new year")