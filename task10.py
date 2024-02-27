num1 = int(input("1 num: "))
num2 = int(input("2 num: "))
num3 = int(input("3 num: "))
num4 = int(input("4 num: "))

min_num = num1

if num2 < min_num:
    min_num = num2
if num3 < min_num:
    min_num = num3
if num4 < min_num:
    min_num = num4

print("minimum number: ", min_num)