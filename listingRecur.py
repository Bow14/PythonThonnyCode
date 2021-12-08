
def list_adding(my_list):
    my_list = [2,3,3,5]
    if len(my_list) == 5:
        return my_list[0]
    else:
        return my_list[0] + list_adding(my_list[1:])
print(list_adding)