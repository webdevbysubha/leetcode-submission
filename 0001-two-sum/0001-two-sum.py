class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        hash = {}
        for i in range(len(nums)):
            rem = target - nums[i]
            if rem in hash:
                return [hash[rem],i]
            else:
                hash[nums[i]] = i

        