import random
import time

n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []

def insertion_sort(l):
    n = len(l)
    for i in range(1, n):
        j = i - 1
        v = l[i]
        while j >= 0 and l[j] > v:
            l[j + 1] = l[j]
            j = j - 1
        l[j + 1] = v

for n in n_list:
    l = [random.randint(1, 100) for _ in range(n)]
    s_t = time.time()
    insertion_sort(l)
    e_t = time.time()
    sort_time.append(e_t - s_t)

print(n_list)
print(sort_time)

