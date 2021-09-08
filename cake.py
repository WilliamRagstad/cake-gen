"""
A program that generates n number of random new cake recepies with different fillings, toppings and shapes.
The program should print the neccesarry ingredients with quantity and units, as well as the steps to take for baking the actual cake.
"""

import random

# The list of ingredients
ingredients = ["flour", "sugar", "eggs", "milk", "butter", "baking powder", "vanilla"]

# The list of steps
steps = ["Mix ingredients", "Put in oven", "Take out of oven", "Pour filling", "Decorate"]

# The list of shapes
shapes = ["round", "square", "triangle", "heart"]

# The list of fillings
fillings = ["strawberry jam", "raspberry jam", "cherry jam", "chocolate", "nuts", "cream", "vanilla", "caramel"]

# The list of toppings
toppings = ["whipped cream", "cocoa powder", "caramel"]

# The list of baking times
baking_times = ["10", "15", "20", "25", "30", "35", "40", "50"]

# The list of oven temperatures
oven_temperatures = ["180", "190", "200", "210", "220", "230", "240", "250", "260", "270", "280", "290", "300"]

# The list of baking methods
baking_methods = ["in the oven", "on the grill", "in the toaster"]

# The list of cake types
cake_types = ["cake", "muffin", "cupcake"]

"""
Combine the different lists of steps, shapes, fillings and topings, etc, to generate
a pretty printed recepie of a complete cake.
"""
def generate_recepie():
    # Generate a random number of steps
    steps_nr = random.randint(2, len(steps))

    # Generate a random number of shapes
    shapes_nr = random.randint(1, len(shapes))

    # Generate a random number of fillings
    fillings_nr = random.randint(1, len(fillings))

    # Generate a random number of toppings
    toppings_nr = random.randint(1, len(toppings))

    # Generate a random number of baking times
    baking_times_nr = random.randint(1, len(baking_times))

    # Generate a random number of oven temperatures
    oven_temperatures_nr = random.randint(1, len(oven_temperatures))

    # Generate a random number of baking methods
    baking_methods_nr = random.randint(1, len(baking_methods))

    # Generate a random number of cake types
    cake_types_nr = random.randint(1, len(cake_types))

    # Print the recepie
    print("\n")
    print("--- Recepie: " + shapes[shapes_nr - 1]+ " " + cake_types[cake_types_nr - 1] + " ---")
    print("\n")

    """
    Print the ingredients with name, quantity and units
    """
    print("--- Ingredients ---")
    for i in range(0, len(ingredients)):
        print(ingredients[i] + ": " + str(random.randint(1, 10)) + " " + random.choice(["kg", "g", "l", "ml", "cl", "dl"]))
    print("\n")
    """
    Print the steps with number and description
    """
    print("--- Steps ---")
    for i in range(0, steps_nr):
        print(str(i + 1) + ". " + steps[i])
    print("\n")
    """
    Print a random filling and topping
    """
    print("--- Filling ---")
    print(fillings[fillings_nr - 1])
    print("\n")
    print("--- Topping ---")
    print(toppings[toppings_nr - 1])
    print("\n")
    """
    Print the expected duration of the baking from start to finnish taking the number of steps into consideration
    """
    print("--- Duration ---")
    print("Expected duration: " + str(steps_nr * random.randint(1, 10) + int(baking_times[baking_times_nr - 1])) + " minutes")
    print("\n")
    """
    Print the baking temperature and method
    """
    print("--- Baking temperature and method ---")
    print(str(oven_temperatures[oven_temperatures_nr - 1]) + " degrees Celsius " + baking_methods[baking_methods_nr - 1])
    print("\n")
    """
    Print the baking temperature, method and time in the oven
    """
    print("--- Baking ---")
    print("Baking temperature: " + oven_temperatures[oven_temperatures_nr - 1] + " degrees")
    print("Baking method: " + baking_methods[baking_methods_nr - 1])
    print("Baking time: " + baking_times[baking_times_nr - 1] + " minutes")
    print("\n")
    print("--- Enjoy your cake! ---")
    print("\n")
    

# Generate a recepie
generate_recepie()
