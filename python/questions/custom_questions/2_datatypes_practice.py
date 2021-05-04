# datatypes practice


if __name__ == '__main__':
    # Lists use square brackets
    my_list = [10, 20, 30, 40, 50]
    print(my_list)
    print(type(my_list))

    # iterate through list using pointer
    for x in range(0, len(my_list)):
        print(my_list[x])

    # iterate through elements in list directly
    for x in my_list:
        print(x)

    # Tuples specifically use parenthesis
    my_tuple = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)
    my_tuple2 = ('s', 'u', 'p', 'r', 'e', 'm', 'e',)
    print(my_tuple2)
    print(type(my_tuple))
    for x in range(0, len(my_tuple)):
        print(my_tuple[x])
    for x in my_tuple:
        print(x)

    # dictionary, uses key value pairs

    my_dict = {'Judgment Dragon': 'Light', 'Dark Armed Dragon': 'Dark', 'Stardust Dragon': 'Wind'}
    # print(my_dict)
    for key in my_dict:
        print(key)  # these are the keys
        print(my_dict.get(key))  # these are the values

    for key, val in my_dict.items():
        print(key)
        print(val)

    # sets use curly brackets
    my_set = {10, 20, 30, 40, 50}
