class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0
        # nums.sort() 因为快速排序的时间复杂度是O（nlogn）
        # 所以不能排序
        # 可以采用哈希表记录下来
        st = set(nums) # 导致有空间复杂度
        ans = 0
        for x in st: # 保证O(n)
            if x-1 in st: 
                # 有重复的
                continue
            y = x + 1
            while y in st:
                y += 1
            ans = max(ans, y-x)
        return ans
            
