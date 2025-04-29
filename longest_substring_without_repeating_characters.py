"""
Complexity:
Time: O(n)
Space: O(min(n, m)), where m is the size of the character set

How this works:
char_index: keeps track of the last index each character was seen at.
left: marks the start of the current window of unique characters.
When a duplicate is found within the current window, move left past it.
max_len is updated if the current window is longer.
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        char_index = {}
        left = 0
        max_len = 0

        for right, char in enumerate(s):
            if char in char_index:
                if char_index[char] >= left:
                    left = char_index[char] + 1
            char_index[char] = right
            max_len = max(max_len, right - left + 1)

        return max_len

solution = Solution()
