n=int(input())
problem=[]
solution=[]
cnt=0
for i in range(0,n) :
    problem.append(input())
    solution.append(1)

for i in range(0,len(problem)-1) :
    for j in range (i+1,len(problem)):
        if problem[i]==problem[j] and solution[j]!=0:
            solution[i]+=1
            solution[j]=0
    
for i in range(0,n) :
    if solution[i]!=0 :
        cnt+=1
print(cnt)
for i in range(0,n) :
     if solution[i]!=0 :
            print(solution[i],end=' ')
        