import math
from email.charset import add_alias


class Solution(object):
    def removeSubfolders(self, folder):
        """
        :type folder: List[str]
        :rtype: List[str]
        """

        folder.sort()
        result = []
        prev = None

        for f in folder:
            if prev is None or not f.startswith(prev + "/"):
                result.append(f)
                prev = f

        return result

    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        s = list(s)
        for i in range(0, len(s), 2 * k):
            s[i:i + k] = reversed(s[i:i + k])
        return ''.join(s)

    def makeFancyString(self, s):
        """
        :type s: str
        :rtype: str
        """
        result = []
        count = 0
        prev_char = None

        # leeetcode

        for char in s:
            if char == prev_char:
                count += 1
            else:
                count = 1
                prev_char = char

            if count < 3:
                result.append(char)

        return ''.join(result)

    def maximumUniqueSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        seen = set()
        left = 0
        max_sum = -1
        current_sum = 0

        for right in range(len(nums)):
            while nums[right] in seen:
                seen.remove(nums[left])
                current_sum -= nums[left]
                left += 1

            seen.add(nums[right])
            current_sum += nums[right]
            max_sum = max(max_sum, current_sum)

        return max_sum

    #1717
    def maximumGain(self, s, x, y):
        """
        :type s: str
        :type x: int
        :type y: int
        :rtype: int
        """
        def remove_pairs(s, first, second, points):
            stack = []
            score = 0

            for char in s:
                if stack and stack[-1] == first and char == second:
                    stack.pop()
                    score += points
                else:
                    stack.append(char)

            return ''.join(stack), score

        if x >= y:
            s, score1 = remove_pairs(s, 'a', 'b', x)
            s, score2 = remove_pairs(s, 'b', 'a', y)
        else:
            s, score1 = remove_pairs(s, 'b', 'a', y)
            s, score2 = remove_pairs(s, 'a', 'b', x)

        return score1 + score2

    #1647
    def minDeletions(self, s):
        """
        :type s: str
        :rtype: int
        """
        from collections import Counter

        freq = Counter(s)
        freq_values = list(freq.values())
        freq_values.sort(reverse=True)

        deletions = 0
        seen = set()
                # aaa bbb cc
        for f in freq_values:
            while f > 0 and f in seen:
                f -= 1
                deletions += 1
            seen.add(f)

        return deletions




if __name__ == '__main__':
    s = Solution()
    print(s.minDeletions('aaabbbcc'))
