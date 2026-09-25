# mortgage.py
#
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
month = 0

extra_payment_start_month = int(input('Enter the month to start extra payment: '))
extra_payment_end_month = int(input('Enter the month to end extra payment: '))
extra_payment = int(input('Enter the extra payment amount: $'))    
    
while principal > 0:
    month += 1
    
    if extra_payment_start_month <= month <= extra_payment_end_month:
        current_payment = payment + extra_payment
    else:
        current_payment = payment
    
    principal = principal * (1 + rate/12)

    if current_payment > principal:
        current_payment = principal
        
    principal -= current_payment
    total_paid += current_payment
    
    print(month, round(total_paid, 2), round(principal, 2))


print('Months:', month, ',Total paid: $', total_paid)
