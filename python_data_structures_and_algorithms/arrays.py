arrs = [1, 5, 9, 7, 5, 0]


def print_arrs(datas):
    for x in datas:
        print(x)


def insert_arrs(index, value, datas):
    datas.insert(index, value)
    return datas


def pop_arrs(index, datas):
    datas.pop(index)
    return datas


def update_arrs(index, value, datas):
    datas[index] = value
    return datas


# insert array
print('* insert array')
insert_arrs(1, 10, arrs)
print(arrs)

# remove array by index
print('* remove array by index')
pop_arrs(1, arrs)
print(arrs)

# update value by index
update_arrs(1, -10, arrs)
print(arrs)
