##input_var = raw_input("Enter the variable names:\t")
##input_exp = raw_input("Enter the Boolean Expression:\t")
def algo_input(input_var,input_exp):
    input_varnum = len(input_var)

    exp_new = input_exp.split("+")

    exp_final = set([])                      
    for term in exp_new:
        term = term.strip()

        temp = ""
        for i in xrange(input_varnum):
            if input_var[i] not in term:
                temp += 'x'
            elif (term[term.find(input_var[i])-1] == '~'):
                temp += "0"
            else:
                temp += "1"
        exp_final.add(temp)
    return list(exp_final)   

