def binary_search(item, my_list):
    found = False
    bottom = 0
    top = len(my_list) - 1
    counter = 0
    
    while bottom <= top and not found:
        counter += 1
        print(f"Search Count {counter}")
        middle = (bottom + top) // 2
        print(f"Current Middle Position {middle}")
        if my_list[middle] == item:
            found = True
        elif my_list[middle] < item:
            bottom = middle + 1
            print(f"Current Bottom Position {bottom}")
        else:
            top = middle - 1
            print(f"Current Top Position {top}")
            
    return found

num_list = [1, 4, 6, 8, 12, 15, 18, 24, 27, 31, 42, 44, 47]
item = 42

result = binary_search(item, num_list)

if result:
    print(f"Found the number {item}!")
