def collatz(num):
    print(num)
    if num % 2 == 0:
        return num //2
    else:
        return 3 * num + 1

print("Enter number:")
try:
    num = int(input())
    while num != 1:
        num = collatz(num)
    print(num)
except ValueError:
    print('Please enter an integer value')
