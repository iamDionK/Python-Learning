# Python-Learning
# 1. Define your variables (The Data)
eth_price = 3800.50
wallet_balance = 2.5
gas_fee = 15.00

# 2. The Logic (The Math)
total_value = eth_price * wallet_balance
net_profit = total_value - gas_fee

# 3. The Output (What the user sees)
# We use an 'f-string' (f"...") to mix text and variables easily.
print(f"Current ETH Price: ${eth_price}")
print(f"My Portfolio Value: ${total_value}")
print(f"Value after Gas Fees: ${net_profit}")
initial_investment = 5000  # What you put in

# Calculate the profit
actual_profit = total_value - initial_investment

# Print it
print(f"Net Profit: ${actual_profit}")
