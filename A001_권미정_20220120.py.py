"""
A001
g index 인원수
g >> 아이가 만족하는 쿠키사이즈
s = 쿠키사이즈
"""


class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        output = 0
        nextCookie = 0
        for j in range(0, len(s)):
            for i in range(nextCookie, len(g)):
                if s[j] >= g[i]:
                    output += 1
                    nextCookie = i+1
                    break

        return output
