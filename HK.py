# Pandas

import pandas as pd

# **1. 初始化資料**
# 建立初始 DataFrame，包含範例資料
data = {
    'Name': ['Alice', 'Bob', 'Charlie'],  # 姓名
    'Age': [25, 30, 35],                 # 年齡
    'City': ['Taipei', 'Kaohsiung', 'Taipei']  # 城市
}
df = pd.DataFrame(data)

# 顯示初始資料
print("初始資料：")
print(df)

# **2. 新增資料：使用 df.loc[len(df)]**
# 新增一筆新資料到 DataFrame 的最後一行
new_data = {
    'Name': 'David',  # 姓名
    'Age': 28,        # 年齡
    'City': 'New Taipei'  # 城市
}
df.loc[len(df)] = new_data  # 新增資料
print("\n新增資料後的結果：")
print(df)

# **3. 篩選資料：df[df['欄位名稱'] == 值]**
# 篩選出居住在 Taipei 的資料
filtered_df = df[df['City'] == 'Taipei']
print("\n篩選結果（居住在 Taipei 的人）：")
print(filtered_df)

# **4. 計算欄位總和：df['欄位名稱'].sum()**
# 計算 Age 欄位的總和
total_age = df['Age'].sum()
print(f"\n年齡總和: {total_age}")

# **5. 編輯資料：使用 df.loc[index]**
# 修改第 1 行的資料
print("\n編輯前的資料（第 1 行）：")
print(df.loc[1])  # 查看第 1 行的資料

df.loc[1, 'City'] = 'Taichung'  # 修改第 1 行的 City 欄位
print("\n編輯後的資料（第 1 行）：")
print(df.loc[1])  # 查看修改後的資料

# **6. 刪除資料：使用 df.drop(index)**
# 刪除第 0 行的資料
df = df.drop(0)  # 刪除第 0 行
print("\n刪除第 0 行後的資料：")
print(df)

# **7. 將資料儲存到 CSV：使用 df.to_csv()**
# 將資料儲存到 CSV 檔案中
filename = 'data.csv'
df.to_csv(filename, index=False)  # 儲存到 CSV，並移除索引
print(f"\n資料已儲存到 {filename}")

# **8. 從 CSV 載入資料：使用 pd.read_csv()**
# 嘗試從 CSV 檔案載入資料，並處理檔案不存在的情況
try:
    df_loaded = pd.read_csv(filename)  # 從 CSV 載入資料
    print(f"\n從 {filename} 載入的資料：")
    print(df_loaded)
except FileNotFoundError:
    # 若檔案不存在，建立空的 DataFrame
    df_loaded = pd.DataFrame(columns=['Name', 'Age', 'City'])
    print(f"\n檔案 {filename} 不存在，建立新的資料表：")
    print(df_loaded)