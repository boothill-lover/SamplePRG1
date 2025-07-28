continuegame = 1
numberlistE = []
numberlistO = []
total = 0

while continuegame==1:
    number = int(input('Please enter a number (0 to end): '))
    if number == 0:
        break

    else:
        total = total + number
        if number % 2 == 0:
            numberlistE.append(number)
        else:
            numberlistO.append(number)

print(f'Odd Numbers: {sorted(numberlistO)}')
print(f'Even Numbers: {sorted(numberlistE)}')
print(f'{total / (len(numberlistE) + len(numberlistO)):.2f}')