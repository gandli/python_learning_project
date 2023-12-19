import random


def quick_sort(nums):
    # 分区函数，用于确定枢纽元素的位置并将数组分成两部分
    def partition(left, right):
        # 随机选择一个枢纽元素，并将其交换到右边
        pivot_index = random.randint(left, right)
        nums[pivot_index], nums[right] = nums[right], nums[pivot_index]
        pivot = nums[right]
        i = left - 1

        # 遍历数组，将小于等于枢纽元素的元素移动到左边，大于枢纽元素的元素移动到右边
        for j in range(left, right):
            if nums[j] <= pivot:
                i += 1
                nums[i], nums[j] = nums[j], nums[i]

        # 将枢纽元素交换到正确的位置
        nums[i + 1], nums[right] = nums[right], nums[i + 1]
        return i + 1

    # 快速排序的辅助函数
    def quick_sort_helper(left, right):
        if left < right:
            pivot_index = partition(left, right)
            # 递归地对左右两部分进行快速排序
            quick_sort_helper(left, pivot_index - 1)
            quick_sort_helper(pivot_index + 1, right)

    # 初始调用快速排序函数
    quick_sort_helper(0, len(nums) - 1)


# 生成一个包含 n 个随机整数的列表
def generate_random_list(n):
    return [random.randint(0, 100) for _ in range(n)]


if __name__ == "__main__":
    nums = generate_random_list(99)
    print(nums)
    quick_sort(nums)
    print(nums)
