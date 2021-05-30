def main():
    datasets = int(input())
    for _ in range(datasets):
        n, m = [int(x) for x in input().split(" ")]
        l = [int(x) for x in input().split(" ")]
        pos_min = [i for i, x in enumerate(l) if x == m]
        maximum = 0
        for k in pos_min:
            sum = m
            i = k - 1
            j = k + 1
            while i >= 0 and l[i] > m:
                sum += l[i]
                i -= 1
            while j < n and l[j] > m:
                sum += l[j]
                j += 1
            maximum = max(maximum, sum)

        print(maximum)

main()