class Solution:
    def isHappy(self, n: int) -> bool:
        seen_numbers = []  # Tracks previous sums to prevent infinite loops
        
        while n != 1 and n not in seen_numbers:
            seen_numbers.append(n)
            
            s = str(n)
            l = []
            
            # Step 1: Separate digits into a list
            for i in s:
                l.append(int(i))
                
            # Step 2: Square each digit by transforming the list elements
            for i in range(len(l)):
                l[i] = l[i] ** 2
                
            # Step 3: Update n with the new sum for the next loop iteration
            n = sum(l)
            
        if n == 1:
            return True
        return False
