def myxor(a,b):
    if (a == '0'):
        return b
    elif (b=='0'):
        return a
    elif (a == '1'):
        return mynot(b)
    elif (b == '1'):
        return mynot(a)
    axorb = ''
    an = mynot(a)
    bn = mynot(b)
    axorb = myor(myand(an,b),myand(a,bn))
    if axorb == '':
        return '0'
    return axorb

def myand(a,b):
 
    if (a=='0' or b == '0'):
        return '0'

    tempa = a.split(' + ')
    tempb = b.split(' + ')
    
    while ('0' in tempa):
        tempa.remove('0')
    while ('0' in tempb):
        tempb.remove('0')

    a = ' + '.join(tempa)
    b = ' + '.join(tempb)

    if ('1' in tempa):
        return b
    elif ('1' in tempb):
        return a
    
    al = a.split('+')
    for i in xrange(len(al)):
        al[i] = al[i].strip()
    bl = b.split('+')
    
    for i in xrange(len(bl)):
        bl[i] = bl[i].strip()

    for i in xrange(len(al)):
        t = []
        j1 = 0
        j = 0
        while j < len(al[i]):
            if (j == len(al[i]) -1 or (al[i][j].isdigit() and (al[i][j+1].isalpha() or al[i][j+1] == '~'))):
                t.append(al[i][j1:j+1])
                j += 1
                j1 = j
            else:
                j+=1
        al[i] = list(set(t))

    for i in xrange(len(bl)):
        t = []
        j1 = 0
        j = 0
        while j < len(bl[i]):
            if (j == len(bl[i]) -1 or (bl[i][j].isdigit() and (bl[i][j+1].isalpha() or bl[i][j+1] == '~'))):
                t.append(bl[i][j1:j+1])
                j += 1
                j1 = j
            else:
                j+=1
        bl[i] = list(set(t))

    aandb = ''
    aandbs = set([])
    for i in al:
        
        for j in bl:
            flag = 1
            temp = set(i)
            
            for z in j:
                
                if z[0] == '~':
                    if z[1:] in temp:
                        temp = set([])
                        flag = 0
                        break
                else:
                    if ('~' + z) in temp:
                        temp = set([])
                        flag = 0
                        break

            if flag == 1:
                temp|=set(j)
                aandbs.add(''.join(list(temp)))

    aandb = ' + '.join(list(aandbs))
    if aandb == '':
        return '0'
    
    return aandb

def mynot(a):
    if (a == '0'):
        return '1'
    elif (a == '1'):
        return '0'
    al = a.split('+')
    for i in xrange(len(al)):
        al[i] = al[i].strip()
    for i in xrange(len(al)):
        temps = ''
        tildaflag = False
        j = 0
        varstring =''
        while j < len(al[i]):
            z = al[i][j]
            if z.isalpha():
                varstring = z
                j+=1
                continue
            if z.isdigit():
                varstring += z
                j+=1
                try :
                    if al[i][j].isdigit():
                    
                        continue
                    else:
                        if tildaflag:
                                temps += varstring + ' + '
                                tildaflag = False
                                continue
                        else:
                                temps += '~' + varstring + ' + '
                                continue
                except (IndexError):
                    if tildaflag:
                                temps += varstring
                                tildaflag = False
                                
                    else:
                                temps += '~' + varstring
                               
                    break
            try:
                z = al[i][j]  
                if z == '~':
                    tildaflag = True
                    varstring = ''
                else:
                    varstring = z
                    tildaflag = False

                j+=1
            except:
                pass
        al[i] = temps.rstrip(' +')

    nota = ''
    nota = reduce(myand,al)
    if nota == '':
        return '0'
    return nota
            
        

def myor(a,b):

    tempa = a.split(' + ')
    tempb = b.split(' + ')
    if ('1' in tempa or '1' in tempb):
        return '1'
    while ('0' in tempa):
        tempa.remove('0')
    while ('0' in tempb):
        tempb.remove('0')

    tempa = set(tempa)
    tempb = set(tempb)
    temp = tempa | tempb

    #a = ' + '.join(tempa)
    #b = ' + '.join(tempb)
    #print b
    aorb = ' + '.join(list(temp))
    if aorb == '':
        return '0'

    return aorb


