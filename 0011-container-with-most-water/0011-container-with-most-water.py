class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left = 0
        right = n - 1
        maxWater = 0
        while left < right:
            l = min(height[left],height[right])
            w = right - left
            area = l * w
            maxWater = max(maxWater,area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxWater
