# -*- coding: utf-8 -*-

class Solution:
    def two_sum(self, nums:list, target):
        hashtable = dict()
        for i,j in enumerate(nums):
            if target - j in hashtable:
                return [hashtable[target - j], i]
            else:
                hashtable[j] = i
        return []



if __name__ == '__main__':
    solution = Solution()
    retult1 = solution.two_sum([12,2,3,4,1,4,4,1],7)
    print(retult1)
    import jsonpath,os.path