__author__ = 'Alif'

#Write a function to remove duplicate integers from a given integer array of given length. Return a
#new array with result, do not modify the existing array. Also return the length of the result array.

count_list = [10, 20, 10, 30, 30, 40, 20, 50, 90, 60, 80, 70, 80, 90]



def remove_duplicate(count_list):
    tup = [];
    new_list = list(tup)
    for index in range(len(count_list)):
        dup_bool = False
        hold =count_list[index]
        for index2 in range(len(new_list)):
            if(new_list[index2] == hold) :
                dup_bool = True
                break
            else :
                dup_bool = False

        if(dup_bool==False):
            new_list.insert(0,hold)
    new_list.sort()
    return new_list


print count_list
new_count_list = remove_duplicate(count_list)
print new_count_list
print 'Length',len(new_count_list)