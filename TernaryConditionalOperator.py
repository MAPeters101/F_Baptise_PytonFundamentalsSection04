from linecache import clearcache

ask_price = 100
if ask_price > 50:
    volume = 50
else:
    volume = 80
print(volume)


volume = 50 if ask_price > 50 else 80
print(volume)


a = 10
b = 20
distance = a-b if a>=b else b-a
print(distance)


current_value = 100
running_total = 150000
running_count = 125
if current_value == -999:
    clean_value = 0
else:
    clean_value = current_value
running_total = running_total + clean_value
print(running_total)

current_value = 100
running_total = 150000
running_count = 125
clean_value = 0 if current_value == -999 else current_value
running_total = running_total + clean_value
print(running_total)

current_value = 100
running_total = 150000
running_count = 125
running_total = running_total + 0 if current_value == -999 else current_value
print(running_total)

current_value = 100
running_total = 150000
running_count = 125
running_total = (running_total + 0) if current_value == -999 else current_value
print(running_total)

current_value = 100
running_total = 150000
running_count = 125
running_total = running_total + (0 if current_value == -999 else current_value)
print(running_total)

