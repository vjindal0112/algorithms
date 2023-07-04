def binary_search(data: list[int], target: int) -> int:
    left = 0
    right = len(data)
    mid = (left + right) // 2
    while mid < right:
        if data[mid] == target:
            return mid
        elif target > data[mid]:
            left = mid + 1
        else:
            right = mid
        mid = (left + right) // 2
    return left