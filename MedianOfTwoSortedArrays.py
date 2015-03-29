class Solution:
    # @return a float
    def findMedianSortedArrays(self, A, B):
        m = len(A)
        n = len(B)
        if m+n == 0:
            return 0
        i = 0
        j = 0
        c = []
        if (m+n)%2 == 1:
            if m == 0:
                return B[(m+n-1)/2]
            if n == 0:
                return A[(m+n-1)/2]
            for k in range(0,(m+n+1)/2):
                if j >= n:
                    c.append(A[i])
                    i += 1
                    continue
                if i >= m:
                    c.append(B[j])
                    j += 1
                    continue
                if A[i] <= B[j]:
                    c.append(A[i])
                    i += 1
                else:
                    c.append(B[j])
                    j += 1
            return c[(m+n-1)/2]
        else:
            if m == 0:
                return (B[(m+n)/2-1] + B[(m+n)/2])/2.
            if n == 0:
                return (A[(m+n)/2-1] + A[(m+n)/2])/2.
            for k in range(0,(m+n)/2+1):
                if j >= n:
                    c.append(A[i])
                    i += 1
                    continue
                if i >= m:
                    c.append(B[j])
                    j += 1
                    continue
                if A[i] <= B[j]:
                    c.append(A[i])
                    i += 1
                else:
                    c.append(B[j])
                    j += 1
            return (c[(m+n)/2-1] + c[(m+n)/2])/2.

testA = [1,3,5,7]
testB = [2,4,6]
sol = Solution()
print sol.findMedianSortedArrays([1], [1])
print sol.findMedianSortedArrays(testA, testB)