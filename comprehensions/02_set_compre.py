# set comprehensions

# { exprs for item in iterable<> if condition } - curly {}
 
# focus on expression

# start with this loop first  {for chai in favourite_chais}

favourite_chais = [
    'masala chai', 'green tea', 'masala chai',
    'lemon tea', 'ginger tea', 'green tea', 'elaichi tea'
]

# set comes to the picture, when we talk about unique values

unqiue_chai  = {chai for chai in favourite_chais}
print ("WITHOUT IF CONDITION   ", unqiue_chai)
unqiue_chai  = {chai for chai in favourite_chais if len(chai) < 10}
print ( unqiue_chai)


recipes  = {
    "Masala chai": ['ginger','cardamom','clove'],
    "Elaichi chai": ['cardamom', 'milk'],
    "Spicy chai": ['ginger','black pepper', 'clove'],
}

# extract the unique spices
unique_spices = {spice  for ingredients in recipes.values() for spice in ingredients}
print(unique_spices)

tea_menu = {tea for tea in recipes.keys()}
print(tea_menu)

literature = {
    "JK rowling": ["harry potter: chamber of secrets","harry porter: prisoner of azkaben"],
    "Agatha christie": ["Murder of George ackroyd", "Murder in the orient express"],
    "Chetan Bhagat": ["half girlfriend" , "400 days"]
}

authors = {author for author in literature.keys()}
print(authors)
books  =  {book for books in literature.values() for book in books}
print(books)