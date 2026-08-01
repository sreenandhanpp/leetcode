class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        n = len(firstList)
        m = len(secondList)
        res = []
        final = []
        i,j = 0,0
        while i < n and j < m:
            a = firstList[i]
            b = secondList[j]
            
            if a[0] <= b[0] and b[0] <= a[1]:
                res.append(b[0])
            elif a[0]>b[0] and a[0] <= b[1]:
                res.append(a[0])
                
            if a[1] <= b[1] and a[1] >= b[0]:
                res.append(a[1])
            elif a[1] > b[1] and b[1]>=a[0]:
                res.append(b[1])
                
            if res:
                final.append(res[:])
                res.clear()
            if a[1] > b[1]:
                j+=1
            else:
                i +=1
            
        return(final)
        

# class Solution:
#     def intervalIntersection(self, firstList, secondList):

#         i = 0
#         j = 0

#         ans = []

#         while i < len(firstList) and j < len(secondList):

#             start = max(firstList[i][0], secondList[j][0])
#             end = min(firstList[i][1], secondList[j][1])

#             if start <= end:
#                 ans.append([start, end])

#             if firstList[i][1] < secondList[j][1]:
#                 i += 1
#             else:
#                 j += 1

#         return ans