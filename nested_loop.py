#creatinfg a square matrix
#for rows in range(1,6):
#    for colums in range(1,6):
#        print("@",end ="")
#        #this end equals to the "" prevents the cursor to go to next line
#    print("\n")

rows  = int(input("Enter the number of the rows : "))
columns = int(input("Enter the number of the columns: "))
symbol = input("Enter the required symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol,end="")#the end here is for not allowing
                            #the cursor to into the new line
    print()#this prints a newline