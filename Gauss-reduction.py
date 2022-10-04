from random import randint as rd

def randomQuadratic(n):
    q = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            q[i][j]=q[j][i]=rd(1,3)
    return q

def GaussReduction(q, k=set()):
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
                b=0
                c,d=[],[]
                for i in range(n+len(k)):
                    if i not in k:
                        if b==p or b==s: k.add(i)
                        c.append((q[p][b]+q[s][b])/a)
                        d.append((q[s][b]-q[p][b])/a)
                        b+=1
                    else:
                        c.append(0)
                        d.append(0)
                c = [(a/(2*(int(p!=s)+1)),c)]
                d = [None,[(-1,d)]][set(d)!={0}]
                yield c
                if d: yield d
                q = [[q[i][j]-(q[p][i]*q[s][j]+q[p][j]*q[s][i])/a for j in range(n)]for i in range(n)]
                for x in GaussReduction([[q[i][j]for j in range(n)if (j!=p and j!=s)]for i in range(n)if (i!=p and i!=s)],k): yield x
                return
            
def renderLatex(q = randomQuadratic(4)):
    def floater(h):
        if abs(h)==1:
            c=''
        elif int(h)==h:
            c=str(abs(int(h)))
        else:
            x=2
            while True:
                y=x*h
                if abs(int(y)-y)<1e-1:
                    c=r'\frac{'+str(abs(int(y)))+'}{'+str(x)+'}'
                    break
                x+=1
        return c
    a='$'
    d=0
    for i in range(len(q)):
        if q[i][i]!=0:
            d+=1
            c=floater(q[i][i])
            s=['','+','-'][int(q[i][i]//abs(q[i][i]))]
            if d==1 and s=='+':
                s=''
            a+=s+c+'x_'+str(i)+'^2'
    f=0
    for i in range(len(q)):
        for j in range(i+1,len(q)):
            if q[i][j]!=0:
                f+=1
                c = floater(2*q[i][j])
                s=['','+',''][int(2*q[i][j]//abs(2*q[i][j]))]
                if d==0 and s=='+' and f==1:
                    s=''
                a+=s+c+'x_'+str(i)+'x_'+str(j)
    a=a+'='
    d=0
    for k in list(GaussReduction(q,set())):
        if k[0][0]!=0:
            d+=1
            c=floater(k[0][0])
            s=['','+','-'][int(k[0][0]//abs(k[0][0]))]
            if d==1 and s=='+':
                s=''
            a+=s+c
            f=0
            if len([x for x in k[0][1] if x!=0])>1:
                a+=r'\big('
            for i in range(len(k[0][1])):
                if k[0][1][i]!=0:
                    f+=1
                    c=floater(k[0][1][i])
                    s=['','+','-'][int(k[0][1][i]//abs(k[0][1][i]))]
                    if f==1 and s=='+':
                        s=''
                    a+=s+c+'x_'+str(i)
            if len([x for x in k[0][1] if x!=0])>1:
                a+=r'\big)'
            a+='^2'
    a=a+'$'
    return print(a)
