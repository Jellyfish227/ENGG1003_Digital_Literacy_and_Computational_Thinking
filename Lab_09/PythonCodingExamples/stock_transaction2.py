stock_transactions = [
  ("14 Mar 2022", "HSBC", 2000, 49.61),
  ("14 Mar 2022", "A50", 400, 15.52),
  ("10 Mar 2022", "HSBC", 4000, 48.36)
]
print( stock_transactions )
amount = 0
for transaction in stock_transactions:
    print( transaction )
    amount += transaction[2] * transaction[3]
print( "Total transaction amount: HK$", amount)

