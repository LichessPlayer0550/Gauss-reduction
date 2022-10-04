from random import randint as rd

def randomQuadratic(n):
    q = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            r = rd(-9,9)
            q[i][j] = r
            q[j][i] = r
    return q

def gaussReduction(q, l=[], v=[]):
    n = len(q)
    for p in range(n):
        if q[p][p]!=0:
            a=q[p][p]
            c=[]
            i=j=0
            while i<n+len(v):
                if i in v:
                    c.append(0)
                else:
                    c.append(q[p][j]/a)
                    j+=1
                i+=1
            b=0
            for i in range(n+len(v)):
                if i not in v:
                    if b==p:
                        v.append(i)
                        break
                    else:
                        b+=1
            c=[(a,c)]
            for i in range(n):
                for j in range(n):
                    q[i][j]-=q[p][i]*q[p][j]/a
            return gaussReduction([[q[i][j]for j in range(n)if j!=p]for i in range(n)if i!=p],l+c,v)
    for p in range(n):
        for s in range(p+1,n):
            if q[p][s]!=0:
                a = 2*q[p][s]
                c=[]
                d=[]
                i=j=0
                while i<n+len(v):
                    if i in v:
                        c.append(0)
                    else:
                        c.append((q[p][j]+q[s][j])/a)
                        d.append((q[s][j]-q[p][j])/a)
                        j+=1
                    i+=1
                b=0
                for i in range(n+len(v)):
                    if i not in v:
                        if b==p:
                            v.append(i)
                            break
                        else:
                            b+=1
                b=0
                for i in range(n+len(v)):
                    if i not in v:
                        if b==s:
                            v.append(i)
                            break
                        else:
                            b+=1
                c=[(a/4,c)]
                d=[(-1,d)]
                for i in range(n):
                    for j in range(n):
                        q[i][j]-=(q[p][i]*q[s][j]+q[p][j]*q[s][i])/(a/2)
                return gaussReduction([[q[i][j]for j in range(n)if (j!=p and j!=s)]for i in range(n)if (i!=p and i!=s)],l+c+d,v)
    return l

def renderLatex(q = randomQuadratic(4)):
    a='$'
    for i in range(len(q)):
        a+=str(q[i][i])+'x_'+str(i)+'^2+'
    for i in range(len(q)):
        for j in range(i+1,len(q)):
            a+=str(2*q[i][j])+'x_'+str(i)+'x_'+str(j)+'+'
    a=a[:-1]+'='
    l=gaussReduction(q)
    for k in l:
        a+=str(k[0])+'('
        for i in range(len(k[1])):
            a+=str(k[1][i])+'x_'+str(i)+'+'
        a=a[:-1]+')^2+'
    a=a[:-1]+'$'
    return a
    
    
    
            
            
