def squaresSorted(sortedArr):
    sorted = []
    for i in sortedArr:
        sorted.append(i*i)
    sorted.sort()
    return sorted


print(squaresSorted([-4, -1, 0, 3, 10]))

# O(nlogn) time | O(n) space


def squaredSorted(sortedArr):
    n = len(sortedArr)
    result = [0] * n
    i = 0
    j = n - 1
    index = n - 1

    while j >= i:
        left_square = sortedArr[i] ** 2
        right_square = sortedArr[j] ** 2

        if left_square > right_square:
            result[index] = left_square
            i += 1
        else:
            result[index] = right_square
            j -= 1
        index -= 1

    return result


print(squaredSorted([-4, -1, 0, 3, 10]))

# O(n) time | O(n) space