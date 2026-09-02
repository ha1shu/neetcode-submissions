class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merge = nums1 + nums2
        

        merge.sort()

        totalLength = len(merge)


        mid = totalLength // 2

        if totalLength % 2 == 0:
            return (merge[mid-1] + merge[mid]) /2.0
        else:
            return merge[mid]



        