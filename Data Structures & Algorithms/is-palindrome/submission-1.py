class Solution:
    def isPalindrome(self, s: str) -> bool:
        s=s.lower()
        s=''.join(each for each in s if each.isalnum())
        return s==s[::-1]