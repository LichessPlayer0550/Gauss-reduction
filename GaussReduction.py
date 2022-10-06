def GaussReduction(q, k=set()):
    ##
    ## q is a symmetrical matrix ##
    ## computes a decomposition of the quadratic form associated to the matrix q in a sum of independant linear forms ##
    ## example of usage : let q(x,y) = x^2 + 2y^2 - 6xy in dimension 2, here the matrix of q is (1 -3)
    ##                                                                                          (-3 2)
    ## hence we call GaussReduction([[1,-3],[-3,2]]), giving [(1.0, [1.0, -3.0]), (-7.0, [0, 1.0])]
    ## this means that q(x,y) = x^2 + 2y^2 - 6xy = (x-3y)^2 - 7y^2
    ##
    n = len(q)
    for p in range(n):
        for s in range(p,n):
            if q[p][s]!=0:
                a = 2*q[p][s]
                b=0
                c,d=[],[]
                for i in range(n+len(k)):
                    if i not in k:
                        if b==p or b==s: k.add(i)
                        c.append((q[p][b]+q[b][s])/a)
                        d.append((q[s][b]-q[b][p])/a)
                        b+=1
                    else:
                        c.append(0)
                        d.append(0)
                c = [(a/(2*(int(p!=s)+1)),c)]
                d = [None,[(-a/(2*(int(p!=s)+1)),d)]][set(d)!={0}]
                yield c
                if d: yield d
                q = [[q[i][j]-(q[p][i]*q[s][j]+q[p][j]*q[s][i])/a for j in range(n)]for i in range(n)]
                for x in GaussReduction([[q[i][j]for j in range(n)if (j!=p and j!=s)]for i in range(n)if (i!=p and i!=s)],k): yield x
                return
