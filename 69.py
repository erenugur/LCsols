class Solution:
    def mySqrt(self, x: int) -> int:
        if (x == 0) or (x == 1):
            return x
        else:
            low = 1
            high = x
            mid = 0
            midSquare = 0

            while low <= high:
                mid = (high + low) // 2
                midSquare = mid * mid

                if midSquare < x:
                    low = mid + 1
                elif midSquare > x:
                    high = mid - 1
                else:
                    return mid
        
        return high
                
                
