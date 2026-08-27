from typing import List

# median of two sorted arrays
def findMedianSortedArrays(nums1: List[int], nums2: List[int]) -> float:
    nums = nums1 + nums2
    nums.sort()

    length = len(nums)
    middle = length // 2

    if length % 2 == 0:
        median = (nums[middle - 1] + nums[middle]) / 2
    else:
        median = float(nums[middle])

    return median

print(findMedianSortedArrays([1,3],[2])) # Output: 2.0
