# The item's discount and stock status have been defined
discounted = False
lowStock = True

#Should the product be sold
movingProduct = True

# Is it discounter or low in stock?
movingProduct = discounted or lowStock

#Promotion if NOT a moving product
promotion = not movingProduct

# Print the result
print("Is the item eligible for promotion?", promotion)