a = int(input('2-e number: '))
if a % 10 == a // 10:
    print('YES')
elif a // 100 != 0:
    print('THATS NOT 2-E NUMBER!')
else:
    print("NO")
