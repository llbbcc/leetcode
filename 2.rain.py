'''
11.盛最多雨水的容器

给定一个长度为 n 的整数数组 height 。有 n 条垂线，第 i 条线的两个端点是 (i, 0) 和 (i, height[i]) 。

找出其中的两条线，使得它们与 x 轴共同构成的容器可以容纳最多的水。

返回容器可以储存的最大水量。

说明：你不能倾斜容器。

42.接雨水

给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right = 0, len(height) - 1
        res = 0
        while left < right:
            res = max(res, (right-left)*min(height[left], height[right]))
            if height[left] <= height[right]:
                left += 1
            else:
                right -= 1
        return res
    
    def trap(self, height: List[int]) -> int:
        pre = [height[0]]
        for i in range(1, len(height)):
            pre.append(max(pre[-1], height[i]))
        suf = [height[-1]]
        for i in range(len(height)-2, -1, -1):
            suf.append(max(suf[-1], height[i]))
        res = 0
        for i in range(len(height)):
            res += min(pre[i],suf[-(i+1)]) - height[i]
        return res