class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
      '''
      时间复杂度：O(n)
      空间复杂度：O(1)
      '''
        if not nums:
            return 0
        nums.sort()
        res = 1
        maxlen = 1
        for i in range(1, len(nums)):
            if nums[i] - 1 == nums[i-1]:
                res += 1
            elif nums[i] - 1 > nums[i-1]:
                res = 1
                
            maxlen = max(maxlen, res)
        
        return maxlen
            
