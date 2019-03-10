def linear_search(my_item, my_list):

    count = 0
    position = 0
    found = False

    while position < len(my_list) and not found:
        if my_list[position] == my_item:
            found = True
        position += 1 
        count += 1
        print 'Current Search Count: {}'.format(count)

        if my_item not in my_list:
            my_list.append(my_item)

    return found

game_list = ["Devil May Cry 5", "World of Final Fantasy", "Super Mario Odyssey"]
item = "Super Mario Odyssey"
second_item = "Diablo 3"

""" test for existing entry """
result = linear_search(item, game_list)
if result:
    print 'Found item: {}'.format(item)

""" test for the in operator """
result_two = linear_search(second_item, game_list)
if result_two:
    print 'Found item: {}'.format(second_item)
