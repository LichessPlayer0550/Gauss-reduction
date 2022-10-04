from random import randint as rd

def randomQuadratic(n):
    q = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            q[i][j]=q[j][i]=rd(-9,9)
    return q

def GaussReduction(q, l=[], v=[]):
    ##
    ## q is a symmetrical matrix ##
    ## computes a decomposition of the quadratic form associated to the matrix q in a sum of independant linear forms ##
    ## example of usage : let q(x,y) = x^2 + 2y^2 - 6xy in dimension 2, here the matrix of Q is (1 -3)
    ##                                                                                          (-3 2)
    ## hence we call GaussReduction([[1,-3],[-3,2]]), giving [(1.0, [1.0, -3.0]), (-7.0, [0, 1.0])]
    ## this means that q(x,y) = x^2 + 2y^2 - 6xy = (x-3y)^2 - 7y^2
    ##
    n = len(q)
    for p in range(n):
        for s in range(p,n):
            if q[p][s]!=0:
                a = 2*q[p][s]
                c,d=[],[]
                b=0
                j=[]
                for i in range(n+len(v)):
                    if i not in v:
                        if b==p or b==s:
                            j.append(i)
                        c.append((q[p][b]+q[s][b])/a)
                        d.append((q[s][b]-q[p][b])/a)
                        b+=1
                    else:
                        c.append(0)
                        d.append(0)
                v+=list(set(j))
                c=[(a/(2*(int(p!=s)+1)),c)]
                if set(d)!={0}:
                    d=[(-1,d)]
                else:
                    d=[]
                for i in range(n):
                    for j in range(n):
                        q[i][j]-=(q[p][i]*q[s][j]+q[p][j]*q[s][i])/a
                return GaussReduction([[q[i][j]for j in range(n)if (j!=p and j!=s)]for i in range(n)if (i!=p and i!=s)],l+c+d,v)
    return l

def renderLatex(q = randomQuadratic(4)):
    #this does'nt work
    def floater(h):
        if h==1:
            c=''
        elif int(h)==h:
            c=str(abs(h))
        else:
            x=2
            while True:
                y=x*h
                if abs(int(y)-y)<1e-1:
                    c=r'\frac{'+str(int(y))+'}{'+str(x)+'}'
                    break
                x+=1
        return c
    a='$'
    for i in range(len(q)):
        if q[i][i]!=0:
            c=floater(q[i][i])
            s=['','+','-'][int(q[i][i]//abs(q[i][i]))]
            a+=s+c+'x_'+str(i)+'^2'
    for i in range(len(q)):
        for j in range(i+1,len(q)):
            if q[i][j]!=0:
                c = floater(2*q[i][j])
                s=['','+',''][int(2*q[i][j]//abs(2*q[i][j]))]
                a+=s+c+'x_'+str(i)+'x_'+str(j)+'+'
    a=a[:-1]+'='
    l=GaussReduction(q)
    for k in l:
        if k[0]!=0:
            c=floater(k[0])
            s=['','+','-'][int(k[0]//abs(k[0]))]
            a+=s+c+'('
            for i in range(len(k[1])):
                if k[1][i]!=0:
                    c=floater(k[1][i])
                    s=['','+','-'][int(k[1][i]//abs(k[1][i]))]
                    a+=s+c+'x_'+str(i)+'+'
            a=a[:-1]+')^2+'
    a=a[:-1]+'$'
    return a
