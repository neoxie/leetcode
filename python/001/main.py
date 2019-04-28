# https://leetcode-cn.com/problems/two-sum/
import datetime
import timeit


class Solution:
    def twoSum1(self, nums, target):
        for indexA in range(len(nums)):
            for indexB in range(indexA, len(nums)):
                if(nums[indexA] + nums[indexB] == target):
                    return [indexA, indexB]

    def twoSum2(self, nums, target):
        dic1 = dict()
        for id in range(len(nums)):
            number2 = target - nums[id]
            if number2 in dic1:
                return [dic1[number2], id]

            if nums[id] not in dic1:
                dic1[nums[id]] = id


def calc(nums, target, func):
    start = datetime.datetime.now()
    result = func(nums, target)
    print(result)
    difference = datetime.datetime.now() - start
    print('last: ', difference)


if __name__ == "__main__":
    nums = range(100001)

    target = 199999
    s = Solution()

    calc(nums, target, s.twoSum2)
    calc(nums, target, s.twoSum1)
