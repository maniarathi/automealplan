import sys

sys.path.append(".")
from data.ingredients import INGREDIENTS
from data.pantry import PANTRY
from data.recipes import RECIPES
from data.substitutions import SUBSTITUTIONS


# Tests TODO:
#  -write something that converts amounts from string to [unit, value] and make
#   sure it works for (1) all recipe amounts and (2) all purchase amounts

def validate_pantry_ingredients_are_in_ingredients():
    all_ingredients = INGREDIENTS.keys()
    validation_passed = True

    for pantry_ingredient in PANTRY:
        if pantry_ingredient not in all_ingredients:
            print(f"DEEDOODEEDOO ERROR: {pantry_ingredient} in pantry not in ingredient list!!!")
            validation_passed = False

    return validation_passed


def validate_all_ingredients_in_recipe_are_in_ingredients():
    all_ingredients = INGREDIENTS.keys()
    validation_passed = True

    for recipe_name in RECIPES:
        recipe_ingredients = RECIPES.get(recipe_name).get("ingredients").keys()
        for ingredient in recipe_ingredients:
            if ingredient not in all_ingredients:
                print(f"DEEDOODEEDOO ERROR: {ingredient} in recipe {recipe_name} not in ingredient list!!!")
                validation_passed = False
    return validation_passed


def validate_ingredients():
    valid_rareness_values = ["rare", "uncommon", "common"]
    validation_passed = True

    for ingredient, ingredient_metadata in INGREDIENTS.items():
        rareness = ingredient_metadata.get("rareness")
        if not rareness:
            print(f"DEEDOODEEDOO ERROR: Ingredient {ingredient} does not have a rareness value.")
            validation_passed = False
        elif rareness not in valid_rareness_values:
            print(f"DEEDOODEEDOO ERROR: Ingredient {ingredient} has an invalid rareness value {rareness}!")
            validation_passed = False

    return validation_passed


def validate_substitutions():
    all_ingredients = INGREDIENTS.keys()
    valid_goodness_scores = ["good", "fine", "poor"]
    validation_passed = True

    for substitution in SUBSTITUTIONS:

        # Validate that the from ingredient and to ingredient exists in the ingredients list.
        from_ingredient = substitution.get("from")
        to_ingredient = substitution.get("to")
        if from_ingredient not in all_ingredients:
            print(f"DEEDOODEEDOO ERROR: {from_ingredient} in substitution not in ingredient list!!!")
            validation_passed = False
        if to_ingredient not in all_ingredients:
            print(f"DEEDOODEEDOO ERROR: {to_ingredient} in substitution not in ingredient list!!!")
            validation_passed = False

        # Validate that each substitution has a goodness score
        goodness = substitution.get("goodness")
        if not goodness:
            print(f"DEEDOODEEDOO ERROR: Substitution {from_ingredient} to {to_ingredient} is missing a goodness score!")
            validation_passed = False
        elif goodness not in valid_goodness_scores:
            print(
                f"DEEDOODEEDOO ERROR: Substitution {from_ingredient} to {to_ingredient} has invalid goodness "
                f"{goodness}!")
            validation_passed = False

    return validation_passed


if __name__ == "__main__":
    result1 = validate_all_ingredients_in_recipe_are_in_ingredients()
    result2 = validate_ingredients()
    result3 = validate_pantry_ingredients_are_in_ingredients()
    result4 = validate_substitutions()

    if result1 and result2 and result3 and result4:
        print("VALIDATION PASSED!")
