# link: https://leetcode.com/problems/insert-interval/

class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        if not intervals:
            return [newInterval]

        new_start, new_end = newInterval
        new_intervals = []
        met = False
        done = False
        for intv in intervals:
            start, end = intv
            if new_start > end or done:
                new_intervals.append(intv)
                continue
            if not met:
                if new_start < start and new_end < start:
                    new_intervals.append(newInterval)
                    new_intervals.append(intv)
                    done = True
                else:
                    new_start = min(start, new_start)
                    new_end = max(end, new_end)
                met = True
            else:
                if new_end < start:
                    new_intervals.append([new_start, new_end])
                    new_intervals.append(intv)
                    done = True
                else:
                    new_end = max(end, new_end)
        
        if not done:
            new_intervals.append([new_start, new_end])
        
        return new_intervals
