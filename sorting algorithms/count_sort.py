from time import time, sleep

def count_sort(a):
    k = max(a)
    count = [0] * (k+1)
    for j in range(0, len(a)):
        count[ a[j] ] += 1

    total = 0
    for i in range(0, k+1):
        oldCount = count[i]
        count[i] = total
        total += oldCount

    output = [0] * (len(a))
    for j in range(0, len(a)):
        element = a[j]
        targetIndex = count[element]
        output[targetIndex] = element
        count[element] += 1

    return output


def to_check(z, z_sorted, sort_type, t):
    if z == z_sorted:
        print(f"Pass {sort_type} Test in: {time() - t}")
    else:
        print(f"Failed to sort using: {sort_type} in: {time() - t}")


if __name__=="__main__":

    z_sorted = [3, 4, 6, 6, 7, 8, 8, 9, 21, 21, 45, 73]

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    z = count_sort(z)
    to_check(z, z_sorted, 'count_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    z = count_sort(z)
    to_check(z, z_sorted, 'count_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    z = count_sort(z)
    to_check(z, z_sorted, 'count_sort', t)

    sleep(1)

    t = time()
    z = [6,7,73,45,8,3,21,6,8,9,21,4]
    z = count_sort(z)
    to_check(z, z_sorted, 'count_sort', t)