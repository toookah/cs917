team=[]
goals=[]
goals_allowed=[]
with open("football.csv",'r') as football:
  i=0
  for line in football:
    if i>0:
      value=line.split(',')
      team.append(value[0])
      goals.append(abs(int(value[5])-int(value[6])))
      #goals_allowed.append(value[6])
    i+=1
#print(team)
#print(goals)
print(team[goals.index(min(goals))])
#print(goals_allowed[1:])
  
    
