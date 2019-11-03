#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov  3 07:53:42 2019

@author: bijayamanandhar
"""

class Solution(object):
    def twoSum(self, nums, target):
        '''
        :type nums: List[int]
        :type target: int
        rtype: List[int]
        '''
        result = [None] * 2
        
        for i in range(len(nums) -1):
            for j in range(i +1, len(nums)):
                if nums[i] +nums[j] == target:
                    result[0], result[1] = nums[i], nums[j]
        return result
        
    
if __name__ == '__main__':
    nums = [2, 1, 3, -2, 6, 7]
    s = Solution()
    result = s.twoSum(nums, 7)
    print(result)