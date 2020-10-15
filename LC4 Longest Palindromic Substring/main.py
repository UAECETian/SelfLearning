from pip._vendor.msgpack.fallback import xrange


class Solution:
    def longestPalindrome(self, s):
        temp = ""
        left = 0
        right = 0

        for i in xrange(len(s)):
            res = self.getthestr(s, i, i)
            if len(res) > len(temp):
                temp = res
            res = self.getthestr(s, i, i+1)
            if len(res) > len(temp):
                temp = res
        return temp



    def getthestr(self,s,l,r):
        while l >= 0 and r < len(s) and s[l] == s[r]:
            l = l - 1
            r = r + 1
        return s[l+1:r]

tmp = Solution()
print(tmp.longestPalindrome('aabaa'))