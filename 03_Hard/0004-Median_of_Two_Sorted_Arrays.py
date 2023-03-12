# ==============================================================================
#* Median of Two Sorted Arrays
#* Given two sorted arrays nums1 and nums2
#* of size m and n respectively, return the
#* median of the two sorted arrays.
#* The overall run time complexity should be O(log (m+n)).
# ==============================================================================
from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # m = len(nums1)
        # n = len(nums2)
        merged_list = nums1
        merged_list.extend(nums2)
        merged_list = sorted(merged_list)
        mll = len(merged_list) # Merged List Lenght
        median = 0
        if mll % 2 == 0:
            median = (merged_list[(mll//2)-1] + merged_list[mll//2]) / 2
        else:
            median = merged_list[mll//2]
        return float(median)
        
my_solution = Solution()

print(my_solution.findMedianSortedArrays([1,2], [3,4]))
print(my_solution.findMedianSortedArrays([1,3], [2]))