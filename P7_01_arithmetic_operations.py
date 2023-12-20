"""
这个模块用于演示Python中的算术运算。
"""

# 定义两个数字
number1 = float(input("输入第一个数字或按回车键设置默认值 (12): ") or 12)
number2 = float(input("输入第二个数字或按回车键设置默认值 (3): ") or 3)

print(
    f"第一个数字: {number1}，类型: {type(number1)}\n"
    f"第二个数字: {number2}，类型: {type(number2)}\n"
    f"加法结果:{number1+number2}\n"
    f"减法结果:{number1-number2}\n"
    f"乘法结果:{number1*number2}\n"
    f"除法结果:{ number1 / number2 }\n"
    f"整数除法结果:{ number1 // number2 }\n"
    f"取余结果:{ number1 % number2 }\n"
    f"幂运算结果:{ number1 ** number2 }"
)
