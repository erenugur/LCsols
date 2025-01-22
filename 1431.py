class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        retList = []
        for i in range(len(candies)):
            boolVal = True
            for j in range(len(candies)):
                if not ((candies[i] + extraCandies) >= candies[j]):
                    boolVal = False
            retList.append(boolVal)
        return retList

                    

        
