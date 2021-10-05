# Python program to make a GUI Marksheet using Tkinter

NumList=[]
evenSum=0

Number=int(input("Please enter the total number of list elements: "))
for i in range(1, Number+1):
    value=int(input("Please enter the value of %d Elements: " %i))
    
Sum of even numbers from a list


NumList.append(value)
for j in range(Number):
    if(NumList[j]%2==0):
        evenSum=evenSum+NumList[j]
print("\n The sum of even numbers in the list= ",evenSum)
