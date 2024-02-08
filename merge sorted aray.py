nums1 = [0]
nums2 = [1]
m = 0
n = 1
for i in range(0, n):
    nums1[m + i] = nums2[i]

nums1.sort()
print(nums1)