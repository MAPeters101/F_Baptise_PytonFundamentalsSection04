"""
Exercise 1
Given a variable a (containing any value), re-assign the value "N/A" if
a is None, and leave a unchanged otherwise. Use an if...else... statement.

We need to create a variable a assign it some value, and then test the value
of a to see if we need to change it to 'N/A':
"""
a = None
if a is None:
    a = 'N/A'

print(a)


"""
Exercise 2
Do the same thing as Question 1, but this time use a ternary operator.
"""
b = 100
b = "N/A" if b is None else b
print(b)


"""
Exercise 3
Given an credit score score, assign a string value to another variable rating 
based on the following scale:

[0, 580) --> Poor
[580, 670) --> Fair
[670, 740) --> Good
[740, 800) --> Very Good
[800, 850] --> Excellent
"""
score = 570
if score >= 800:
    rating = "Excellent"
elif score >= 740:
    rating = "Very Good"
elif score >= 670:
    rating = "Good"
elif score >= 580:
    rating = "Fair"
else:
    rating = "Poor"

print(rating)

"""
Exercise 4
Given an elapsed time (in seconds), write code to set a variable magnitude 
based on the following conditions:

if elapsed time is less than 1 minute, magnitude --> 'seconds'
if elapsed time is more than 1 minute, but less than 1 hour, magnitude --> 'minutes'
if elapsed time is more than 1 hour, but less than 1 day, magnitude --> 'hours'
if elapsed time is more than 1 day, but less than 1 week: magnitude --> 'days'
if elapsed time is more than 1 week, magnitude --> 'weeks'
"""
time = 60*60*24*7+10
if time < 60:
    magnitude = 'seconds'
elif time < 60*60:
    magnitude = 'minutes'
elif time < 60*60*24:
    magnitude = 'hours'
elif time < 60*60*24*7:
    magnitude = 'days'
else:
    magnitude = 'weeks'

print(magnitude)









