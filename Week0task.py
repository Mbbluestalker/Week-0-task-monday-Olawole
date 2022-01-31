def print_triangle(num):
    num_arr = []
    for x in range(0, num - 1):
        x = (2 * x) + 1
        num_arr.append(x)
    num_arr = num_arr[::-1]
    for y in num_arr:
        print(y * "*")


print_triangle(9)