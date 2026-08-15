class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        m = len(flowerbed)
        i = 0
        if m == 1:
            if flowerbed[i] == 0:
                n-=1
            return n<=0
                
        while i < m:
            if i-1 < 0:
                if flowerbed[i+1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n-=1
            elif i+1 >= m:
                if flowerbed[i-1] == 0 and flowerbed[i] == 0:
                    flowerbed[i] = 1
                    n-=1
            elif flowerbed[i-1] == 0 and flowerbed[i+1] == 0 and flowerbed[i] == 0:
                flowerbed[i] = 1
                n-=1
            i+=1

        if n <=0:
            return(True)
        else:
            return(False)