import math
PI_INT = math.floor((math.pi-3)*10**100)  
print(PI_INT)
E_INT = math.floor((math.e-2)*10**100)
print(E_INT)
def pi_real(n):
    pee = math.floor((math.pi - 3)*10**n)
    res = '3,' + str(pee)
    return res
def e_real(n):
    ee = math.floor((math.e -2)*10**n)
    res = '2,' + str(ee)
    return res
