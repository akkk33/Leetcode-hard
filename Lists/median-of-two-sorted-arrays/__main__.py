"""
URL: https://leetcode.com/problems/median-of-two-sorted-arrays/

Description:

There are two sorted arrays nums1 and nums2 of size m and n respectively.

Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

You may assume nums1 and nums2 cannot be both empty.

Example 1:

nums1 = [1, 3]
nums2 = [2]

The median is 2.0
Example 2:

nums1 = [1, 2]
nums2 = [3, 4]

The median is (2 + 3)/2 = 2.5

"""


class Solution:
    def findMedianSortedArrays(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: float
        """
        if len(sorted(nums1 + nums2)) > 0:
            if len(sorted(nums1 + nums2)) % 2 != 0:
                return sorted(nums1 + nums2)[int(len(sorted(nums1 + nums2)) / 2)]
            else:
                result = (sorted(nums1 + nums2)[(int(len(sorted(nums1 + nums2)) / 2)) - 1] + sorted(nums1 + nums2)[int(len(sorted(nums1 + nums2)) / 2)]) / 2
                return result


nums1 = [1,2]
nums2 = [3]
example = Solution()
print(example.findMedianSortedArrays(nums1, nums2))

"""
Result: Runtime: 156 ms, faster than 23.82% of Python3 online submissions for Median of Two Sorted Arrays.
"""