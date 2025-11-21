print("Welcome to my Python Program!")
savings = input("How much did you save this past month?" \
" (From the start of this month to today.)")
savings_goal = input("How much do you want to save this month?")
try:
    savings = float(savings)
    savings_goal = float(savings_goal)
except ValueError:
    print("Please enter a valid number.")
    exit()
percent_progress = savings / savings_goal * 100
print(f"You have saved {percent_progress}% of your monthly goal.")
