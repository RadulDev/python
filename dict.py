abc= {
    'name' : "ram",
    'age' : 20,
    'place' : "india",
    'work' : "graphic designer",
    'salary' : 23000
}

print(abc)

# print(abc['age'])
# print(abc['work'])
# print(abc['name'])
# print(abc['salary'])
# print(abc.value[23000])

print(len(abc))

for key,value in abc.items():
    # print (key, '->', abc[item])
    print(key, '->', value)