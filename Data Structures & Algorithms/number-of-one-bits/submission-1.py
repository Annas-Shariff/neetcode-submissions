class Solution:
    def hammingWeight(self, n: int) -> int:
        num_1=bin(n).count('1')
        return num_1
        
        