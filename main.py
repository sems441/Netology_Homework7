cook_book = {}


def read_food_recipe(cook):
    cook_book[cook] = ""
    step = int(file.readline())
    current_ingredients = []
    for count in range(0, step):
        ingredients = file.readline().rstrip()
        ingredients = list(ingredients.split(sep="|"))
        new = {"ingredient_name": ingredients[0], "quantity": ingredients[1], "measure": ingredients[2]}
        current_ingredients.append(new)
    cook_book[cook] = current_ingredients
    _ = file.readline()


def get_shop_list_by_dishes(dishes, person_count):
    name_ingredient = {}
    for nutrition in dishes:
        for ingredient in cook_book[nutrition]:
            total = int(ingredient["quantity"]) * person_count
            name = ingredient["ingredient_name"]
            if name in name_ingredient:
                name_ingredient[name]["quantity"] += total
            else:
                name_ingredient[name] = {"measure": ingredient["measure"], "quantity": total}
    print("\nСловарь с ингридиентами (повторяются помидоры)")
    print(name_ingredient)


with open("recipt.txt", encoding="utf-8") as file:
    for recipe in file:
        recipe = recipe.rstrip()
        read_food_recipe(recipe)

print("\nСловарь с рецептами")
print(cook_book)

food = ["Омлет", "Фахитос"]
get_shop_list_by_dishes(food, 3)
