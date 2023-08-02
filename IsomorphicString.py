class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return len(set(s))==len(set(t))==len(set(zip(s,t)))
if __name__=="__main__":
    s = "bar"
    t = "foo"
    solution = Solution()
    result = solution.isIsomorphic(s,t)
    print(result)
    
