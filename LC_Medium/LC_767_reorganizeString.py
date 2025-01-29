# LINK https://leetcode.com/problems/reorganize-string/

from collections import Counter
import heapq
class Solution:
    def reorganizeString(self, s: str) -> str:
        counts = Counter(s)
        
        heap = [(-count, char) for char, count in counts.items()]

        heapq.heapify(heap)
        answer = []
        
        # Go from highest frequency character to least frequent but make sure character that was added is not added unless a new character has been appeneded.
        previous_count, previous_char = 0, ''
        while heap:
            count, char = heapq.heappop(heap)
            answer += [char]

            if previous_count < 0:
                heapq.heappush(heap, (previous_count, previous_char))
            
            count += 1
            previous_count, previous_char = count, char
        
        response = ''.join(answer)

        if len(response) != len(s):
            return ""

        return response
