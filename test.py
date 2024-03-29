def recursive_function(obj, depth):
    if depth == 0:
        return
    print(f"Depth {depth}: {obj}")
    recursive_function(obj, depth - 1)

# 创建一个对象
my_object = {"key": "value"}

# 调用递归函数，并传递相同的对象和深度
recursive_function(my_object, 3)
