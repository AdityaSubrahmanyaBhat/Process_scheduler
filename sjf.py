def findWaitingTime(at, bt,n, wt):
    completed = [0] * n
    time=0
    count=0
    
    while count!=n:
        flag=0
        mini=9999999999
        for i in range(n):
            if at[i]<=time and completed[i]==0 and bt[i]<mini:
                mini=i
                flag=1
        if flag:
            wt[mini]=time-at[i]
            if wt[mini]<0:
                wt[mini]=0
            time+=bt[mini]
            completed[mini]=1
            count+=1

        else:
            time+=1
 
def findTurnAroundTime(at,bt, n, wt, tat):
    for i in range(n):
        tat[i] = bt[i] + wt[i]

def findavgTime(at,bt, n,result,compl_time,total_wt,total_tat):
    wt = [0] * n
    tat = [0] * n

    findWaitingTime(at, bt,n, wt)

    findTurnAroundTime(at,bt, n, wt, tat)

    
    for i in range(n):
        total_wt = total_wt + wt[i]
        total_tat = total_tat + tat[i]
        compl_time = tat[i] + at[i]
        result.append([at[i],bt[i],compl_time,wt[i],tat[i]])
    return total_wt,total_tat,compl_time

def sjf(at,bt,n):
    result=[]
    compl_time=0
    total_wt = 0
    total_tat = 0
    total_wt,total_tat,compl_time=findavgTime(at,bt,n,result,compl_time,total_wt,total_tat)
    return result,total_wt,total_tat,compl_time


