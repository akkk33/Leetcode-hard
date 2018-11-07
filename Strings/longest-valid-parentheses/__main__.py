"""
URL: https://leetcode.com/problems/longest-valid-parentheses/
Problem description:
Given a string containing just the characters '(' and ')', find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"
Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "()()"
#################3
The last example is weird, I couldn't understand it so I made an algorithm to count only valid parantheses like () or (()) .. etc
but It never

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
                if index != 0 and s[index - 1] != '(':
                    popen = 0
                popen += 1
            else:  # )
                pclose += 1
                result.append(min(pclose, popen) * 2)
        if len(result) > 0:
            return max(result)


ex = Solution()
print(ex.longest_valid_parentheses(")()())"))
