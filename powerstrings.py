from math import sqrt
    
def generate_divisors(l):
    array = []
    m = int(sqrt(l))
    for i in range(1, m+1):
        if l%i==0: 
            array.append(i)
            array.append(int(l/i))
    return sorted(array)

def alternative(stringa):
    l = len(stringa)
    possible_numbers = generate_divisors(l)
    for i in possible_numbers:
        ind_i = int(l-i)
        ind_f = int(l)
        rep = int(l/i)
        if stringa[ind_i:ind_f]*rep == stringa: return rep
    return 1

def main():
    point = False
    while not point:
        stringa = input()
        if stringa == '.': point = True
        else: print(alternative(stringa))
main()
