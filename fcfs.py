def fcfsWT(at, n, bt, wt):
    cur_time=0
    count=0
    minm=999999
    mini=0
    flag=0
    completed=[0]*n
    while count!=n:
        for i in range(n):
            if at[i]<=cur_time and completed[i]==0 and at[i]<minm:
                minm=at[i]
                mini=i
                flag=1
    
        if flag==0:
            cur_time+=1
            continue
            
        wt[mini]=cur_time-at[mini]
        cur_time+=bt[mini]
        completed[mini]=1
        count+=1
        flag=0
        minm=999999

def fcfsTAT( n,bt, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def fcfsMain(at,bt,n,result,total_wt,total_tat,compl_time):
    wt = [0] * n
    tat = [0] * n

    fcfsWT(at, n, bt, wt)

    fcfsTAT( n,bt, wt, tat)
    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        result.append([at[i],bt[i],compl_time,wt[i],tat[i]])
    return total_wt,total_tat,compl_time

def fcfs(at,bt,n):
    result=[]
    total_wt = 0
    total_tat = 0
    compl_time=0
    total_wt,total_tat,compl_time= fcfsMain(at,bt,n,result,total_wt,total_tat,compl_time)
    return result,total_wt,total_tat,compl_time

    