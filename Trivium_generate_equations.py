# This program generate equations for trivium in 'n' rounds. 


# Key size = 80 bits
# IV size= 80 bits
# Internal state= 288 bits. 
from sympy.logic.boolalg import And, Or, Not, Xor
import sympy as sp
import random
from sympy.logic.boolalg import to_anf
n=288
variables=5
rounds=1152
iterations=10

file=open("output_new.txt", 'w')
k= sp.symbols(f'x0:{n}')
iv=list()


for i in range(80):
    iv.append(random.randint(0,1))
s=list()
for i in range(variables):
    s.append(k[i])
for i in range(80-variables):
    s.append(random.randint(0,1))
for i in range(13):
    s.append(0)

for i in range(80):
    s.append(iv[i])
for i in range(4):
    s.append(0)
for i in range(108):
    s.append(0)
for i in range(3):
    s.append(1)

print(s)
print(len(s))
'''

s=list()

for i in range(variables):
    s.append(k[i])
for i in range(288-variables):
    s.append(random.randint(0,1))
'''
#initialization

#t1=(s[65] and s[91])
for __ in range(rounds):
    t1=Xor(s[65],And(s[90],s[91]),s[92], s[170])
    t2=Xor(s[161], And(s[174], s[175]), s[176], s[263])
    t3=Xor(s[242], And(s[285], s[286]), s[287], s[68])

    for i in range(92, 0, -1):
        s[i]=s[i-1]
    s[0]=t3

    for i in range(176, 93,-1):
        s[i]=s[i-1]
    s[93]=t1
    for i in range(287,177,-1):
        s[i]=s[i-1]
    s[177]= t2
    print("after round", __)
    file.write("after round ")
    file.write(str(__))

    #print(s)
    #file.write(str(s))

file.close()
#############################################
#running cipher

z=list()

for i in range(iterations):
    t1=Xor(s[65], s[93])
    t2=Xor(s[161], s[176])
    t3=Xor(s[242], s[287])
    z.append(Xor(t1, t2, t3))
    t1= Xor(t1, And(s[90], s[91]), s[170])
    t2= Xor(t2, And(s[174], s[175]), s[263])
    t3= Xor(t3, And(s[285], s[286]), s[68])

    for j in range(92, 0, -1):
        s[j]=s[j-1]
    s[0]=t3

    for j in range(176, 93,-1):
        s[j]=s[j-1]
    s[93]=t1
    for j in range(287,177,-1):
        s[j]=s[j-1]
    s[177]= t2

#for i in range(len(z)):
    #z[i]= to_anf(z[i])

print("z is ")

print(z)

file=open("z_output_new.txt", 'w')
#for eq in z:
    #eq=eq.to_anf()
#file.write("z is \n")
#for i in range(len(z)):
    #z[i]=(z[i])
    #file.write("z bit no. \n" )
    #file.write(str(i)+ "\n")
    #file.write(str(z[i]))
file.write(str(z))

file.close()









#############################################################
#copied program

