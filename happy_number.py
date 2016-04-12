class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n==0:
            return True
        if n<0:
            n = -n
        new_n = n
        n_iter = 0
        history_dict=set()
        history_dict.add(new_n)
        while new_n > 1:
            #print("iteration # %d the number is %d" % (n_iter, new_n))
            new_n = self.digits_sum_square(new_n)
            if (new_n in history_dict) and (new_n != 1):
                #print "Unhappy"
                return False
            history_dict.add(new_n)
            n_iter += 1
            if n_iter>100:
                break
        if new_n==1:
            #print "Happy"
            return True
        else:
            #print "Unhappy"
            return False

    def get_digits(self, n):
        digits = []
        while n >= 1:
            digits.append(n%10)
            n = n/10
        return digits

    def digits_sum_square(self, n):
        answer = 0
        for digit in self.get_digits(n):
            answer += digit*digit
        return answer

sol = Solution()
for n in range(100):
    #print sol.get_digits(n), sol.digits_sum_square(n), sol.isHappy(n)
    print n, sol.isHappy(n)



