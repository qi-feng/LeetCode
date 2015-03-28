class Solution:
    # @return a boolean
    def isPalindrome(self, x):
        list = []
        #x = abs(x)
        if x<0:
            is_Palindrome = False
        else:
            is_Palindrome = True
        while x/10 >= 1:
            list.append(x%10)
            x = x/10
        list.append(x%10)

        for digit in range(0, len(list)/2+1):
            if list[digit] == list[-1-digit]:
                continue
            else:
                is_Palindrome = False
                break
        return is_Palindrome

sol = Solution()
#test = 1234321
#test = 2112
test = -2147483648
print sol.isPalindrome(test)