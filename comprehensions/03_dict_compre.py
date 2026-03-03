# {expression for item in iterable if condition}
# expression = {key : value}


tea_prices_inr =  {
    "Masala chai": 40 , 
    "Green tea" : 50 , 
    "Lemon Tea" : 200 
}

# inr/100 = usd 
tea_prices_usd = { tea:price / 100 for tea, price in tea_prices_inr.items()  }

print(tea_prices_usd)
