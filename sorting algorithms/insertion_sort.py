from time import time, sleep

def insertion_sort(a):

    for i in range(1, len(a)):

        key = a[i]
        j = i-1
        while j >= 0 and key < a[j] :
                a[j + 1] = a[j]
                j -= 1
        a[j + 1] = key


def to_check(z, z_sorted, sort_type, t):
    if z == z_sorted:
        print(f"Pass {sort_type} Test in: {time() - t}")
    else:
        print(f"Failed to sort using: {sort_type} in: {time() - t}")


if __name__=="__main__":

    z_sorted = [3, 4, 6, 6, 7, 8, 8, 9, 21, 21, 45, 73]

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    insertion_sort(z)
    to_check(z, z_sorted, 'insertion_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    insertion_sort(z)
    to_check(z, z_sorted, 'insertion_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    insertion_sort(z)
    to_check(z, z_sorted, 'insertion_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    insertion_sort(z)
    to_check(z, z_sorted, 'insertion_sort', t)