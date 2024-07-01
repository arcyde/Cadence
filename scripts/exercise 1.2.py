def value_in_list(my_value, my_list):
    if my_value in my_list:
        print(f'The value {my_value} is present in this list, index: {my_list.index(my_value)}')
    else:
        print(f'The value {my_value} is not in this list')
        
list_1 = list(range(1, 1000001))
print('Approach 1')
value_in_list(518741, list_1)
value_in_list(1000001, list_1)
print()

def binary_search(my_list, desired_value, initial_position = None, final_position = None): 
    initial_position = 0 if not initial_position else initial_position
    final_position = len(my_list) - 1 if not final_position else final_position
    found = False

    while initial_position <= final_position and not found:
        mid_term = (initial_position + final_position) // 2
        try:
            if my_list[mid_term] == desired_value: 
                found = True                     
                return 'The value {} is present in this list, index: {}'.format(desired_value, mid_term)
            if my_list[mid_term] > desired_value:
                final_position = mid_term - 1
            else:
                initial_position = mid_term + 1
        except IndexError:
            final_position = mid_term - 1
      
    return 'The value {} is not in this list'.format(desired_value)
    

list_2 = list(range(1, 1000001))
print('Approach 2')
print(binary_search(list_2, 54844))
print(binary_search(list_2, 1000001))
print()

def search_element(my_list, value):
    initial_position = 0
    final_position = 1
    
    while True:
        try:
            if my_list[final_position] == value:
                return final_position
            if my_list[final_position] > value:
                break
            final_position *= 2
        except IndexError:
            final_position -= 1
            break 
    
    return binary_search(my_list, value, initial_position, final_position)

list_3 = list(range(1, 1000001))
print('Approach 3')
print(search_element(list_3, 4887))
print(search_element(list_3, 1000001))
print()    