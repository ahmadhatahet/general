from time import time, sleep

def get_pivot_quick_sort(a, low, hi):
    mid = (low + hi) // 2
    pivot = hi
    if a[low] < a[mid]:
        if a[mid] < a[hi]:
            pivot = mid
        elif a[low] < a[hi]:
            pivot = low

    return pivot

def partition_quick_sort(a, low, hi):
    pivot_index=get_pivot_quick_sort(a, low, hi)
    pivot_value=a[pivot_index]

    a[pivot_index], a[low] = a[low], a[pivot_index]

    border = low
    for i in range(low, hi+1):
        if a[i] < pivot_value:
            border += 1
            a[i], a[border] = a[border], a[i]

    a[low], a[border] = a[border], a[low]

    return border

def quick_sort_temp(a, low, hi):
    if low < hi:
        p = partition_quick_sort(a, low, hi)
        quick_sort_temp(a, low, p-1)
        quick_sort_temp(a, p+1, hi)

def quick_sort(a):
    quick_sort_temp(a, 0, len(a)-1)


def to_check(z, z_sorted, sort_type, t):
    if z == z_sorted:
        print(f"Pass {sort_type} Test in: {time() - t}")
    else:
        print(f"Failed to sort using: {sort_type} in: {time() - t}")


if __name__=="__main__":

    z_sorted = [3, 4, 6, 6, 7, 8, 8, 9, 21, 21, 45, 73]

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    quick_sort(z)
    to_check(z, z_sorted, 'quick_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    quick_sort(z)
    to_check(z, z_sorted, 'quick_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    quick_sort(z)
    to_check(z, z_sorted, 'quick_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    quick_sort(z)
    to_check(z, z_sorted, 'quick_sort', t)