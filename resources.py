# Aizhamal Rysbaeva
# Nov 5, 2024


# Problem 2
# check if a number is within a specified range of 1-10.
def lets_see(x):
    # see if x is in a range i make up
    # make a range
    # check if x is in a range
    a = 1
    b = 10

    if a <= x <= b:
        print(f"{x} is in the range.")
        return True
    else:
        print(f"{x} is not in the range.")
        return False


# lets_see(9)

print("i am in resources")


# Problem 5
# print a specific message if the file is run directly.
def main():
    print("this only happens when i run the file directly")


print("i will always get printed")
if __name__ == "_main_":
    main()
