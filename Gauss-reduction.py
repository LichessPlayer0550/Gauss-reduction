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
