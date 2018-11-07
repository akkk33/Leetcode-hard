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
        pclose = len(s)

        odict = {}
        cdict = {}

        result = []
        if 0 <= s.find('(') < s.rfind(')'):
            s = s[s.find('('):s.rfind(')') + 1]
        else:
            s = ''
        for index, par in enumerate(s):
            if par == "(":
                odict[index] = par
            else:
                cdict[index] = par
        for index, par in odict.items():
            for num, val in cdict.items():
                if len(s[index:num]) % 2 == 0:
                    result.append(len(s[index:num]) + 2)
        return result


ex = Solution()
print(ex.longest_valid_parentheses("()"))
