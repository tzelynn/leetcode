# link https://leetcode.com/problems/decode-ways/description/

class Solution:
    def numDecodings(self, s: str) -> int:
        nums = [0] * len(s)
        for i in range(len(s)):
            count = 0
            if s[i] != "0":
                if i > 0:
                    count += nums[i-1]
                else:
                    count += 1
            if i > 0 and s[i-1] != "0" and s[i-1:i+1] <= "26":
                if i > 1:
                    count += nums[i-2]
                else:
                    count += 1
            nums[i] = count

        return nums[-1]
