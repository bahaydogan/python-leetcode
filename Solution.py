import math


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






if __name__ == '__main__':
    s = Solution()
    print(s.maximumUniqueSubarray([4, 2, 4, 5, 6]))
