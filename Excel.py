class Solution(object):
    def convertToTitle(self, n):
        """
        :type n: int
        :rtype: str
        """
        tuple1 = ('A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z')
        result = ''
        while n > 0:
            get = (n-1) % 26
            result = tuple1[get] +  result
            n = (n-1) // 26
        return result




s = Solution()
print(s.convertToTitle(79))
