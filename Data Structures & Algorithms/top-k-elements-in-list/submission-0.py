class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        #consider this input set - nums=[5,5,5,1,1,8,8,8,8], k=2
        freq = Counter(nums) #counts the number and the frequency
        freq.items()  #converts to key value pairs (number, frequency) [(5,3), (1,2), (8,4)]
        sorted_items = sorted(freq.items(),
        key= lambda x:x[1], #we are sorting using the frequency
        reverse = True) #descending 4,3,2 [(8,4),(5,3), (1,2)]
        return [num for num, count in sorted_items[:k]]