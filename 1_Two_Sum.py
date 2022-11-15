from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        tamanhoList = len(nums)

        for i in range(tamanhoList):
            for j in range(i+1, tamanhoList):
                
                if (nums[i] + nums[j]) == target:
                    return [i, j]

            



if __name__ == "__main__":  
    s = Solution()
    r = s.twoSum([3,3], 6)
    print(r)