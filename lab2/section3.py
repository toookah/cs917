def cal2col(filename,indexOfName,index1,index2):
  col1=[]
  col2=[]
  with open(filename,'r') as file1:
    i=0
    for line in file1:
      if i>0:
          value=line.split(',')
          col1.append(value[indexOfName])
	  col2.append(abs(int(value[index1])-int(value[index2])))
      i+=1
  print(col1[col2.index(min(col2))])
#problem1
cal2col("football.csv",0,5,6)
cal2col("weather.csv",0,1,2)
