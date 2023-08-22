for i in [2,1,5]:
    print(i)

#Finding the biggest number in an array

arr = [2,50,1,29,3,594,592,182]

big_num = 0
for num in arr:
    print(num)
    if num > big_num:
        big_num = num
print(f"The biggest number is: {big_num}")


#Finding the smallest number in an array

arr = [2,50,1,29,3,594,592,182]

small_num = 100
for num in arr:
    print(num)
    if num < small_num:
        small_num = num
print(f"The smallest number is: {small_num}")