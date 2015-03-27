
import numpy as np
class Solution1:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        print A
        A = np.sort(A)
        print A
        print np.append(A[1::2],[A[len(A)-2]]), A[0::2]
        print np.append(A[1::2],[A[len(A)-2]]) - A[0::2]
        index = np.where((np.append(A[1::2],[A[len(A)-2]]) - A[0::2]) != 0)
        print index[0], (2*index[0])
        return A[(2*index[0])]

# can't use numpy, so do this:
class Solution:
    # @param A, a list of integer
    # @return an integer
    def singleNumber(self, A):
        dic = dict()
        for i in A:
            if i in dic:
                #dic[i] += 1
                del dic[i]
            else:
                dic[i] = 1
        if len(dic)>1:
            raise RuntimeError, "more than one single numbers"
        return dic.keys()[0]

test = [1,1,4,5,6,5,4]
sol = Solution()
print sol.singleNumber(test)
