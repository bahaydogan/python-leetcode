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






if __name__ == '__main__':
    s = Solution()
    print(s.reverseStr("abcdefg", 2))
