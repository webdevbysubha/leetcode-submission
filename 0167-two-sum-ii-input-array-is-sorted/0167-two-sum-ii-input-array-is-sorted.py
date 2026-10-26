class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        hash = {}
        for i in range(len(numbers)):
            rem = target - numbers[i]
            if rem in hash:
                return [hash[rem]+1,i+1]
            else:
                hash[numbers[i]] = i