list = int(raw_input())
nums = [2,3,4,5,6]
nums.sort()
length = len(nums)
if (length % 2 == 0):
    median = (nums[(length)//2] + nums[(length)//2-1]) / 2
else:
    median = nums[(length-1)//2]
print(median)
