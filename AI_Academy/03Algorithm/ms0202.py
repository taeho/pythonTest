def thirdMax(nums):
    return quickSelect(nums, 0, len(nums) - 1, 2)


def quickSelect(nums, start, end, k):
    if start == end:
        return nums[start]

    left, right = start, end
    pivot = nums[(left + right) // 2]

    while left <= right:
        while left <= right and nums[left] > pivot:
            left += 1
        while left <= right and nums[right] < pivot:
            right -= 1
        if left <= right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

    if right >= k and start <= right:
        return quickSelect(nums, start, right, k)
    elif left <= k and left <= end:
        return quickSelect(nums, left, end, k)
    else:
        return nums[k]


def main():
    print(thirdMax([2, 8, 19, 37, 4, 5, 12, 50, 1, 34, 23]))  # should return 34


if __name__ == "__main__":
    main()
