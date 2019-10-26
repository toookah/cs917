day=[]
spread=[]
with open("weather.csv",'r') as weather:
  i=0
  for line in weather:
    if i>0:
      value=line.split(',')
      day.append(value[0])
      spread.append(int(value[1])-int(value[2]))
    i+=1

print(day[spread.index(min(spread))])
    