def update_mark_list(mark_list, new_element, pos):
    mark_list.insert(pos,new_element)
    return mark_list

def find_mark(mark_list,pos1,pos2):
    rs=list()
    for i in range(len(mark_list)):
        if(i==pos1 or i==pos2 ):
            rs.append(mark_list[i])
    return rs
            
    
mark_list=[89,78,99,76,77,67,99,98,90]
new_element=78
pos=8
pos1=5
pos2=7
print(update_mark_list(mark_list, new_element, pos))
print(find_mark(mark_list, pos1, pos2))
