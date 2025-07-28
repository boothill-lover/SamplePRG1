days = int(input('Enter number of days: '))
i = 1
print(f'Day | Task(s)')
for i in range(i, days + 1):
    if i % 7 != 0:
        print(f'{i:>3} |')

    else:
        print(f'{i:>3} |')
        print(f'Day | Task(s)')