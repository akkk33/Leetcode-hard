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

"""
class Solution:
    def longest_valid_parentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0 or len(s) == 1:
            return 0
        elif len(s) == 2:
            if s == "()":
                return 2
            else:
                return 0
        count = []
        popen = []
        pclose = []
        for index, letter in enumerate(s):
            if letter == "(":
                popen.append(index)
            else:
                pclose.append(index)
        if len(popen) == 0 or len(pclose) == 0:
            return 0
        for opening in popen:
            for closing in reversed(pclose):
                entire = len(s[opening:closing])
                if entire == 0:
                    count.append(2)
                elif entire % 2 == 0:
                    count.append(entire)
        return max(count)


ex = Solution()
print(ex.longest_valid_parentheses("()()"))
