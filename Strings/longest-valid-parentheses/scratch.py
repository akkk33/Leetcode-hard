"""
References

"""


class Solution:
    def longest_valid_parentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        popen = 0
        pclose = 0
        result = []
        if 0 <= s.find('(') < s.rfind(')'):
            s = s[s.find('('):s.rfind(')') + 1]
        else:
            s = ''
        for index, letter in enumerate(s):
            if letter == '(':
                if index != 0 and s[index - 1] != '(' and s[index-2] != '(':
                    popen = 0
                popen += 1
            else:  # )
                if s[index - 1] != ')' and s[index - 2] != ')':
                    pclose = 0
                pclose += 1
                result.append(min(pclose, popen) * 2)
        if len(result) > 0:
            return max(result)
        else:
            return 0


ex = Solution()
print(ex.longest_valid_parentheses("()(())"))
