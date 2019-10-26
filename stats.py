#!/usr/bin/env python3
print("Enter number. When finished type 'stop' to calculate statistics.")
list1=[]
while True:
    input1=input()
   # print(input1)
    if input1=="stop":
        break
    list1.append(int(input1))
print("=== Result ===")
print("You entered "+str(len(list1))+" numbers.")
print("Minimum number: "+str(min(list1)))
print("Maximum number: "+str(max(list1)))
mean=sum(list1)/len(list1)
print("Mean: "+str(mean))
    

    
