"""
References

"""


class Solution:
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        result = []
        if 0 <= s.find('(') < s.rfind(')'):
            s = s[s.find('('):s.rfind(')') + 1]
        else:
            s = ''
        for index, letter in enumerate(s):
            if letter == ')':
                if s[index - 1] == '(':
                    result.append(2)
        return sum(result)


ex = Solution()
print(ex.longestValidParentheses(")("))
