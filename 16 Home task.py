# Write a program that calculates and displays the letter grade for a given numerical score
# (e.g., A, B, C, D, or F) based on the following grading scale:
score = int(input("Enter the score \n"))
if score >= 90 and score <= 100:
    print("Grade is A")
if score >= 80 and score <= 89:
    print("Grade is B")
if score >= 70 and score <= 79:
    print("Grade is C")
if score >= 60 and score <= 69:
    print("Grade is D")
if score >= 0 and score <= 59:
    print("Grade is F")

# Leap year
Year = 2024
is leap year = False
if year % 4 == 0 and not year % 100 !==0 or year % 400 == 0
is_leap_year = True

print(f"{Year} is {is_leap year}")
