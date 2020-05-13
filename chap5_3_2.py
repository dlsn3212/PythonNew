# def power(item):
#     return item * item

power = lambda item: item * item

# def under_3(item):
#     return item < 3

under_3 = lambda item : item < 3

lists = [1,2,3,4,5]

output = map(power,lists)
print(output)
print(list(output))

output_b = filter(under_3,lists)
print(output_b)
print(list(output_b))