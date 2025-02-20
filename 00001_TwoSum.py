"""
time complexity: O(nlogn), depend on sorting algorithm
space complexity: O(n)
"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        nums_sorted = sorted(nums)
        index1 = 0
        index2 = len(nums_sorted) - 1
        while True:
            if nums_sorted[index1] + nums_sorted[index2] > target:
                index2 = index2 - 1
            elif nums_sorted[index1] + nums_sorted[index2] < target:
                index1 = index1 + 1
            elif nums_sorted[index1] + nums_sorted[index2] == target:
                break
        if nums_sorted[index1] != nums_sorted[index2]:
            return [nums.index(nums_sorted[index1]), nums.index(nums_sorted[index2])]
        else:
            place1 = nums.index(nums_sorted[index1])
            nums.reverse()
            place2 = nums.index(nums_sorted[index2])
            return [place1, len(nums) - 1 - place2]

"""
time complexity: O(n^2)
space complexity: O(1)

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        size = len(nums)
        for i in range(size):
            for j in range(i + 1, size):
                if target == nums[i] + nums[j]:
                    return [i, j]
"""