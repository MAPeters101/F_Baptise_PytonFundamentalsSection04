grade = 72
if grade >= 90:
    print("Passed with distinction")
else:
    if grade >= 70:
        print("Passed")
    else:
        print("Failed")

grade = 72
if grade >= 90:
    print("Passed with distinction")
elif grade >= 70:
    print("Passed")
else:
    print("Failed")

grade = 72
if grade >= 90:
    grade_letter = 'A'
elif grade >= 80:
    grade_letter = 'B'
elif grade >= 70:
    grade_letter = 'C'
elif grade >= 60:
    grade_letter = 'D'
else:
    grade_letter = 'F'
print(grade_letter)


account_enabled = True
balance = 1000
withdraw = 100_000
if account_enabled and withdraw <= balance:
    print('authorized')
else:
    if not account_enabled:
        print('account disabled')
    else:
        print("insufficient funds")


account_enabled = True
balance = 1000
withdraw = 100_000
if not account_enabled:
    print('account disabled')
else:
    if withdraw > balance:
        print("insufficient funds")
    else:
        print('withdrawal authorized')

account_enabled = True
balance = 1000
withdraw = 100_000
if not account_enabled:
    print('account disabled')
elif withdraw > balance:
    print("insufficient funds")
else:
    print('withdrawal authorized')


