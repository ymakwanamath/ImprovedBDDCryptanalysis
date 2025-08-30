from pyeda import *
from pyeda.inter import *
import math
import random
import time
import matplotlib.pyplot as plt
import numpy as np


import sys


sys.setrecursionlimit(100000)
for i in range(288):
    exec("x{}=exprvar('x',{})".format(i,i))



eqn1=x1^(x2&x3)^x4
eqn2=x3^(x1&x2)

eqn3=eqn1&eqn2
print(eqn3)