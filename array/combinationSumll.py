class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
         # Sort so duplicates are next to each other
        candidates.sort()

        def backtrack(start, current, total):

            if total == target:
                result.append(current[:])
                return

            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicate numbers at the same recursion level
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                current.append(candidates[i])

                # i + 1 because each element can be used only once
                backtrack(i + 1, current, total + candidates[i])

                current.pop()

        backtrack(0, [], 0)

        return result


# Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

# Each number in candidates may only be used once in the combination.

# Note: The solution set must not contain duplicate combinations.