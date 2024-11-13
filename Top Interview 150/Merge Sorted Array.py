class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        nums1_copy = nums1[:m]
        index = 0

        def safe_pop(my_list, default=float('inf')):
            if my_list:
                return my_list.pop(0)
            else:
                return default
        
        while index < m+n:
            item_nums1 = safe_pop(nums1_copy)
            item_nums2 = safe_pop(nums2)

            if item_nums1 <= item_nums2:
                nums1[index] = item_nums1
                nums2.insert(0, item_nums2)
            elif item_nums2 < item_nums1:
                nums1[index] = item_nums2
                nums1_copy.insert(0, item_nums1)

            index += 1
