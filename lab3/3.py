def h1(list):
    if len(list) > 3:
        max_value = float('-inf')
        observed_list = list[1:(len(list)-1)] 
        for element_one in observed_list:
            if element_one > max_value:
                max_value = element_one
        max_value_two = float('-inf')
        for element_two in list[1:(len(list)-1)] :
            if element_two < max_value and element_two > max_value_two:
                max_value_two = element_two
    else:
        return None
    if max_value_two == float('-inf'):
       return None
    return max_value_two


def h2(list):
    if len(list) >= 1: 
        modul = []   
        for i in range(len(list)):
            if i%2 == 0 and list[i] <= 0:
                modul.append(list[i]%7)
        if len(modul) <= 0:
            return 0
        max_mod = float('-inf')
        for md in modul:  
            if md > max_mod:  
                max_mod = md  
                count = 1     
            elif md == max_mod:
                count += 1
    else:   
        count = 0
    return count
