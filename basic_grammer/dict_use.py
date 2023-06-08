import operator
data=[{"age":31,"city":"taipei"},{"age":19,"city":"rio"},{"age":20,"city":"london"},{"age":56,"city":"tokyo"}]
sorted_data=sorted(data, key=operator.itemgetter("age"))
for dic in sorted_data:
    print(dic)

