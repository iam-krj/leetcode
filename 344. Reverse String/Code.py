class Solution:
    def reverseString(self, s: List[str]) -> None:
        front, end = 0, len(s) - 1
        while front < end:
            s[front], s[end] = s[end], s[front]
            front+=1
            end-=1
        return end