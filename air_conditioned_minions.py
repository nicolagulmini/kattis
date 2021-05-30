# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 08:42:11 2019

@author: Nicola Gulmini
"""
# NON FUNZIONA!! Dovevo ordinare e prendere gli upper bound
'''
def method(input):
    # sort!
    count = 1
    index = 0
    # print(input)
    for i in range(len(input)):
        # print(i)
        query = input[i][0]
        fixed = input[index][1]
        if query > fixed:
            count += 1
            index = i
    return count

m_new = [int(x) for x in input.split(" ")]
minions.sort(key=lambda x: x[1])

// modificare

in_1 = [[1,2],
        [2,4],
        [5,6]]

in_2 = [[1,2],
        [3,5],
        [4,6],
        [7,9],
        [8,10]]

print(method(in_2))
'''

# questo è giusto: verificato con Kattis

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

