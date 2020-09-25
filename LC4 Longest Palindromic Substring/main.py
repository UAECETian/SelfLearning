from pip._vendor.msgpack.fallback import xrange


class Solution:
    def longestPalindrome(self, s):
        temp = ""
        left = 0
        right = 0




        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= left
            right += right

