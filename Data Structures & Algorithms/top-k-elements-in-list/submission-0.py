class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        h = {}

        for num in nums :
            h[num] = h.get(num, 0) + 1
        
        bucketsL = [[] for _ in range(len(nums)+1)]
        
        for key in h :
            bucketsL[h[key]].append(key)
        
        returnedL = []

        for i in range(len(bucketsL)-1, -1, -1) :
            for num in bucketsL[i] :
                returnedL.append(num)
                k -= 1
                if k==0 :
                    return returnedL
        
        return None