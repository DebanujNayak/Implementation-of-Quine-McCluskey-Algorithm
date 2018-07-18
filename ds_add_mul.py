from ds_parser import mynot, myand, myxor, myor
def full_add(a,b,cin):
    summ=myxor(myxor(a,b),cin)
    carry=myor(myor(myand(a,b),myand(a,cin)),myand(b,cin))
    return summ,carry

def adder(A,B):
    a=len(A)
    b=len(B)   
    if a==b:
        P=list(A)
        Q=list(B)
        m=a
    elif a>b:
        P=list(A)
        Q=list(B)+(['0']*(a-b))
        m=a
    else:
        P=list(A)+(['0']*(b-a))
        Q=list(B)
        m=b


    S=['0']*(m+1)
    summ,carry=full_add(P[0],Q[0],'0')
    S[0]=summ   
    for i in range(1,m-1):        
        summ,carry = full_add(P[i],Q[i],carry)
        S[i]=summ
    summ,carry=full_add(P[m-1],Q[m-1],carry)
    S[m-1]=summ
    S[m]=carry

    return S

def multiplier(M,Q):
    ans=['0']*(len(M)+len(Q))
    shift=0    
    step=['0']*(len(M)+1)
    for i in range(len(M)):
        step[i]= myand(M[i],Q[0])
        
    ans[shift]=step[0]
    shift+=1
    for i in range(1,len(Q)):
        P=['0']*len(M)
        for j in range(len(M)):
            P[j]=myand(M[j],Q[i])
        step=adder(step[1:],P)
        ans[shift]=step[0]
        shift+=1

    for i in range(len(step)):
        ans[shift+i-1]=step[i]
        
    return ans

            

        
            
            
            
        
    
