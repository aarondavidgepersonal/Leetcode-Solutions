class Solution:
    
    def isPalindrome(self, x: int) -> bool:
        
        pali = str(x)[::-1]
        
        if(x == int(pali)):
            return True
        else:
            return False
        