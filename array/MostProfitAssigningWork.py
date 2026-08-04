class Solution:
    def maxProfitAssignment(self, difficulty: List[int], profit: List[int], worker: List[int]) -> int:
        jobs = list(zip(difficulty, profit))

        jobs.sort()
        worker.sort()

        i = 0
        maxProfit = 0
        totalProfit = 0

        for ability in worker:

            while i < len(jobs) and jobs[i][0] <= ability:
                maxProfit = max(maxProfit, jobs[i][1])
                i += 1

            totalProfit += maxProfit

        return totalProfit