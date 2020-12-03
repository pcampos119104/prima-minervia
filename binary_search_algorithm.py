# https://www.techiedelight.com/binary-search/
from typing import List


def binary_search(l: List, x: int) -> int:
    (left, right) = (0, len(l) - 1)

    while left <= right:
        mid = (left + right) // 2
        if x == l[mid]:
            return mid
        elif x < l[mid]:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def recursive_binary_search(l: List, left: int, right: int, x: int) -> int:
    if left > right:
        return -1
    mid = (left + right) // 2

    if x == l[mid]:
        return mid
    elif x < l[mid]:
        return recursive_binary_search(l, left, mid - 1, x)
    else:
        return recursive_binary_search(l, mid + 1, right, x)


if __name__ == '__main__':

    A = [2, 5, 6, 8, 9, 10]
    key = 5

    index = binary_search(A, key)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")

    (left, right) = (0, len(A) - 1)
    index = recursive_binary_search(A, left, right, key)

    if index != -1:
        print("Element found at index", index)
    else:
        print("Element found not in the list")
