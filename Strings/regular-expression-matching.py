"""
URL: https://leetcode.com/problems/regular-expression-matching/

Description:
Given an input string (s) and a pattern (p), implement regular expression matching with support for '.' and '*'.

'.' Matches any single character.
'*' Matches zero or more of the preceding element.
The matching should cover the entire input string (not partial).

Note:

s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like . or *.
Example 1:

Input:
s = "aa"
p = "a"
Output: false
Explanation: "a" does not match the entire string "aa".
Example 2:

Input:
s = "aa"
p = "a*"
Output: true
Explanation: '*' means zero or more of the precedeng element, 'a'. Therefore, by repeating 'a' once, it becomes "aa".
Example 3:

Input:
s = "ab"
p = ".*"
Output: true
Explanation: ".*" means "zero or more (*) of any character (.)".
Example 4:

Input:
s = "aab"
p = "c*a*b"
Output: true
Explanation: c can be repeated 0 times, a can be repeated 1 time. Therefore it matches "aab".
Example 5:

Input:
s = "mississippi"
p = "mis*is*p*."
Output: false
"""

import re


class Solution:
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        if re.compile('^'+p+'$').match(s):
            return True
        return False


attempt = Solution()
print(attempt.isMatch('aa', 'a'))  # False
print(attempt.isMatch('aa', 'a*'))  # True
print(attempt.isMatch('ab', '.*'))  # True
print(attempt.isMatch('aab', 'c*a*b'))  # True
print(attempt.isMatch('mississippi', 'mis*is*p*.'))  # False

"""
First attempt finished successfully with Runtime: 120 ms, faster than 23.26% of Python3 online submissions for Regular Expression Matching.
However I'm going to work on giving more performance

Second attempt resulted in increasing speed by only 3% with overall 26% !! Seeking new approach.

Third attempt: Runtime: 96 ms, faster than 31.70% of Python3 online submissions for Regular Expression Matching.

Fourth attempt: Runtime: 80 ms, faster than 45.93% of Python3 online submissions for Regular Expression Matching.

"""
