
def twoSum(nums: [int], target: int) -> [int] :
    lst_ans = []
    l = len(nums)

    for i, val in enumerate(nums) :
        if len(lst_ans) > 0 :
            break
        for j in range(i+1, l) :
            if val+nums[j] == target :
                lst_ans.append(i)
                lst_ans.append(j)
                break
            
    return lst_ans

