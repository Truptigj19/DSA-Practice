class Solution:
    def isSorted(self, arr) -> bool:
        out = True
        for i in range(0,len(arr)-1):
            if arr[i]<arr[i+1] or arr[i]==arr[i+1]:
                continue
            else:
                out = False
        return out