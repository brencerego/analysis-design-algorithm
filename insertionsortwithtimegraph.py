import random
import time
import matplotlib.pyplot as plt
def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        j = i - 1
        v = arr[i]
        while j >= 0 and arr[j] > v:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = v

n_list = [5000, 6000, 7000, 8000, 9000, 10000]
sort_time = []

for n in n_list:
    l = [random.randint(1, 100) for _ in range(n)]

    s_t = time.time()
    insertion_sort(l)
    e_t = time.time()

    sort_time.append(e_t - s_t)

print("Input sizes:", n_list)
print("Sorting times:", sort_time)


#plotting the graph
plt.plot(n_list,sort_time, marker='x')
plt.xlabel("Number of Elements (n)")
plt.ylabel("Time Taken (seconds)")
plt.title("Insertion sort sort: Time Complexity Analysis")
plt.grid(True)
#save the plot
plt.savefig("Insertion_sort_time_complexity.png", dpi=300, bbox_inches='tight')
plt.show()