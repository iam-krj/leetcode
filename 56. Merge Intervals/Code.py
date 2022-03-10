class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals = sorted(intervals, key = lambda x : x[0])
        res = []
        curr = intervals[0]
        for interval in intervals:
            if interval[0]<= curr[1]:
                if interval[1] > curr[1]:
                    curr[1] = interval[1]
            else:
                res.append(curr)
                curr = interval
        res.append(curr)
        return res
        