nums = [3,2,4]
target = 6


class Solution:
    def space(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n2).
        Space complexity: O(1).
        """
        for n, i in enumerate(nums):
            for m, j in enumerate(nums):
                if n != m:
                    if i + j == target:
                        return [n,m]

    def time(self, nums: list[int], target: int) -> list[int]:
        """
        Time complexity: O(n).
        Space complexity: O(n).
        """
        hashmap = {}
        for n, i in enumerate(nums):
            complement = target - i
            if complement in hashmap:
                return [n, hashmap[complement]]
            hashmap[i] = n

            
solution = Solution()

print("Space Complexity:")
print(solution.space(nums=nums, target=target))

print("Time Complexity:")
print(solution.time(nums=nums, target=target))
