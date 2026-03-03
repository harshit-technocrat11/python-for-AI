# generator : ( expr for item in iterable if condition)

# [x for x in items] - makes the entire list in memory 
#  (x for x in items) - streaming one by one

daily_sales =[5, 10 , 12, 7 , 3, 8 , 9 , 15]

# /streaming
total_cups = ( sale for sale in daily_sales if sale > 5)

print(total_cups)
# <generator object <genexpr> at 0x0000023B9C14B440>

# for i in total_cups:
#     print(i)

# carrying out operations
total_cups = sum ( sale for sale in total_cups if sale> 5)
print(total_cups)