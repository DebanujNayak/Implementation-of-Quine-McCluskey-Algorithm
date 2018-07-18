from random import randint

def check(n,l1,l11,l2):


    for i in range(100):
        A = []
        s = set([])
        for i in range(n):
            A.append(str(randint(0,1)))

        if ''.join(A) in l11:
            s.add(True)
            continue


        l1o = 0
        l2o = 0
        for i in l1:
            chk = 1
            for j in range(len(i)):
                if A[j] != i[j] and i[j] != 'x':
                    chk = 0
            l1o = l1o|chk
            
        for i in l11:
            chk = 1
            for j in range(len(i)):
                if A[j] == i[j] or i[j] != 'x':
                    chk = 0
            l1o = l1o|chk

        for i in l2:
            chk = 1
            for j in range(len(i)):
                if A[j] != i[j] and i[j] != 'x':
                    chk = 0
            l2o = l2o | chk

        #print l1o,l2o
        s.add(l1o == l2o)

    if len(list(s)) == 1:
        return True
    else:
        False
        

