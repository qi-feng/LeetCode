class Solution:
    # @return an integer
    def lengthOfLongestSubstring(self, s):
        '''
        :param s: a string
        :return: integer of length fo longest substring with no repeating chars
        :internal variables:
        :dic: keys of dic are chars that are seen; values of dic are the indices of appearance of a seen char
        :len_sub: a list of length fo longest substring with no repeating chars * starting at i * where i is list index
        :cursor: marks the index of the input s after which no repeating chars have been read so far
        '''
        dic = dict()
        len_sub = []
        cursor = 0
        # WTF LeetCode???
        if not s:
            return 0
        for i, char in enumerate(s):
            #print i, char
            # if read a repeating character:
            #    (1) append 0 to len_sub
            #    (2) increment only len_sub values for [(dic[char]+1):]
            #    (3) shift cursor to dic[char]+1
            #    (4) treat the newly read repeating char as a fresh one that aren't seen before: dic[char] = i
            if char in dic.keys():
                print "repeat", char, i-dic[char]
                len_sub.append(0)
                if cursor<=dic[char]:
                    len_sub[(dic[char]+1):] = [x + 1 for x in len_sub[(dic[char]+1):]]
                    cursor = dic[char]+1
                else:
                    len_sub[(cursor):] = [x + 1 for x in len_sub[(cursor):]]

                dic[char] = i
                print len_sub
            # if read a non-repeating char:
            #    (1) append new len_sub of length 0
            #    (2) increment all len_sub after cursor (ones before cursor are cut by already seen repeating char)
            else:
                dic[char] = i
                len_sub.append(0)
                len_sub[cursor:] = [x + 1 for x in len_sub[cursor:]]
                print len_sub

        return max(len_sub)


test = 'xdgesxuuxuu'
test = "museuwzbczdejn"

sol = Solution()
print sol.lengthOfLongestSubstring(test)