# Aizhamal Rysbaeva
# Nov 5, 2024

# Problem 1
# take a name as a parameter and print a friendly or angry greeting at random
import random
import resources

# check to make sure you can use the function in the other file!
# make a choice list, that has only 0 or 1 in it
# use random choice to pick one valu and ...


def say_my_name(string):
    greetings = random.choice([0, 1])

    if greetings == 0:
        print(f"yo, {string}")
    else:
        print(f"have a bad day, {string}")


say_my_name("Aizhamal")
resources.lets_see(9)

# Problem 3
# a list of random numbers and multiplies by 5 any numbers within the range defined by lets_see.


def multiply_if():

    list = [random.randrange(1, 20) for _ in range(10)]
    results = []
    for x in list:
        if resources.lets_see(x):
            results.append(x*5)
        else:
            results.append(x)
        print(results)
    return results


multiply_if()


# Problem 4
# This function takes a list, removes duplicates
# and returns the sorted list of unique elements.
def unique_elements(new_list):
    unique_list = []

    for item in new_list:
        if item not in unique_list:
            unique_list.append(item)

    unique_list.sort()
    return unique_list


print("unique elements are ", unique_elements([1, 3, 3, 3, 6, 2, 3, 5]))
