# 基本 Python 語法示例

# 1. 註釋（Comments）
# 單行註釋
# 這是一個單行註釋

# docstring
'''
多行註釋
可以用來寫多行文字
'''

"""
多行註釋也可以用雙引號
"""

# 2. 變量（Variables）
# 定義不同類型的變量（Variables）
# 格式：變量名（Identifier） = 值（Value）
name = "Alice"      # 字符串 (String)
age = 25            # 整數 (Integer)
salary = 70000.0    # 浮點數 (Float)
is_true = True      # 布爾值 (Boolean)

# 3. 數據類型（Data Types）

# 字符串 (String)
text = "Python"     # 字符串示例
text = 'Python'     # 字符串示例
text = '''Python'''     # 字符串示例
text = """Python"""     # 字符串示例

# 數字型 (Numbers)
integer_num = 10    # 整數 (Integer)
float_num = 10.5    # 浮點數 (Float)

# 布爾型 (Boolean)
is_active = True    # 布爾值 (Boolean)

# 列表 (List)
my_list = ['Alice', 'Bob', 'Charlie']  # 列表包含多個元素

# 字典 (Dictionary)
my_dict = {  # 字典包含鍵值對
    'Name': ['Alice', 'Bob', 'Charlie'],  # 鍵 'Name' 對應的值是一個列表
    'Age': [25, 30, 35],                  # 鍵 'Age' 對應的值是一個列表
    'City': ['New York', 'Los Angeles', 'Chicago']  # 鍵 'City' 對應的值是一個列表
}

# 4. 使用 Pandas 處理數據
import pandas as pd

# 創建 DataFrame
df = pd.DataFrame(my_dict)

# 顯示原始 DataFrame
print("原始 DataFrame:")
print(df)

# 訪問特定列
print("\n訪問 'Name' 列:")
print(df['Name'])

# 使用 iloc 訪問特定行
print("\n使用 iloc 訪問第二行:")
print(df.iloc[1])

# 添加新列
df['Salary'] = [70000, 80000, 75000]
print("\n添加 'Salary' 列後的 DataFrame:")
print(df)

# 基於條件過濾行
filtered_df = df[df['Age'] > 28]
print("\n年齡大於 28 的過濾後 DataFrame:")
print(filtered_df)

# 計算平均工資
average_salary = df['Salary'].mean()
print(f"\n平均工資: {average_salary}")