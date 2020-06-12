#Given an array A of non-negative integers, 
# return an array consisting of all the even elements of A, 
# followed by all the odd elements of A.

#Input: [3,1,2,4]
# Output: [2,4,3,1]
# The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.



class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:
        
        odd_arr = []
        even_arr = []
        
        for i in range(len(A)):
            if A[i] % 2 != 0: #if A[i] is an odd number
                odd_arr.append(A[i])
            else:
                even_arr.append(A[i])
        result = even_arr + odd_arr
        return result
    
print(Solution)