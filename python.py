# 函數與程序結構

# 基本函數定義
def basic_function():
    """
    # 基礎函數定義
    # 使用 def 關鍵字定義函數
    """
    pass

print("調用基本函數:")
basic_function()  # 輸出: 無返回值

# 帶參數的函數
def with_params(a, b, c=10):
    """
    # 函數參數示例
    # a, b 為必需參數
    # c 為默認參數
    """
    return a + b + c

print("\n帶參數函數示例:")
result = with_params(5, 3)  # 使用默認值 c=10
print(f"5 + 3 + 10 = {result}")  # 輸出: 18
result = with_params(5, 3, 2)  # 覆蓋默認值
print(f"5 + 3 + 2 = {result}")  # 輸出: 10

# Lambda 函數示例
# 簡短的匿名函數
square = lambda x: x**2

print("\nLambda 函數示例:")
print(f"5 的平方 = {square(5)}")  # 輸出: 25

# 作用域示例
global_var = 100
def scope_demo():
    """
    # 變量作用域示例
    # global 關鍵字用於修改全局變量
    """
    global global_var
    local_var = 200
    return local_var + global_var

print("\n作用域示例:")
print(f"局部變量 + 全局變量 = {scope_demo()}")  # 輸出: 300

# 遞迴函數示例
def factorial(n):
    """
    # 遞迴函數示例
    # 計算階乘
    """
    return 1 if n <= 1 else n * factorial(n-1)

print("\n遞迴函數示例:")
print(f"5! = {factorial(5)}")  # 輸出: 120

# 文檔字符串示例
def documented_function():
    """
    # 這是文檔字符串
    # 用於說明函數用途
    # 可使用 help() 查看
    """
    pass

print("\n文檔字符串示例:")
help(documented_function)  # 輸出函數的文檔字符串

# 異常處理示例
def safe_division(a, b):
    """
    # 異常處理示例
    # 處理除零錯誤
    """
    try:
        return a / b
    except ZeroDivisionError:
        return "除數不能為零"

print("\n異常處理示例:")
print(f"10 / 2 = {safe_division(10, 2)}")  # 輸出: 5.0
print(f"10 / 0 = {safe_division(10, 0)}")  # 輸出: 除數不能為零

# 模塊導入示例
"""
# 模塊導入方式：
import math
from math import sqrt
from math import *

print("\n模塊使用示例:")
print(f"sqrt(16) = {math.sqrt(16)}")  # 輸出: 4.0
"""

# 主要知識點總結：
"""
1. 函數定義與調用
2. 參數類型（位置參數、關鍵字參數、默認參數）
3. 變量作用域（局部、全局）
4. Lambda 函數
5. 遞迴
6. 文檔字符串
7. 異常處理
8. 模塊與包的使用
"""""" 
hnbgyg