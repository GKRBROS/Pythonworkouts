def min_orbs(recipes, target_potion):
    from collections import defaultdict
    import sys
    recipe_dict = defaultdict(list)
    for recipe in recipes:
        potion, ingredients = recipe.split('=')
        ingredients = ingredients.split('+')
        recipe_dict[potion].append(ingredients)
    memo = {}  
    def dfs(potion):
        if potion not in recipe_dict:
            return 0
        if potion in memo:
            return memo[potion]  
        min_orbs = sys.maxsize
        for ingredients in recipe_dict[potion]:
            orbs = len(ingredients) - 1
            for ingredient in ingredients:
                orbs += dfs(ingredient)
            min_orbs = min(min_orbs, orbs)
        memo[potion] = min_orbs
        return min_orbs 
    return dfs(target_potion)

n = int(input())
recipes = [input().strip() for _ in range(n)]
target_potion = input().strip()
result = min_orbs(recipes, target_potion)
print(result)
