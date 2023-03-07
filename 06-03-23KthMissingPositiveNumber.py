#1539. Kth Missing Positive Number
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        beg, end = 0, len(arr)
        while beg < end:
            mid = (beg + end) // 2
            if arr[mid] - mid - 1 < k:
                #arr[mid] - mid - 1 represents no. of elements skipped!
                beg = mid + 1
            else:
                end = mid
        return end + k
