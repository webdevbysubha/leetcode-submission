class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        countzero = countone = counttwo = 0;
        n = len(nums)
        for i in range(n):
            if nums[i] == 0:
                countzero += 1
            elif nums[i] == 1:
                countone += 1
            else:
                counttwo += 1
        i = 0
        while countzero > 0:
            nums[i] = 0
            countzero -= 1
            i += 1
        while countone > 0:
            nums[i] = 1
            countone -= 1
            i += 1
        while counttwo > 0:
            nums[i] = 2
            counttwo -= 1
            i += 1
        