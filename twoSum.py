
def twoSum(nums, target):
    a = nums
    b = target
    c = len(a)
    m = c-1
    ans = []
    
    for i in range(m):
        if i < m :   
            for x in range(i+1,m+1):
                if a[i] + a[x] == b:
                    ans.append(i)
                    ans.append(x)
                    return ans
                break


nums1 = [2,7,11,15]
target1 = 9
print(twoSum(nums1,target1))
