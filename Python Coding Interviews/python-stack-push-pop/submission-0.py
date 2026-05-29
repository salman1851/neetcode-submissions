from typing import List


def reverse_list(arr: List[int]) -> List[int]:
    rev_list = []
    while arr:
        rev_list.append(arr.pop())
    return rev_list

# do not modify below this line
print(reverse_list([1, 2, 3]))
print(reverse_list([3, 2, 1, 4, 6, 2]))
print(reverse_list([1, 9, 7, 3, 2, 1, 4, 6, 2]))
