'''
34. 在排序数组中查找元素的第一个和最后一个位置

给你一个按照非递减顺序排列的整数数组 nums，和一个目标值 target。请你找出给定目标值在数组中的开始位置和结束位置。

如果数组中不存在目标值 target，返回 [-1, -1]。

你必须设计并实现时间复杂度为 O(log n) 的算法解决此问题。
'''

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def search(nums, target):
            left, right = 0, len(nums) - 1
            while left <= right:
                mid = left + (right - left) // 2
                if nums[mid] < target:
                    left += 1
                else:
                    right -= 1
            return left
        if len(nums) == 0 or nums[0] > target or nums[-1] < target:
            return [-1, -1]
        left = search(nums, target)
        right = search(nums, target+1) - 1
        if nums[left] == nums[right]:
            return [left, right]
        else:
            return [-1, -1]