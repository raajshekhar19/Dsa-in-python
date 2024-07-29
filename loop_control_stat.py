#these are used to control/change the loop execution from its normal sequence

#break : instantly terminateds the loop
#continue skip that particualr iteration
#pass does nothing acts as a place ]holder 

#while True:
#    name = input("enter your name: ")
#    if name != "":
#        break
    
    
#phone_number = "123-456-7890"
##remove the dashesin the phone number
#for number in phone_number:
#    if number=="-":
#        continue
#    else:
#        print(number,end="")


for i in range(1,21):
    if i == 13 :
        pass
    else:
        print(i)