import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        h = collections.defaultdict(list)
        
        for st in strs:
            sorted_key = "".join(sorted(st))
            
            h[sorted_key].append(st)
            
        return list(h.values())