# Link: https://leetcode.com/problems/optimal-partition-of-string/

class Solution:
    def partitionString(self, s: str) -> int:
        char_dict = {}
        substrings_count = 1
        for char in s:
            if (char not in char_dict):
                char_dict[char] = 1
            else:
                char_dict = {}
                char_dict[char] = 1
                substrings_count += 1
        return substrings_count
