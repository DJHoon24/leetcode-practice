# Link: https://leetcode.com/problems/flood-fill/

from typing import List

class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        queue = []
        visited = {}
        starting_colour = image[sr][sc]
        queue.append((sr,sc))
        visited[(sr, sc)] = 1

        while (len(queue) != 0):
            (curr_sr, curr_sc) = queue.pop(0)
            print((curr_sr, curr_sc))
            image[curr_sr][curr_sc] = color
            if (curr_sr > 0 and image[curr_sr - 1][curr_sc] == starting_colour and (curr_sr - 1, curr_sc) not in visited):
                queue.append((curr_sr - 1, curr_sc))
                visited[(curr_sr - 1, curr_sc)] = 1
            if (curr_sc > 0 and image[curr_sr][curr_sc - 1] == starting_colour and (curr_sr, curr_sc - 1) not in visited):
                queue.append((curr_sr, curr_sc - 1))
                visited[(curr_sr, curr_sc - 1)] = 1
            if (curr_sr + 1 < len(image) and image[curr_sr + 1][curr_sc] == starting_colour and (curr_sr + 1, curr_sc) not in visited):
                queue.append((curr_sr + 1, curr_sc))
                visited[(curr_sr + 1, curr_sc)] = 1
            if (curr_sc + 1 < len(image[0]) and image[curr_sr][curr_sc + 1] == starting_colour and (curr_sr, curr_sc + 1) not in visited):
                queue.append((curr_sr, curr_sc + 1))
                visited[(curr_sr, curr_sc + 1)] = 1
        
        return image