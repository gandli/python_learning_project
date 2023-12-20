"""
这个模块用于演示Python中的算术运算。
"""

# 定义两个数字
NUMBER1 = int(input("Enter first number or press enter for default (12): ") or 12)
NUMBER2 = int(input("Enter second number or press enter for default (3): ") or 3)

# 加法
print(f"加法结果:{NUMBER1+NUMBER2}")

# 减法
print(f"减法结果:{NUMBER1-NUMBER2}")

# 乘法
print(f"乘法结果:{NUMBER1*NUMBER2}")

# 除法（浮点数结果）
print(f"除法结果:{ NUMBER1 / NUMBER2 }")

# 整数除法
print(f"整数除法结果:{ NUMBER1 // NUMBER2 }")

# 取余
print(f"取余结果:{ NUMBER1 % NUMBER2 }")

# 幂运算
print(f"幂运算结果:{ NUMBER1 ** NUMBER2 }")
