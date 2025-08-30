from pyeda import *
from pyeda.inter import *
import math
import random
import time
import matplotlib.pyplot as plt


for i in range(80):
    exec("x{}=exprvar('x',{})".format(i,i))




def RSANDbdd(bdd_list):
    #print(bdd_list2)
    m = len(bdd_list)
    #print("len is", m)
    if (m == 1):
        print(bdd_list[0])
        return(bdd_list[0])
        #print("m=1 ")
        #print("output value is")
        #print(bdd_list2)
       
        
    else:
        m1 = math.floor((m+1)/2)
        #print("m1 is ", m1)

        bddlist1 = list()
        for i in range(m1-1):
            bddlist1.append(bdd_list[i]&  bdd_list[m-i-1])

        if (m % 2) == 1:
            bddlist1.append(bdd_list[m1-1])
        else:
            bddlist1.append((bdd_list[m1-1] & bdd_list[m1]))
        #print(bddlist1)
    RSANDbdd(bddlist1)

#eqn_array=[x1&x2+x3&x4+x5, x2&x5&x3+x7, x9&x3&x2+x6&x7, x8&x2&x1^x5&x2&x1^x3, x5&x1&x3^x7^x8]
eqn_array=[x1&x3, x2&x3]
bdd_list=list()
for i in range(len(eqn_array)):
    bdd_list.append(expr2bdd(eqn_array[i]))
print(bdd_list)
def bdd_check(bdd_list):
    m=len(bdd_list)
    if m==1:
        print(bdd_list[0])
        return bdd_list[0]
    else:
        m1=math.floor((m+1)/2)
    bdd_list_new=list()
    for i in range(m1-2):
        bdd_list_new.append(bdd_list[i]&bdd_list[m-i-1])
    if m%2==1:
        bdd_list_new.append(bdd_list[m1])
    else:
        bdd_list_new.append(bdd_list[m1-1]&bdd_list[m1])
    return(bdd_check(bdd_list_new))







    
#res_bdd=RSANDbdd(bdd_list)
#print(res_bdd)
res_check=bdd_check(bdd_list)
print(list(res_check.satisfy_all()))