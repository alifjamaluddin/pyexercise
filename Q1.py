__author__ = 'Alif'

#Write a function in Python language to calculate the average of the numbers in the list above.

count_list = [10, 20, 30, 40, 50, 60, 70, 80, 90]
print count_list

def avg(listno):
    sum = 0
    count = 0
    for no in listno:
        sum+=no
        count+=1
    avg = sum/count
    return avg

print avg(count_list)
