'''
print("How many rows of stars should I print?")
input1=input()
for i in range(1,int(input1)+1):
    print("*"*i)
'''
def draw_stars(number,order):
  for i in range(1,number+1):
    if order==1:
      print("*"*i)
    else:
      print("*"*(number+1-i))
#Now ask the user for the number of rows
print("How many rows of stars should I print?")
number=int(input())
#Now ask the user if the rows should be increasing
print("Whether the rows should be increasing(in) or decreasing(de)?")
order_str=input()
if order_str=="in":
  order=1
else:
  order=0
draw_stars(number,order)    