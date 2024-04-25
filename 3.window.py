'''
209.长度最小的子数组

给定一个含有 n 个正整数的数组和一个正整数 target 。

找出该数组中满足其总和大于等于 target 的长度最小的 连续
子数组[numsl, numsl+1, ..., numsr-1, numsr] ，并返回其长度。如果不存在符合条件的子数组，返回 0 。

713.乘积小于 K 的子数组

给你一个整数数组 nums 和一个整数 k ，请你返回子数组内所有元素的乘积严格小于 k 的连续子数组的数目。

3. 无重复字符的最长子串

给定一个字符串 s ，请你找出其中不含有重复字符的 最长子串的长度。
'''

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        if sum(nums) < target:
            return 0
        s = 0
        left = 0
        res = len(nums)
        for i in range(len(nums)):
            s += nums[i]
            while s >= target:
                res = min(res, i - left + 1)
                s -= nums[left]
                left += 1
        return res
    
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if min(nums) >= k:
            return 0
        left = 0
        res = 0
        m = 1
        for i in range(len(nums)):
            m *= nums[i]
            while m >= k:
                m /= nums[left]
                left += 1
            res += i - left + 1
        return res
    
    def lengthOfLongestSubstring(self, s: str) -> int:
        if s is '':
            return 0
        res = 1
        left = 0
        d = dict()
        for i in range(len(s)):
            if s[i] not in d:
                d[s[i]] = 1
            else:
                d[s[i]] += 1
            while d[s[i]] > 1:
                d[s[left]] -= 1
                left += 1
            res = max(res, i-left+1)
        return res
