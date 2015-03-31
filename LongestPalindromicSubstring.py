class Solution:
    def findPalindrome(self, s, i, j):
        """
        # input j-i = 1 or 0, find the longest Palindrome substring that
        # is symmetric about axis (i+j)/2
        """
        max_itr = min(len(s)-j, i+1)
        if max_itr == 0 or max_itr == 1:
            return i, j
        for k in range(max_itr):
            if s[i-k] == s[j+k]:
                continue
            else:
                return i-k+1, j+k-1
        return i-max_itr+1, j+max_itr-1

    # @return a string
    def longestPalindrome(self, s):
        sub_start = []
        sub_end = []
        sub_len = []
        if len(s) <= 1:
            return s
        for i, char in enumerate(s):
            if i>=1 and s[i-1] == char:
                _start, _end = self.findPalindrome(s,i-1,i)
                sub_start.append(int(_start))
                sub_end.append(int(_end))
                sub_len.append(int(_end)-int(_start))
            if i>=2 and s[i-2] == char:
                _start, _end = self.findPalindrome(s,i-1,i-1)
                sub_start.append(int(_start))
                sub_end.append(int(_end))
                sub_len.append(int(_end)-int(_start))

        max_len = max(sub_len)
        for i, length in enumerate(sub_len):
            if length == max_len:
                return s[int(sub_start[i]):int(sub_end[i])+1]


#test = "bfegabcdcbaffg"
test = 'aaabbbaaa'
#test = 'a'
#test = ''
#print test[3]
sol = Solution()
print sol.longestPalindrome(test)