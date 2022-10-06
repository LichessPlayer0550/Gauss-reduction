from GaussReduction import *
from random import randint as rd

def randomQuadratic(n):
    q = [[0 for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            q[i][j]=q[j][i]=rd(-9,9)
    return q
            
def renderLatex(q = randomQuadratic(4)):
    ##
    ## produce a LaTeX snippet showing the Gauss reduction of a matrix q
    ##
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
                s=['','+','-'][int(2*q[i][j]//abs(2*q[i][j]))]
                if d==0 and s=='+' and f==1:
                    s=''
                a+=s+c+'x_'+str(i)+'x_'+str(j)
    a=a+'='
    d=0
    for k in GaussReduction(q,set()):
        if k[0][0]!=0:
            d+=1
            c=floater(k[0][0])
            s=['','+','-'][int(k[0][0]//abs(k[0][0]))]
            if d==1 and s=='+':
                s=''
            a+=s+c
            f=0
            if len([x for x in k[0][1] if x!=0])>1:
                a+=r'\left('
            for i in range(len(k[0][1])):
                if k[0][1][i]!=0:
                    f+=1
                    c=floater(k[0][1][i])
                    s=['','+','-'][int(k[0][1][i]//abs(k[0][1][i]))]
                    if f==1 and s=='+':
                        s=''
                    a+=s+c+'x_'+str(i)
            if len([x for x in k[0][1] if x!=0])>1:
                a+=r'\right)'
            a+='^2'
    a=a+'$'
    return print(a)
