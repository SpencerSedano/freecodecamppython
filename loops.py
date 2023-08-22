for i in [2,1,5]:
    print(i)

#getting the biggest number in an array

arr = [2,50,1,29,3,594,592,182]

big_num = 0
for num in arr:
    print(num)
    if num > big_num:
        big_num = num
print(f"The biggest number is: {big_num}")