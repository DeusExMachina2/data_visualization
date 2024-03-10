# 20214519-马煜辉-第一次作业
要求分析
作业任务1：
设计或开发工作：
用可视化软件或工具（包括但不限于Tableau，Excel，Weka，Weave）对课程第1讲教学内容中所涉及的Anscombe's quartet数据集进行分析，将四组数据进行可视化；
提示：
每组数据可以单独用1个散点图，最后生成4个散点图；
请注意图表的设置，配色要美观；
尝试使用1个散点图，对每组数据使用不同的颜色进行编码；
文字阐述工作：
根据你自己的知识来说明这四组数据的分布特征；
提示：
可以结合均值、方差、相关系数等统计特征进行分析；引用必要的文献；给出必要的公式；
结合这个任务，用适当文字阐述数据可视化的意义和价值；
作业任务2：
用脚本语言或编程语言，计算四组数据的最小二乘法回归线方程；
提示：
请将代码贴入到石墨文档，使用【插入】—【</>代码块】方式；
简单描述自己使用的脚本语言或编程语言类型；
给出计算结果，并进行相应的阐述；查阅和引用相关资料，阐述最小二乘法回归线方程的相关知识；可以使用【插入】—【Tex数学公式】的组件来编辑可能出现的数学公式或特殊的符号变量。
数据集：
任务1.
1.生成四个散点图
使用python的matplotlib.pyplot进行绘图，代码如下
import matplotlib.pyplot as plt
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
plt.scatter(s['X'], s['Y_D1'], color='red', label='Y_D1')
plt.scatter(s['X'], s['Y_D2'], color='blue', label='Y_D2')
plt.scatter(s['X'], s['Y_D3'], color='green', label='Y_D3')
plt.scatter([8]*11, s['Y_D4'], color='purple', label='Y_D4')
# 添加图例
plt.legend()
# 添加标题和标签
plt.title('Scatter Plot of Four Data Groups')
plt.xlabel('X')
plt.ylabel('Y')
# 显示图形
plt.show()
# 多个散点图
# 创建4个子图
fig, axs = plt.subplots(4, 1, figsize=(8, 12))
# 绘制每个子图
for i, key in enumerate(['Y_D1', 'Y_D2', 'Y_D3', 'Y_D4']):
    if key == 'Y_D4':
        s['X'] = [8]*11
    axs[i].scatter(s['X'], s[key], label=key)
    axs[i].set_title(f'Scatter Plot of {key}')
    axs[i].set_xlabel('X')
    axs[i].set_ylabel('Y')
    axs[i].legend()
# 调整子图之间的间距
plt.tight_layout()
# 显示图形
plt.show()
图片: https://uploader.shimo.im/f/W3v4Xs0w9YvhJp9i.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MTAwNjM3NzUsImZpbGVHVUlEIjoiQjFBd2RFbU9nblN2QkczbSIsImlhdCI6MTcxMDA2MzQ3NSwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjo5MTEyNDIwNX0.FmtIyvouSZF0LFb5wl9Rsnd0z68N0Am9ldjWsgDHa9Q
2.生成单个散点图
图片: https://uploader.shimo.im/f/jF8LJds70eVF1rCl.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MTAwNjM3NzUsImZpbGVHVUlEIjoiQjFBd2RFbU9nblN2QkczbSIsImlhdCI6MTcxMDA2MzQ3NSwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjo5MTEyNDIwNX0.FmtIyvouSZF0LFb5wl9Rsnd0z68N0Am9ldjWsgDHa9Q
形状和统计量描述
平均值计算：
数学公式: $ x_{mean}=\sum_{0}^{n}{x_{n}}\div n $
方差计算：
数学公式: $ x_{var}=\sum_{0}^{n}(x_{n}-x_{mean})^2/（n-1） $
相关系数计算：
数学公式: $ p_{xy}=\frac{\sum_{0}^{n}((x_{n}-x_{mean}) \times (y_{n}-y_{mean})}{\sqrt x_{var}\times \sqrt y_{var}\times n} $
对于1组：
可以看到1组的数据基本上是符合一个线性关系的。通过我们上面公式的计算可以得到其
数学公式: $ x_{mean}=9.0 $
数学公式: $ y_{mean}=7.5 $
数学公式: $ x_{var}=11.0 $
数学公式: $ y_{var}=4.127 $
对于相关系数，用热力矩阵给出
图片: https://uploader.shimo.im/f/DY1cvKbbkjDk3mxb.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MTAwNjM3NzUsImZpbGVHVUlEIjoiQjFBd2RFbU9nblN2QkczbSIsImlhdCI6MTcxMDA2MzQ3NSwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjo5MTEyNDIwNX0.FmtIyvouSZF0LFb5wl9Rsnd0z68N0Am9ldjWsgDHa9Q
对于2组：
观测可以看出，其更加近似于一个二次函数，并非是一个线性的，但是当我们计算其几个常用的统计量的时候，我们可以得到
数学公式: $ x_{mean}=9.0 $
数学公式: $ y_{mean}=7.5 $
数学公式: $ x_{var}=11.0 $
数学公式: $ y_{var}=4.127 $
这与第一组是完全一样的 ，甚至包括了相关系数。所以说相关系数，好像也不是这么的能刻画线性相关。

图片: https://uploader.shimo.im/f/DY1cvKbbkjDk3mxb.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MTAwNjM3NzUsImZpbGVHVUlEIjoiQjFBd2RFbU9nblN2QkczbSIsImlhdCI6MTcxMDA2MzQ3NSwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjo5MTEyNDIwNX0.FmtIyvouSZF0LFb5wl9Rsnd0z68N0Am9ldjWsgDHa9Q
对于3组：
观测可以看出其是有异常点的线性相关，如果删除哪一个过度偏离的点那么相关系数应该接近于1
其统计量如下
数学公式: $ x_{mean}=9.0 $
数学公式: $ y_{mean}=7.5 $
数学公式: $ x_{var}=11.0 $
数学公式: $ y_{var}=4.127 $
图片: https://uploader.shimo.im/f/DY1cvKbbkjDk3mxb.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MTAwNjM3NzUsImZpbGVHVUlEIjoiQjFBd2RFbU9nblN2QkczbSIsImlhdCI6MTcxMDA2MzQ3NSwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjo5MTEyNDIwNX0.FmtIyvouSZF0LFb5wl9Rsnd0z68N0Am9ldjWsgDHa9Q
对于四组。
如果删去离群的点，那么x的值，就没有随着y的值的变化而变化,也就是说不相关
总结
通过可视化展示这些数据，可以让我们更直观快速的发现每组数据的特点，让发现数据中的规律变得容易
任务2.
最小二乘法公式如下
数学公式: $ 拟合直线:y=ax+b $
数学公式: $ a=\frac{\Sigma(x_{i}-x_{mean})(y_{i}-y_{mean})}{\Sigma(x_{i}-x_{mean})^{2}} $
数学公式: $ b=y_{mean}-a\times x_{mean} $
代码如下
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
发现拟合的直线是一样的，如下
图片: https://uploader.shimo.im/f/Sshni6JFef3mG0t5.png!thumbnail?accessToken=eyJhbGciOiJIUzI1NiIsImtpZCI6ImRlZmF1bHQiLCJ0eXAiOiJKV1QifQ.eyJleHAiOjE3MTAwNjM3NzUsImZpbGVHVUlEIjoiQjFBd2RFbU9nblN2QkczbSIsImlhdCI6MTcxMDA2MzQ3NSwiaXNzIjoidXBsb2FkZXJfYWNjZXNzX3Jlc291cmNlIiwidXNlcklkIjo5MTEyNDIwNX0.FmtIyvouSZF0LFb5wl9Rsnd0z68N0Am9ldjWsgDHa9Q
方程为 y = 0.5x + 3
