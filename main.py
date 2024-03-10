import matplotlib.pyplot as plt
import numpy as np

s = {
    'X': [10, 8, 13, 9, 11, 14, 6, 4, 12, 7, 5],
    'Y_D1': [8.04, 6.95, 7.58, 8.81, 8.33, 9.96, 7.24, 4.26, 10.84, 4.82, 5.68],
    'Y_D2': [9.14, 8.14, 8.74, 8.77, 9.26, 8.10, 6.13, 3.10, 9.13, 7.26, 4.74],
    'Y_D3': [7.46, 6.77, 12.74, 7.11, 7.81, 8.84, 6.08, 5.39, 8.15, 6.42, 5.73],
    'Y_D4': [6.58, 5.76, 7.71, 8.84, 8.47, 7.04, 5.25, 12.50, 5.56, 7.91, 6.89]
}

# 任务一
# 单个散点图
# 绘制散点图
# plt.scatter(s['X'], s['Y_D1'], color='red', label='Y_D1')
# plt.scatter(s['X'], s['Y_D2'], color='blue', label='Y_D2')
# plt.scatter(s['X'], s['Y_D3'], color='green', label='Y_D3')
# plt.scatter([8]*11, s['Y_D4'], color='purple', label='Y_D4')
#
# # 添加图例
# plt.legend()
#
# # 添加标题和标签
# plt.title('Scatter Plot of Four Data Groups')
# plt.xlabel('X')
# plt.ylabel('Y')
#
# # 显示图形
# plt.show()

# # 多个散点图
# # 创建4个子图
# fig, axs = plt.subplots(4, 1, figsize=(8, 12))
#
# # 绘制每个子图
# for i, key in enumerate(['Y_D1', 'Y_D2', 'Y_D3', 'Y_D4']):
#     if key == 'Y_D4':
#         s['X'] = [8]*11
#     axs[i].scatter(s['X'], s[key], label=key)
#     axs[i].set_title(f'Scatter Plot of {key}')
#     axs[i].set_xlabel('X')
#     axs[i].set_ylabel('Y')
#     axs[i].legend()
#
# # 调整子图之间的间距
# plt.tight_layout()
#
# # 显示图形
# plt.show()
#

x_mean = sum(s['X']) / 11
y_mean = sum(s['Y_D1']) / 11
up = 0
bot = 0
for i, j in zip(s['X'], s['Y_D1']):
    up += (i - x_mean)*(j - y_mean)
    bot += (i - x_mean) ** 2
a = up / bot
b = y_mean - a * x_mean

# 绘制散点图
plt.scatter(s['X'], s['Y_D1'], color='red', label='Y_D1')
plt.scatter(s['X'], s['Y_D2'], color='blue', label='Y_D2')
plt.scatter(s['X'], s['Y_D3'], color='green', label='Y_D3')
plt.scatter([8]*11, s['Y_D4'], color='purple', label='Y_D4')
x = np.array(s['X'])
plt.plot(x, a * x + b, 'r', label='Regression line')

# 添加图例
plt.legend()

# 添加标题和标签
plt.title('Scatter Plot of Four Data Groups')
plt.xlabel('X')
plt.ylabel('Y')

# 显示图形
plt.show()
