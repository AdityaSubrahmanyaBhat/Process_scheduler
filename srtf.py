def srtf(at,bt,n):
    total_wt=total_tat=0
    wt=[0]*n
    tat=[0]*n
    compl_time=[]
    result=[]
    total_wt,total_tat,compl_time=calcAvgTime(at,bt,n,wt,tat,total_wt,total_tat,compl_time,result)
    return result,total_wt,total_tat,compl_time


def calcAvgTime(at,bt,n,wt,tat,total_wt,total_tat,compl_time,result):
    findWt(at,bt,n,wt)
    findTat(at,bt,n,wt,tat)
    for i in range(n):
        total_wt+=wt[i]
        total_tat+=tat[i]
        compl_time = tat[i] + at[i]
        result.append([at[i],bt[i],compl_time,wt[i],tat[i]])
    return total_wt,total_tat,compl_time

def findWt(at,bt,n,wt):
    cur_time=0
    completed=[0]*n
    count=0
    minm=999999
    flag=0
    mini=0
    temp=bt[:]
    while count!=n:
        for i in range(n):
            if temp[i]<minm and temp[i]>0 and at[i]<=cur_time:
                mini=i
                minm=temp[i]
                flag=1
        
        if flag==0:
            cur_time+=1
            continue

        temp[mini]-=1
        minm=temp[mini]
        if minm==0:
            minm=999999
        
        if temp[mini]==0:
            count+=1
            flag=0
            wt[mini]=cur_time+1-bt[mini]-at[mini]
            if wt[mini]<0:
                wt[mini]=0
        
        cur_time+=1

def findTat(at,bt,n,wt,tat):
    for i in range(n):
        tat[i]=bt[i]+wt[i]


