import numpy as np
def calculator(home_price, d, r, t):
  p=home_price-d
  months=12
  rate=r/100
  rateByMonthsInYear=rate/months
  try:
    monthly_payment=(p*rateByMonthsInYear)/(1-((1+rateByMonthsInYear)**(-months*t)))
    return monthly_payment
  except OverflowError as e:
        print("it's an overflow error, please check")
home_price=int(input("input the whole home price: "))
down_payment=int(input("input the down_payment: "))
rate=int(input("input the rate: "))
total=int(input("input the total amount of years: "))
print(calculator(home_price, down_payment, rate, total))
