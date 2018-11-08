# Будем считать, что в этой переменной лежит список рецептов из
# задачи
recipe_book = { }

# Проверяем каждый ингридиент. Если название то, что нам нужно -
# то сразу возвращает True, т.о. завершая цикл - мы нашли что
# искали.  если среди всех ингридиентов мы не нашли искомый(т.е.
# условие не выполнилось и мы не выполнили `return True` и цикл
# закончил свою работу), то вовращаем False - искомого
# ингридиента в рецепте нет
def is_sausage(recipe):
    for ingridient in recipe['ingridients']:
        if ingridient['name'] == "Докторская колбаса":
            return True
    return False

# применяем функцию к каждому элементу и запоминаем только нужные
def filter_recipe(predicate, recipes):
    result = []
    for item in recipes:
        if predicate(item):
            result.append(item)
    return result

recipes_with_sausage = filter_recipe(is_sausage,
                                     recipe_book)
# тоже самое, но со стандартной функцией из библиотеки python
recipes_with_sausage = filter(is_sausage, recipe_book)

#печатаем найденные рецепты
print(recipes)
