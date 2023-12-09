def print_number_pyramid(rows):
    num = 1
    gap = "  "
    for i in range(1, rows+1):
        print(gap*(rows-i), end=" ")
        for j in range(1, i+1):
            print("{:3}".format(num), end=gap)
            num += 1
            if num > 100:
                break
        print()
print_number_pyramid(10)