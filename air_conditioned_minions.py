def main():
    n = int(input())
    minions = []
    for j in range(n):
        minion_new = [int(x) for x in input().split()]
        minions.append(minion_new)
    minions.sort(key=lambda minion: minion[1])
    no_of_rooms = 1
    th = minions[0][1]
    for minion in minions[1:]:
        if minion[0] > th:
            no_of_rooms += 1
            th = minion[1]

    print(no_of_rooms)
    
main() 

