class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        flag = 0 if n else 1
        while n:
            print(n)
            if n % 2 and n != 1:
                flag = 1
                break
            n = n // 2
        return False if flag else True

  # 将n看作二进制的解法(位运算）
  class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
      return n > 0 and n & (n - 1) == 0  # 
      
