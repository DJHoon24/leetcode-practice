# Link: https://leetcode.com/problems/number-of-ways-to-form-a-target-string-given-a-dictionary/

from typing import List

# O(n * m) time (n = length of words) (m = maxLength of dictionary word element)
class Solution:
    def numWays(self, words: List[str], target: str) -> int:
        max_word_length = len(words[0])
        target_length = len(target)
        character_count_array = [[0 for _ in range(26)] for _ in range(max_word_length)]
        characterOffset = 97
        for word in words: # PREPROCESS THE NUMBER OF COUNTS OF EACH OF THE CHARACTERS AT THE INDICES OF WORDS
            for i, char in enumerate(word):
                character_count_array[i][ord(char) - characterOffset] += 1
        from functools import lru_cache
        @lru_cache(maxsize=None)
        def dp(idx, substring_idx):
            if (substring_idx >= target_length):
                return 1
            if (idx == max_word_length):
                return 0
            total_dp = dp(idx + 1, substring_idx)
            target_char = target[substring_idx]
            characterCount = character_count_array[idx][ord(target_char) - characterOffset]
            total_dp += characterCount * dp(idx + 1, substring_idx + 1)
            return total_dp % 1000000007
        return dp(0, 0) 