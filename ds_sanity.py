from ds_oursanitycheck import check

def binary(n):
    
    k=[]
    while (n>0):
        
        a= n%2
        k.append(a)
        n=n/2
    string=""
    for j in k[::-1]:
        string=string+str(j)
    return string


def star_out(A, B):
	star = {'0':{'0':'0','1':'p','x':'0'},
       		 '1':{'0':'p','1':'1','x':'1'},
	         'x':{'0':'0','1':'1','x':'x'}}	
	C = ''
	p_counter = 0;
	for i in xrange(len(A)):
		out = star[A[i]][B[i]]
		if (out == 'p'):
			p_counter += 1
			out = 'x'
		if (p_counter > 1):
			C = 'p'
			break
		C += out
	return C

def find_pi(initial_cover):
	C = initial_cover
	while (True):
		G = []
		for i in xrange(len(C)-1):
			for j in xrange(i+1, len(C)):
				star_val = star_out(C[i],C[j])
				#print star_val
				if (star_val != 'p'):
					G.append(star_val)
		#print G
		C_new = remove_redun(G+C)
		if (C_new == C):
			break
		else:
			C = C_new	
	return C

def remove_redun(C):
	slash = {'0':{'0':'e','1':'p','x':'j'},
		 '1':{'0':'p','1':'e','x':'j'},
		 'x':{'0':'i','1':'i','x':'e'}}		#defined a new thing to help me to find if i is in j or j is in i
	redun = []
	#print C
	for i in xrange(len(C)-1):
		for j in xrange(i+1,len(C)):
			iFlag = 0
			jFlag = 0
			slash_out = ""
			for k in xrange(len(C[i])):
				out = slash[C[i][k]][C[j][k]]
				if (out == 'p'):
					slash_out = 'p'
					break
				slash_out += out
			#print C[i],C[j],slash_out,
			#if slash_out == 'p':
			#	break
			if 'i' in slash_out:
				iFlag = 1
			if 'j' in slash_out:
				jFlag = 1
			if (iFlag == 1 and jFlag == 1):
				pass
			else:
				if (iFlag == 1):
					#print " i ",
					redun.append(C[j])
				elif (jFlag == 1):
					#print " j ",
					redun.append(C[i])
		#print
	#print redun
	#print C		
	return list((set(C).difference(set(redun))))



def sharp_out(al,b):
    c = []
    sharp = {'0':{'0':'e','1':'p','x':'e'},
             '1':{'0':'p','1':'e','x':'e'},
             'x':{'0':'1','1':'0','x':'e'}}
    for a in al:
        n = len(a)
        asb = ''
        for i in xrange(n):
            asb += sharp[a[i]][b[i]]
        d = {'0':2,'1':3,'e':5,'p':7}
        prod = 1
        for i in asb:
            prod *= d[i]
            
        if (prod%7 == 0):
            c.append(a)
        elif (prod %5==0 and prod//5 == n):
            pass
        else:
            i = 0
            while (i<n):
                if (a[i] == 'x' and b[i] != 'x'):
                    if (b[i] == '0'):
                        c.append(a[:i]+'1'+a[i+1:])
                    else:
                        c.append(a[:i]+'0'+a[i+1:])
                i+=1
    return c

def essential_pm(pi,dc):
    epi = []
    for i in xrange(len(pi)):
        is_ep = 1
        temp = [pi[i]]
        for j in xrange(len(pi)):
            if (i!=j):
                temp=sharp_out(temp,pi[j])
                if temp == []:
                    is_ep = 0
                    break
        if is_ep == 0:
            continue
        for z in dc:
            temp = sharp_out(temp,z)
            if temp == []:
                is_ep = 0
                break
        if is_ep == 1:
            epi.append(pi[i])
    return epi

#P = ['0x000','011x1','101x1','1x111','11x00','x1111','0x101','1x100','x010x','00x0x','x10x0']
#DC = ['11100','11000','01010','00101']






''' E is the list of essential prime implicants
and P is the set of prime implicants
and newP is the set of prime implicants after deleting useless ones'''
def part4(E,P,DC):
    newP=[]
    for i in P:
        if i in E:
            newP.append(i)
        else:
            flag=1
            temp=[i]                    
            for j in range(len(DC)):
                temp = sharp_out(temp,DC[j])
                if temp== []:
                    flag = 0
                    break
            if flag == 0:
                continue
            
            flag2= 1                          # temp is a list containing i # DC                                     
            for k in range(len(P)):
                if(P[k]!=i):
                    temp2= sharp_out(temp,P[k])
                    if temp2==[]:
                        flag2=0
                        break
            if flag2==1:
                newP.append(i)
    return newP

          
def rec(E,newP,DC,L):
    C = E
    nextE = E
    nextP = newP
    nextD = list(DC)
    while True:
        nextD.extend(nextE)
        nextE = essential_pm(nextP,nextD)
        
        if nextE == []:
            break
        else:
            nextP = part4(nextE,nextP,nextD)
            C.extend(nextE)

    if nextP == []:
        L.append(C)
    elif len(nextP) == 1:
        C.extend(nextP)
        L.append(C)
    else:
        rec(E+[nextP[0]], nextP[1:],nextD,L)
        rec(E,nextP[1:],nextD,L)

def part5(E,newP,DC):
    L = []
    rec(E,newP,DC,L)
    minl = len(L[0])
    for i in L:
        if len(i)<minl:
            minl = len(i)

    temp = []
    for i in L:
        if len(i) == minl:
            temp.append(i)

    maxx = 0
    for i in temp:
        x = 0
        for j in i:
                x+=j.count('x')
        if x>maxx:
            maxx = x
            
    for i in temp:
        x = 0
        for j in i:
                x+=j.count('x')
        if x==maxx:
            return list(set(i))

#top-level


b= input("number of variables = " )
a= input("List of minterms = " )
d= input("List of don'tcare = " )
f= a+d
f.sort()

l3 = []
t = []
for i in a:
    l3.append( binary(i) )

for i in range(0,len(l3)):
    t.append(((b-len(l3[i])) * "0") + str(l3[i]))

l2=[]
for i in f:
    l2.append( binary(i) )    

c = []
for i in range(0,len(l2)):
    c.append(((b-len(l2[i])) * "0") + str(l2[i]))
l1 = []
for i in d:
    l1.append( binary(i) )    

dc = []
for i in range(0,len(l1)):
    dc.append(((b-len(l1[i])) * "0") + str(l1[i]))

P = find_pi(c)

E = essential_pm(P,dc)
newP = part4(E,P,dc)      
L = part5(E,newP,dc)

print check(b,t, dc, L)
