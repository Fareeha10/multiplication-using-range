print("++++++++++++++MULTIPLICATION TABLE+++++++++++++")
a=int(input("Enter value:"))  # value on which you want to do multiplication
b=int(input("Enter range begin:")) # starting number of the range 
c=int(input("Enter range end:")) # value after the last number of the range
for i in range(b,c): # loop for multiplication
    res=a*i
    print(a,"*",i,"=",res)