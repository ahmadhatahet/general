from time import time, sleep

def merge_sort(a):
    if len(a) < 2:
        return a

    mid = len(a) // 2
    L = a[:mid]
    R = a[mid:]

    merge_sort(L)
    merge_sort(R)

    i = j = k = 0

    while i < len(L) and j < len(R):
        if L[i] < R[j]:
            a[k] = L[i]
            i+=1
        else:
            a[k] = R[j]
            j+=1
        k+=1

    while i < len(L):
        a[k] = L[i]
        i+=1
        k+=1
    while j < len(R):
        a[k] = R[j]
        j+=1
        k+=1


def to_check(z, z_sorted, sort_type, t):
    if z == z_sorted:
        print(f"Pass {sort_type} Test in: {time() - t}")
    else:
        print(f"Failed to sort using: {sort_type} in: {time() - t}")


if __name__=="__main__":

    z_sorted = [3, 4, 6, 6, 7, 8, 8, 9, 21, 21, 45, 73]

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    merge_sort(z)
    to_check(z, z_sorted, 'merge_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    merge_sort(z)
    to_check(z, z_sorted, 'merge_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    merge_sort(z)
    to_check(z, z_sorted, 'merge_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    merge_sort(z)
    to_check(z, z_sorted, 'merge_sort', t)