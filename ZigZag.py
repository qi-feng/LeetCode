class Solution:
    # @return a string
    def convert(self, s, nRows):
        N = len(s)
        res = []
        if nRows == 1:
            return s
        for i in range(nRows):
            for k in range(N/(2*(nRows-1))+1):
                if (i + 2*k*(nRows-1)) >= N:
                    break
                else:
                    res.append(s[i + 2*k*(nRows-1)])
                    if i % (nRows-1) != 0 and ((2*k+1)*(nRows-1) + nRows - 1 - i) < N:
                        res.append(s[(2*k+1)*(nRows-1) + nRows - 1 - i ])
        return ''.join(res)


test = '123456789xabc'
test = "PAYPALISHIRING"
#test = 'a'
#test = ''
#print test[3]
sol = Solution()
res = sol.convert(test,2)
print res
print type(res)
#print sol.convert("", 2)