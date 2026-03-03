#  list
#  [ expression for item in iteratable if condition ]

menu = [
    "masala chai ",
     "iced lemon tea",
     "Iced peach tea",
     "ginger chai"
]

iced_tea = [my_tea for my_tea in menu if "iced" in my_tea.lower()]

print( iced_tea )

iced_tea =  [ tea for tea in menu if len(tea) < 12]
print( iced_tea )