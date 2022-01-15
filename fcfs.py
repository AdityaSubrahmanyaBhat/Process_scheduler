def fcfsWT(at, n, bt, wt):
    service_time = [0] * n
    service_time[0] = 0
    wt[0] = 0
 
    for i in range(1, n):
        service_time[i] = (service_time[i - 1] +bt[i - 1])

        wt[i] = service_time[i] - at[i]
        if (wt[i] < 0):
            wt[i] = 0

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

    