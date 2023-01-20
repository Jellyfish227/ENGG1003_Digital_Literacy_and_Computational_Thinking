stock_transactions = [
  ("14 Mar 2022", "HSBC", 2000, 49.61),
  ("14 Mar 2022", "A50", 400, 15.52),
  ("10 Mar 2022", "HSBC", 4000, 48.36)
]
print( stock_transactions )
amount = stock_transactions[0][2] * stock_transactions[0][3] + \
	 stock_transactions[1][2] * stock_transactions[1][3] + \
	 stock_transactions[2][2] * stock_transactions[2][3]
print( "Total transaction amount: HK$", amount)

