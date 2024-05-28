## https://leetcode.com/problems/two-sum/
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Brute force solution - Time complexity of O(n^2) and Space complexity of O(n)
        for i in range(0, len(nums) - 1):
            for j in range(i + 1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
        # Solution with the space complexity of O(n) and time complexity will be O(n)
        hash_map = {}
        for i in range(0, len(nums)):
            if nums[i] in hash_map.keys():
                return [i, hash_map[nums[i]]]
            hash_map[target - nums[i]] = i