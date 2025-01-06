class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target in nums:
            return nums.index(target)
        else:
            if len(nums) == 0:
                return 0
            elif target > nums[len(nums)-1]:
                return len(nums)
            else:
                for i in range(len(nums)):
                    try:
                        if (target > nums[i-1]) and (target < nums[i]):
                            return i
                    except IndexError:
                        if i == 0:
                            if target < nums[i]:
                                return 0
                            elif len(nums) == 1:
                                return 1
        return 0
