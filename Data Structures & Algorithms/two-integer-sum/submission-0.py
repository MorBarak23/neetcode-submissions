class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}
        
        for i in range(len(nums)):
            h[nums[i]] = i
            
        for i in range(len(nums)):
            current = target - nums[i]
            
            if current in h and h[current] != i:
                return [i, h[current]]
                
        return []
