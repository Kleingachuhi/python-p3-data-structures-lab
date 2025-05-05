spicy_foods = [
    {
        "name": "Green Curry",
        "cuisine": "Thai",
        "heat_level": 9,
    },
    {
        "name": "Buffalo Wings",
        "cuisine": "American",
        "heat_level": 3,
    },
    {
        "name": "Mapo Tofu",
        "cuisine": "Sichuan",
        "heat_level": 6,
    },
]


def get_names(spicy_foods):
    new_spicy_names = []
    for item in spicy_foods:
        new_spicy_names.append(item['name'])
    return(new_spicy_names)
get_names(spicy_foods)

def get_spiciest_foods(spicy_foods):
    hot_food = []
    for item in spicy_foods:
        if item['heat_level'] >5 :
            hot_food.append(item)
            return(hot_food)
    pass       
get_spiciest_foods(spicy_foods)

def print_spicy_foods(spicy_foods):
    for item in spicy_foods:
        print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶' * item['heat_level']}")
    pass
print_spicy_foods(spicy_foods)

def get_spicy_food_by_cuisine(spicy_foods, cuisine):
    for item in spicy_foods:
        if item['cuisine'] == cuisine:
            return(item)
    pass
get_spicy_food_by_cuisine(spicy_foods, "American")
get_spicy_food_by_cuisine(spicy_foods, "Thai")


def print_spiciest_foods(spicy_foods):
    for item in spicy_foods:
        if item['heat_level'] > 5:
                    print(f"{item['name']} ({item['cuisine']}) | Heat Level: {'🌶' * item['heat_level']}")

    pass
print_spiciest_foods(spicy_foods)


def get_average_heat_level(spicy_foods):
    total_heat = 0
    for item in spicy_foods:
        total_heat += item['heat_level']
    return int(total_heat / len(spicy_foods))  

get_average_heat_level(spicy_foods)


def create_spicy_food(spicy_foods, spicy_food):
    spicy_foods = [*spicy_foods, spicy_food]
    return(spicy_foods)
    pass
create_spicy_food(spicy_foods,    {
                "name": "Griot",
                "cuisine": "Haitian",
                "heat_level": 10,
            })