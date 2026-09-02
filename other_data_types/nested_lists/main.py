vegetables = ["tomatoes", "potatoes", "onions"]

# Removing an item from the grocery list
vegetables.remove("onions")

# Adding a new sublist item to the grocery list
vegetables.append("carrots")
vegetables.append("cucumbers")

#If Statement
if "carrots" not in vegetables:
    vegetables.append("carrots")
else:
    print("Carrots are already in the list.")

if "cucumbers" not in vegetables:
    vegetables.append("cucumbers")
else:
    print("Cucumbers are already in the list.")

# Sorting the vegetables list alphabetically
vegetables.sort()
print("Updated Vegetable Inventory:", vegetables)
