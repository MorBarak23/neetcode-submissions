class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        countPerf = {}

        for ch in s:
            if ch in countPerf:
                countPerf[ch] += 1
            else:
                countPerf[ch] = 1
        
        for ch in t:
            if ch not in countPerf:
                return False
            
            countPerf[ch] -=1

            if countPerf[ch] == 0:
                del countPerf[ch]

        
        return True
        