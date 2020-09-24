

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # blue = 0
        # red = 0
        # longest = 0
        # newset = set()
        #
        # while blue < len(s):
        #     if s[blue] not in newset:
        #         newset.add(s[blue])
        #         blue = blue + 1
        #         # print(len(newset))
        #         if longest < len(newset):
        #             longest = len(newset)
        #     else:
        #         newset.remove(s[red])
        #         red = red + 1
        #
        # return longest

        used = {}
        max_length = start = 0
        for i, c in enumerate(s):

            if c in used and start <= used[c]:
                start = used[c] + 1
            else:
                max_length = max(max_length, i - start + 1)

            used[c] = i

        return max_length


temp = Solution();
val = temp.lengthOfLongestSubstring("abcabcabc")
print(val)




