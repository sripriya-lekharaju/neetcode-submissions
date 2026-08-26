class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen = set() #hashset
        for num in nums: #iterating through the list
            if num in seen: #check if the num is the set
                return True #return true 
            seen.add(num) #and add the num to the set
        return False #if it has no duplicates
        