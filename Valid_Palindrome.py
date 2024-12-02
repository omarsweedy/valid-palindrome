class Solution:
    def isPalindrome(self, s: str) -> bool:
        L=0
        R=len(s)-1
        while L<R:
            while L<R and not self.isalpha(s[L]):
                L+=1
            while R>L and not self.isalpha(s[R]):
               R-=1
            if s[L].lower()!=s[R].lower():
               return False
            L,R=L+1,R-1
        return True       

    def isalpha(self,c):
       return  (ord("A")<=ord(c)<=ord("Z")or
               ord("a")<=ord(c)<=ord("z")or
               ord("0")<=ord(c)<=ord("9"))





sol=Solution()
print(sol.isPalindrome("Was it a car or a cat I saw?"))        