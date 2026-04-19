# Lists of items and categories for slicing
items = "Bubblegum, Chocolate, Pasta"
categories = "Candy Aisle, Pasta Aisle"

#Data_define
items     = "Bubblegum, Chocolate, Pasta"
candy1    = items[0:9]      # "Bubblegum"
candy2    = items[11:20]   # "Chocolate"
dry_goods = items[22:27]     # "Pasta"

#Data items
bubblegum = candy1
chocolate = candy2
pasta = dry_goods

#Data categories
category1 = "Candy Aisle"
category2 = "Pasta Aisle"

#Price
bubblegum_price = "$1.50"
chocolate_price = "$2.00"
pasta_price = "$5.40"
#Message
print(f"We have {candy1} for {bubblegum_price} in the {category1}")
print(f"We have {candy2} for {chocolate_price} in the {category1}")
print(f"We have {dry_goods} for {pasta_price} in the {category2}")

