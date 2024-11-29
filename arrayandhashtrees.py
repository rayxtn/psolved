mylist = [1,2,3,4,1]



def find_duplicate(mylist):
    my_duplicate_list = mylist
    found_duplicate = False
    element_myduplicate = 0
    for value in mylist:
        if(value == my_duplicate_list[element_myduplicate]):
            found_duplicate = True
        else:
            element_myduplicate = element_myduplicate + 1
    return found_duplicate            
            
                
find_duplicate(mylist)    fdgdfgfd
