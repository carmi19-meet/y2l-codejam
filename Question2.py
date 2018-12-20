sum = 0
i = 0
while(i<1000):
    i+=1;
    sum += (i**i)
    print(i)
print(sum)
nums = []
for i in range(10):
	nums.append(int(sum % 10))
	sum = sum / 10
print("the last ten digits of the sum are:")
arr = nums[::-1]
for i in range(len(nums)):
	print(arr[i]),