initial_row_values = input()
input_list = []
for _ in range(7):
    try:
        temp = input()
        input_list.append(temp[2:])
    except:
        pass
input_list_as_ints =[]
for item in input_list:
    input_list_as_ints.append([])
    for _ in range(7):
        try:
                input_list_as_ints[-1].append(int(item))
                item = ""
        except:
            try:
                splitter = item.find(' ')
                input_list_as_ints[-1].append(int(item[0:splitter]))
                item = item[splitter+1:]
            except:
                pass
initial_row_space_index = initial_row_values.find(" ")
k = int(initial_row_values[:initial_row_space_index])
m = int(initial_row_values[initial_row_space_index+1:])
solutions=[]
for index in range(len(input_list_as_ints)):
    for index2 in range(len(input_list_as_ints[index])):
        input_list_as_ints[index][index2] = input_list_as_ints[index][index2] ** 2
for a in input_list_as_ints[0]:
    try:
      for b in input_list_as_ints[1]:
            try:
                for c in input_list_as_ints[2]:
                    try:
                        for d in input_list_as_ints[3]:
                            try:
                                for e in input_list_as_ints[4]:
                                    try:
                                        for f in input_list_as_ints[5]:
                                            try:
                                                for g in input_list_as_ints[6]:
                                                    solutions.append(g+f+e+d+c+b+a)
                                            except:
                                                solutions.append(f+e+d+c+b+a)
                                    except:
                                        solutions.append(e+d+c+b+a)
                            except:
                                solutions.append(d+c+b+a)
                    except:
                        solutions.append(c+b+a)
            except:
                solutions.append(b+a)
    except:
        solutions.append(a)
solutions2 = []
for abcd in solutions:
    solutions2.append(abcd % m)
print(max(solutions2))
