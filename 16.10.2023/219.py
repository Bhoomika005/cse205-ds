class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window=set()
        x=0
        
        for i in range(len(nums)):
            if i-x > k:
                window.remove(nums[x])
                x += 1
            if nums[i] in window:
                return True
            window.add(nums[i])
        return False