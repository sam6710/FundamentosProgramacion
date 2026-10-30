num = int(input("Introduce un número entero: "))

if num%2 == 0:
    final = 2
else:
    final = 1

for i in range(final, num + 1, 2):
    print("" * ((num - i) * 2), end="")
    for j in range(i, 0, -2):
        print(j, end=" ")
    print()