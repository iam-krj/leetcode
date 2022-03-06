class Solution:
    def cellsInRange(self, s: str) -> List[str]:
        output = []
        for new in range(ord(s[0]), ord(s[3])+1):
            op =""
            for old in range(int(s[1]), int(s[4])+1):
                op = chr(new) +str(old)
                output.append(op)
        return output
        
        