

def get_and(k,st):
    stn="("+st
    for j in range(len(k)):
        if k[j]=="1":
            stn+=",x"+("%d"%(j+1))
        elif k[j]=="0":
            stn+=",~x"+("%d"%(j+1))
        else:
            continue
    return "and"+stn+");"

def get_or(lst):
    stn="or(out"
    for i in range(len(lst)):
        stn=stn +",y"+str(i+1)
    return stn+");"
        
def make_func(name,lst):
    F=open(name+".txt","w")             #make this a
    F.write("\n\n")                     #add this line
    stn="module "+str(name)+"(out"
    for i in range(len(lst[0])):
        stn=stn+",x"+str(i+1)
    stn=stn+");"
    print stn
    F.write(stn+"\n")

    stn2="input"
    stn2 += " x" + str(1)
    for i in range(1,len(lst[0])):
        stn2=stn2+",x"+str(i+1)
    stn2=stn2+";"
    print stn2
    print "output out;"
    print
    F.write(stn2+"\n")
    F.write("output out;\n")
    F.write("\n")
    
    for i in range(len(lst)):
        print "\t"+get_and(lst[i],"y"+str(i+1))
        F.write("\t"+get_and(lst[i],"y"+str(i+1))+"\n")
    print "\t"+get_or (lst)
    print
    print "endmodule"
    F.write("\t"+get_or (lst)+"\n")
    F.write("\n")
    F.write("endmodule")

    F.close()
    

#make_func("decoder",['0x000','011x1','101x1','1x111','11x00','x1111','0x101','1x100','x010x','00x0x','x10x0'])

#### This part needs to be removed
##input_var = "ab"
###raw_input("Enter the variable names:\t")
##input_var = input_var.strip()
##input_varnum = len(input_var)
##
##size = []
##
##for i in xrange(input_varnum):
##    size.append(2)
##    #input("Enter the size of " + str(input_var[i])+"\t\t"))
##
##input_exp = [['110x','0000','xx11'],['1000','111x']]
## Till here


#raw_input("Enter the file name:\t")

## Function starts here
def out(input_var, input_exp,size,total_size):
    output_file = "main_output"
    F = open(output_file + ".txt", "w")
    input_varnum = len(input_var)

    line = "module " + output_file + "(out"
    for i in xrange(input_varnum):
        line += "," + input_var[i]
    line += ");"
    print line
    F.write(line+"\n")

    line = ""
    for i in xrange(input_varnum):
        line += "input [" + str(size[i]) + ":0] " + input_var[i] + ";\n"
    print line,
    F.write(line)

    maxSize = len(input_exp)

    line = "output [" + str(maxSize) + ":0]" + " out;"
    print line
    F.write(line + "\n")

    for i in range(maxSize):
        #print 'x'*input_varnum,input_exp[i]
        if 'x'*total_size in input_exp[i]:
            if input_exp[i][0] == 'x'*total_size:
                a = input_exp[i][1]
            else:
                a = input_exp[i][0]
            line = "assign out[" + str(i) + "] = " + a + ";"
        else:
            line = "out" + str(i) + " inst" + str(i) + "(out[" + str(i) + "]"
            for i in xrange(input_varnum):
                for j in xrange(size[i]):
                    line += "," + input_var[i] + '[' + str(j )+ ']'
            line += ");"
        print line
        F.write(line + "\n")

    print "endmodule"
    F.write("endmodule\n")

    for i in range(maxSize):
        if 'x'*total_size in input_exp[i]:
            continue
        else:
            make_func("out"+str(i), input_exp[i])

    F.close()

## Function ends here

