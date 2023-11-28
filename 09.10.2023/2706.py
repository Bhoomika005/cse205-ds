class Solution:
    def buyChoco(self, prices: List[int], money: int) -> int:
        min1=float("inf")
        min2=float("inf")

        for price in prices:
            if price < min1:
                min2=min1
                min1=price
            elif price < min2:
                min2=price
            
        remaining= money-min1-min2

        if remaining < 0:
            return money
        
        return remaining