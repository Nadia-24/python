#multiple_lists are created a nested list
#nested_list = [[1,2],['a','b'],['h',5]]
#index            0       1         3

#Hackerrank python nested_list problem

list = [['nadia', 45.0], ['shajia', 34.0], ['moon', 34.0],['abc', 20]]
find_score = [i[1] for i in list]
set_score = set(find_score)
sort_score = sorted(set_score)
print(sort_score[1])

find_name = sorted([i[0] for i in list if(sort_score[1] == i[1])])
print(find_name)

for i in find_name:
    print(i)
