# Exercise#1
# cashier
num=(int(input("integer money")))
money=num
while num<1 or num>1000:
 print ("please write another number")
 num=(int(input("integer money")))


count_10 = 0
count_5 = 0
count_1 = 0


if money >= 10:
    count_10 = money // 10
    money %= 10
if money >= 5:
    count_5 = money // 5
    money %= 5
count_1 = money

# Calculate the total minimum number of coins required
min_coins = count_10 + count_5 + count_1

# Print the result


print("Minimum number of coins:", min_coins)
print("Number of 10 coins:", count_10*" 10 +")
print("Number of 5 coins:", count_5*" 5 + ")
print("Number of 1 coins:", count_1*" 1 + ")


 
