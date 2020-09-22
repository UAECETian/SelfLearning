

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        blue = 0
        red = 0
        longest = 0
        newset = set()

        while blue < len(s):
            if s[blue] not in newset:
                newset.add(s[blue])
                blue = blue + 1
                # print(len(newset))
                if longest < len(newset):
                    longest = len(newset)
            else:
                newset.remove(s[red])
                red = red + 1

        return longest


temp = Solution();
val = temp.lengthOfLongestSubstring("pwwkew")
print(val)




