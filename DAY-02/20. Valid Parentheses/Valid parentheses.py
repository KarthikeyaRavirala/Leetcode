class Solution:
    def isValid(self, s: str) -> bool:
        a=[]
        b= {')': '(', '}': '{', ']': '['}

        for char in s:
            if char in b:
                if not a or a.pop() != b[char]:
                    return False
            else:
                a.append(char)
        return not a

def main():
    c=sol()
    inp=input()
    result=c.isValid(inp)
    print(result)
