def get_cook_book_dict(file):
    with open(file, encoding='utf-8') as f:
        cook_book_list = f.readlines()
        row_number = 0
        cook_book_dict = {}
        for item in cook_book_list:
            if item.strip().isdigit():
                ingredients_list = []
                for ingredient in cook_book_list[row_number+1:row_number+int(item)+1]:
                    _ = {}
                    _['ingredient_name'] = ingredient.split('|')[0].strip()
                    _['quantity'] = ingredient.split('|')[1].strip()
                    _['measure'] = ingredient.split('|')[2].strip()
                    ingredients_list.append(_)
                cook_book_dict[cook_book_list[row_number-1].strip()] = ingredients_list

            row_number += 1
    return cook_book_dict


def get_shop_list_by_dishes(dishes, person_count):
    cook_book_dict = get_cook_book_dict('recipes.txt')
    shop_list = {}
    for dish in dishes:
        for ingredient in cook_book_dict[dish]:
            if ingredient['ingredient_name'] in shop_list.keys():
                shop_list[ingredient['ingredient_name']]['quantity'] += int(ingredient['quantity']) * person_count
            else:
                a = ingredient['ingredient_name']
                ingredient.pop('ingredient_name')
                ingredient['quantity'] = int(ingredient['quantity']) * person_count
                shop_list[a] = ingredient
    return shop_list

get_cook_book_dict('recipes.txt')