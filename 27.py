class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        removeAmt = 0
        for i in range(len(nums)):
            if nums[i] == val:
                removeAmt += 1
        for i in range(removeAmt):
            nums.remove(val)
