deposit = float(input())
deposit_duration = int(input())
annual_interest = float(input())
amount = deposit + deposit_duration * ((deposit * annual_interest) / 12)
print(amount)
