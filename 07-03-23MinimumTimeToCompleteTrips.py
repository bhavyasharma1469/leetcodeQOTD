#2187. Minimum Time to Complete Trips

class Solution:
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        l = 0
        r = 10 ** 14
        ans = r
        while l <r:
            mid = (l + r) // 2
            count = 0
            for ele in time:
                count += mid // ele
            if count >= totalTrips:
                ans = min(ans, mid)
                r = mid
            else:
                l = mid + 1
        return ans  
