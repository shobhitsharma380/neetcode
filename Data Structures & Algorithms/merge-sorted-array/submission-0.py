class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if any(nums1):
            nums1[m:] = nums2
            for i, n in enumerate(nums1):
                while 0 <= i < len(nums1) - 1 and (nums1[i] > nums1[i+1]):
                    temp = nums1[i]
                    nums1[i] = nums1[i+1]
                    nums1[i+1] = temp
                    i -= 1
        else:
            nums1[m:] = nums2



        