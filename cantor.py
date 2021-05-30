def tmp_cantor(n) :
    for i in range(9):
        n *= 3
        tmp = int(n%3)
        if tmp == 1: return 'NON-MEMBER'
    return 'MEMBER' 

def main():
    while(True):
        inp = input()
        if inp == 'END': return
        else:
            n = float(inp)
            print(tmp_cantor(n))
main()