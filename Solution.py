import collections
from typing import List


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

    #3487
    def maxSum(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if max(nums) < 0:
            return max(nums)

        nums_set = set(nums)

        print(nums_set)
        return_list = []
        #nums = [1,1,0,1,1]
        for num in nums_set:
            print("num: "  + str(num))
            if num >= 0:
                return_list.append(num)
        return sum(return_list)

    #2210
    def countHillValley(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        #nums =[6,6,5,5,4,1]
        count = 0
        n = len(nums)
        for i in range(1, n - 1):
            current = nums[i]
            print("current : " + str(current))
            prev = nums[i - 1]
            nextt = nums[i + 1]

            if current == nextt:
                print("burdayız")
                continue


            while prev == current and prev != nums[0]:
                i -= 1
                prev = nums[i - 1]
                print("new prev: " + str(prev))

            while nextt == current and nextt != nums[-1]:
                i += 1
                nextt = nums[i + 1]
                print("new next: " + str(nextt))
            #nums =[6,6,5,5,4,1]



            if current > prev and current > nextt:
                count += 1
                print("bastık: " + str(current))
            elif current < prev and current < nextt:
                count += 1
                print("bastık: " + str(current))



        return count

    #leetcode 2044, totally ai solution:
    def countMaxOrSubsets(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_or = 0
        count = 0

        def backtrack(index, current_or):
            nonlocal max_or, count
            if index == len(nums):
                if current_or > max_or:
                    max_or = current_or
                    count = 1
                elif current_or == max_or:
                    count += 1
                return

            # Include the current number
            backtrack(index + 1, current_or | nums[index])
            # Exclude the current number
            backtrack(index + 1, current_or)

        backtrack(0, 0)
        return count

    def countMaxOrSubsets2(self, nums: List[int]) -> int:
        dp = collections.Counter([0])
        print(f"Initial dp: {dp}")
        max_or = 0
        print(f"Initial max_or: {max_or}")

        for i, num in enumerate(nums):
            print(f"\n--- Processing num: {num} (Index: {i}) ---")
            # Create a list of items to iterate over to avoid "dictionary changed size during iteration" error
            # as we are modifying dp inside the loop
            current_dp_items = list(dp.items())
            print(f"Current dp items before inner loop: {current_dp_items}")

            for val, count in current_dp_items:
                new_or_val = val | num
                dp[new_or_val] += count
                print(f"  Processing (val={val}, count={count}): val | num = {val} | {num} = {new_or_val}")
                print(f"  Updated dp: {dp}")

            max_or |= num
            print(f"After processing num {num}, max_or is now: {max_or}")
            print(f"DP state after processing num {num}: {dp}")

        print(f"\n--- Final State ---")
        print(f"Final max_or: {max_or}")
        print(f"Final dp: {dp}")

        result = dp[max_or]
        print(f"Result (dp[max_or]): {result}")
        return result

    #1295
    def findNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        for num in nums:
            if len(str(num)) % 2 == 0:
                count += 1
        return count

if __name__ == '__main__':
    s = Solution()
    nums = [555,901,482,1771]
    print("nums: " +str(nums))
    print(s.findNumbers(nums))