class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType) // 2

        different_candy = []
        candy_count = 0

        for candy in candyType:
            if candy not in different_candy:
                
                candy_count +=1
                if candy_count == n:
                    break
                different_candy.append(candy)

        
        return(candy_count)

        