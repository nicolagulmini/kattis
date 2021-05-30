def tape(array):
    cost = 0
    for i in range(len(array)-1, 0, -1):
        papermake = array[i]/2
        cost += papermake*(2**((-2*i-1)/4))
        array[i-1] += papermake
    return cost

def main():
    n = int(input()) # useless !!
    papers = []
    papers.append(0)
    inp = [int(x) for x in input().split()]
    needed = 2
    for i in range(len(inp)):
        prov = inp[i]
        if prov < needed:
            needed = 2*(needed-prov)
            papers.append(prov)
        else:
            papers.append(needed)
            return tape(papers)
    return 'impossible'
print(main())





