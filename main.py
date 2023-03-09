import string

def twoSum(nums:[int], target:int) :
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

line = input().split()

lst = list(map(int, line[2][1:-2].split(sep=",")))
tar = int(line[5])

a = twoSum(lst, tar)
print("[", a[0], ", ", a[1], "]", sep="")
