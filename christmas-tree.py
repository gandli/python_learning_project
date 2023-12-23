# import numpy as np

# x = np.arange(7, 16)
# y = np.arange(1, 18, 2)
# z = np.column_stack((x[::-1], y))

# for i, j in z:
#     print(" " * i + "*" * j)

# for _ in range(3):
#     print(" " * 13, "| |")

# print(" " * 11, end="\\\\=====//")
# print(" ")


def print_christmas_tree(height=5):
    # 计算每层的空格数和星号数
    spaces = range(height - 1, -1, -1)
    stars = range(1, height * 2, 2)

    # 打印圣诞树的主体部分
    for i, j in zip(spaces, stars):
        print(" " * i + "*" * j)

    # 打印圣诞树的树干
    # stump_width = height // 2
    stump_width = (max(stars) - 3) // 2
    for _ in range(3):
        print(" " * stump_width + "| |")

    # 打印圣诞树的底座
    print(" " * (stump_width - 3), end="\\\\=====//\n")


# 调用函数打印圣诞树
print_christmas_tree()
