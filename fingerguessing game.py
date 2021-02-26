# 石头剪刀布

import random  # 导入随机数
cpu = random.randint(1, 3)  # 生成电脑伸出结果的变量

playerin = input("请输入要出石头(1)剪刀(2)还是布(3)")

while True:  # 判断玩家输入
    if playerin == '1' or playerin == '2' or playerin == '3':
        break
    else:
        playerin = input("不能输入除了\"1 2 3\"之外的东西哦，请输入要出石头(1)剪刀(2)还是布(3)")

player = int(playerin)

# 判断并显示电脑输入
if cpu == 1:
    cpuout = '石头'
elif cpu == 2:
    cpuout = '剪刀'
else:
    cpuout = '布'
print('电脑伸出的是' + cpuout)

win = 0  # 初始化赢家变量  0：平局  1：玩家胜  2：电脑胜

# 判断赢家
if player == cpu:
    print('平局')
elif player == 1 and cpu == 2:
    win = 1
elif player == 1 and cpu == 3:
    win = 2
elif player == 2 and cpu == 1:
    win = 2
elif player == 2 and cpu == 3:
    win = 1
elif player == 3 and cpu == 1:
    win = 1
elif player == 3 and cpu == 2:
    win = 2
else:
    pass

# 显示赢家
if win == 2:
    print('电脑获胜')
elif win == 1:
    print('玩家获胜')
else:
    pass
