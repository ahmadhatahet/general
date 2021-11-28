from time import time, sleep

def selection_sort(a):

    for i in range(0, len(a)-1):
        minIndex = i
        for j in range(i+1, len(a)):
            if a[j] < a[minIndex]:
                minIndex = j
        if minIndex != i:
            a[i], a[minIndex] = a[minIndex], a[i]


def to_check(z, z_sorted, sort_type, t):
    if z == z_sorted:
        print(f"Pass {sort_type} Test in: {time() - t}")
    else:
        print(f"Failed to sort using: {sort_type} in: {time() - t}")


if __name__=="__main__":

    z_sorted = [3, 4, 6, 6, 7, 8, 8, 9, 21, 21, 45, 73]

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    selection_sort(z)
    to_check(z, z_sorted, 'selection_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    selection_sort(z)
    to_check(z, z_sorted, 'selection_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    selection_sort(z)
    to_check(z, z_sorted, 'selection_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    selection_sort(z)
    to_check(z, z_sorted, 'selection_sort', t)