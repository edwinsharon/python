nums=[2,7,11,15]
target=9
for i in range(len(nums)):
    for k in range(len(nums)):
        t=nums[i]+nums[k]
        if t==target:
            print(i,k)

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         n = len(nums)
#         for i in range(n - 1):
#             for j in range(i + 1, n):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]
#         return []  # No solution found