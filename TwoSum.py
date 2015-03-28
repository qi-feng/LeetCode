class Solution_tooSlow:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num = list(num)
        print num
        for i in range(0,len(num)):
            target2 = target - num[i]
            print "i", i, target2, num[i]
            for j in range(i,len(num)):
                print "j", j, num[j]
                if num[j] == target2:
                    return i+1, j+1

#now assume positive
class Solution:
    # @return a tuple, (index1, index2)
    def twoSum(self, num, target):
        num = list(num)
        target_dic = dict()
        for i in range(0,len(num)):
            target2 = target - num[i]
            if num[i] in target_dic.keys():
                return target_dic[num[i]]+1, i+1
            else:
                target_dic[target2]=i



test = {2, 7, 11, 15}
#test = {-20, -30, 5, 90, 3, 2}
#print test.items()
target= 9
sol = Solution()
print sol.twoSum(test, target)