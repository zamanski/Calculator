def calc():
    sub_or_add = input("enter sub or add")
    nums = input("enter numbers")
    num_arr = nums.split(',')
    print(num_arr)
    if sub_or_add == '-':
        return Subtractor.Subtractor(num_arr)