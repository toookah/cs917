import csv
def cal2col(filename,indexOfName,index1,index2):
  col1=[]
  col2=[]
  with open(filename,'r') as file1:
    i=0
    reader=csv.reader(file1)
    for line in reader:
      if i>0:
        col1.append(line[indexOfName])
        col2.append(abs(int(line[index1])-int(line[index2])))
      i+=1
  print(col1[col2.index(min(col2))])
#problem1
cal2col("football.csv",0,5,6)
cal2col("weather.csv",0,1,2)

