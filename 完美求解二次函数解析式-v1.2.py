try:
    import matplotlib.pyplot as plt          # 导入matplotlib用于绘图
    import numpy as np                       # numpy库用于科学计算
    from fractions import Fraction as fa     # 用于显示分数
except ModuleNotFoundError as error:
    print(error)
    import os
    m = str(error).split("\'")[1]
    path = os.environ['path']
    python_path = None
    print(path)
    if r'C:\Pyblock\resources\app\Python-win64' in path:
        os.system(
            r"pip install --target=C:\Users\Administrator\.wood\libs_x64 {}".format(m))
    else:
        os.system("pip install {}".format(m))


# 求解type1
def solve_type1():
    # 全局变量a, b, c, 作用类似于return
    global a, b, c
    # 若输入存在错误，不用手动重开程序，自动循环再次获取输入
    while True:
        x_collect = []      # 存放搜集到的点的x坐标数据
        y_collect = []      # 存放搜集到的点的y坐标数据
        num = input("请输入a, b, c中已知数量（0，1，2）:")
        if num == '0':
            '''
            for i in range(1, 4):
                x_collect.append(
                    fa(float(input("请输入第{}个点坐标的横坐标(x)：".format(i)))))
                y_collect.append(
                    fa(float(input("请输入第{}个点坐标的纵坐标(y)：".format(i)))))
            # y_collect[0]=a(x_collect[0]^2)+bx_collect[0]+c
            # y_collect[1]=a(x_collect[1]^2)+bx_collect[1]+c
            # y_collect[2]=a(x_collect[2]^2)+bx_collect[2]+c
            '''
            print('当前版本尚不支持，等待后续优化')
            input("按回车键退出程序")
            break
        elif num == '1':
            collect_1 = input('''请输入已知量:
            e.g.:a 1 (两个量中使用空格隔开)：''').split(" ")
            # 输入错误处理
            if collect_1[0] != 'a' and collect_1[0] != 'b' and collect_1[0] != 'c':
                print("请输入符合规则的字符")
                continue
            # 数据采集
            for i in range(1, 3):
                x_collect.append(
                    fa(float(input("请输入第{}个点坐标的横坐标(x)：".format(i)))))
                y_collect.append(
                    fa(float(input("请输入第{}个点坐标的纵坐标(y)：".format(i)))))
            # 已知量为a
            if collect_1[0] == 'a':
                a = fa(float(collect_1[1]))
                b = fa(float(y_collect[1] - y_collect[0] -
                    a*(x_collect[1]+x_collect[0])))
                c = fa(float(y_collect[0] - a *
                    (x_collect[0]**2) - b*x_collect[0]))
                break
            # 已知量为b
            elif collect_1[0] == 'b':
                b = fa(float(collect_1[1]))
                a = fa(float((y_collect[1]-y_collect[0]-b) /
                    (x_collect[1]+x_collect[0])))
                c = fa(float(y_collect[0] - a *
                    (x_collect[0]**2) - b*x_collect[0]))
                break
            # 已知量为c
            elif collect_1[0] == 'c':
                c = fa(float(collect_1[1]))
                a_temp = (x_collect[1]*(y_collect[0]-c)-x_collect[0]*(y_collect[1]-c)) / \
                    (x_collect[1]*(x_collect[0]**2)-x_collect[0]*(x_collect[1]**2))
                a = fa(float(a_temp))
                b_temp = ((y_collect[1]-c)*(x_collect[0]**2)-(y_collect[0]-c)*(x_collect[1]**2))/ \
                    (x_collect[1]*(x_collect[0]**2)-x_collect[0]*(x_collect[1]**2))
                b = fa(float(b_temp))
                break
            # 输入错误处理
            else:
                print("请输入符合规则的字符")
        elif num == '2':
            i = 1
            collect_2 = []
            collect_3 = []
            num_list = [str(i) for i in range(10)]
            while i <= 2:
                _collect = input('''请输入第{}个已知量:
                    e.g.:a 1 (两个量中使用空格隔开)：'''.format(i)).split(" ")
                collect_3.append(_collect)
                # 输入错误处理
                if len(collect_3[i - 1]) != 2:
                    print("请输入符合规则的字符")
                    collect_3.pop(i - 1)
                    continue
                if collect_3[i - 1][0] != 'a' and collect_3[i - 1][0] != 'b' and collect_3[i - 1][0] != 'c':
                    print("请输入符合规则的字符")
                    collect_3.pop(i - 1)
                    continue
                if collect_3[i - 1][1] not in num_list:
                    print("请输入符合规则的字符")
                    collect_3.pop(i - 1)
                    continue
                if i == 2:
                    if collect_3[1][0] in collect_2[0]:
                        print("请不要输入相同的量")
                        collect_3.pop(i - 1)
                        continue
                collect_2.append(_collect)
                i += 1
                print(collect_2)
            x_collect.append(
                    fa(float(input("请输入已知点坐标的横坐标(x)："))))
            y_collect.append(
                    fa(float(input("请输入已知点坐标的纵坐标(y)："))))
            for i in range(2):
                collect_2[i][1] =  int(collect_2[i][1])
            print(collect_2)
            if collect_2[0][0] == 'a':
                a = collect_2[0][1]
                if collect_2[1][0] == 'b':
                    b = collect_2[1][1]
                    c = y_collect[0] - a * \
                        (x_collect[0]**2) - b*x_collect[0]
                    break
                elif collect_2[1][0] == 'c':
                    c = collect_2[1][1]
                    b = (y_collect[0] - a*(x_collect[0]**2)-c) / x_collect[0]
                    break
            elif collect_2[0][0] == 'b':
                b = collect_2[0][1]
                if collect_2[1][0] == 'a':
                    a = collect_2[1][1]
                    c = y_collect[0] - a * \
                        (x_collect[0]**2) - b*x_collect[0]
                elif collect_2[1][0] == 'c':
                    c = collect_2[1][1]
                    a = (y_collect[0]-b*x_collect[0]-c) / x_collect[0]
            elif collect_2[0][0] == 'c':
                c = collect_2[0][1]
                if collect_2[1][0] == 'a':
                    a = collect_2[1][1]
                    b = (y_collect[0] - a*(x_collect[0]**2)-c) / x_collect[0]
                elif collect_2[1][0] == 'b':
                    b = collect_2[1][1]
                    a = (y_collect[0]-b*x_collect[0]-c) / x_collect[0]
            break
        # 输入错误处理
        else:
            print("请输入符合规则的字符")
            continue

# 求解type2
def solve_type2():
    global a, k, h
    while True:
        k = fa(float(input("请输入顶点坐标的横坐标x（e.g.:1）：")))
        h = fa(float(input("请输入顶点坐标的纵坐标y（e.g.:1）：")))
        x = fa(float(input("请输入已知点坐标的横坐标x：")))
        y = fa(float(input("请输入已知点坐标的纵坐标y：")))
        # 输入错误处理
        if y-h == 0 or x-k == 0:
            print("请输入除顶点外的点")
        else:
            a = (y-h) / ((x-k)**2)
            break

# 求解type3
def solve_type3():
    global a, x1, x2
    x1 = fa(float(input("请输入第一个交点的x坐标：")))
    x2 = fa(float(input("请输入第二个交点的x坐标：")))
    x = fa(float(input("请输入已知点坐标的横坐标x：")))
    y = fa(float(input("请输入已知点坐标的纵坐标y：")))
    a = fa(float((y)/((x-x1)*(x-x2))))


# 化简type1的解析式
def huajian_type1():
    global fun
    # 若a为0
    if a == 0:
        if b == 0:
            if c == 0:
                print("该函数不存在，请检查后重试")
                fun = None
            else:
                fun = f"y={c}"
        elif b == 1:
            if c == 0:
                fun = f"y=x"
            elif c > 0:
                fun = f"y=x+{c}"
            elif c < 0:
                fun = f"y=x{c}"
        else:
            if c > 0:
                fun = f"y={b}x+{c}"
            elif c < 0:
                fun = f"y={b}x{c}"
    # 若a为1
    elif a == 1:
        if b == 0:
            if c == 0:
                fun = f"y=x^2"
            elif c > 0:
                fun = f"y=x^2+{c}"
            elif c < 0:
                fun = f"y=x^2{c}"
        elif b == 1:
            if c == 0:
                fun = f"y=x^2+x"
            elif c > 0:
                fun = f"y=x^2+x+{c}"
            elif c < 0:
                fun = f"y=x^2+x{c}"
        elif b > 0:
            if c == 0:
                fun = f"y=x^2+{b}x"
            elif c > 0:
                fun = f"y=x^2+{b}x+{c}"
            elif c < 0:
                fun = f"y=x^2+{b}x{c}"
        elif b < 0:
            if c == 0:
                fun = f"y=x^2{b}x"
            elif c > 0:
                fun = f"y=x^2{b}x+{c}"
            elif c < 0:
                fun = f"y=x^2{b}x{c}"
    # 其他情况
    else:
        if b == 0:
            if c == 0:
                fun = f"y={a}x^2"
            elif c > 0:
                fun = f"y={a}x^2+{c}"
            elif c < 0:
                fun = f"y={a}x^2{c}"
        elif b == 1:
            if c == 0:
                fun = f"y={a}x^2+x"
            elif c > 0:
                fun = f"y={a}x^2+x+{c}"
            elif c < 0:
                fun = f"y={a}x^2+x{c}"
        elif b > 0:
            if c == 0:
                fun = f"y={a}x^2+{b}x"
            elif c > 0:
                fun = f"y={a}x^2+{b}x+{c}"
            elif c < 0:
                fun = f"y={a}x^2+{b}x{c}"
        elif b < 0:
            if c == 0:
                fun = f"y={a}x^2{b}x"
            elif c > 0:
                fun = f"y={a}x^2{b}x+{c}"
            elif c < 0:
                fun = f"y={a}x^2{b}x{c}"   
    if fun != None:
        print("解析式为:"+fun)

# 化简type2
def huajian_type2():
    global fun
    if a == 0:
        if h == 0:
            print("该函数不存在，请检查后重试")
            fun = None
        else:
            fun = f'y={h}'
    elif a == 1:
        if h == 0:
            if k == 0:
                fun = f'x^2'
            elif k > 0:
                fun = f'y=(x-{k})^2'
            elif k < 0:
                fun = f'y=(x+{-k})^2'
        elif h > 0:
            if k == 0:
                fun = f'y=x^2+{h}'
            elif k > 0:
                fun = f'y=(x-{k})^2+{h}'
            elif k < 0:
                fun = f'y=(x+{-k})^2+{h}'
        elif h < 0:
            if k == 0:
                fun = f'y=x^2{h}'
            elif k > 0:
                fun = f'y=(x-{k})^2{h}'
            elif k < 0:
                fun = f'y=(x+{-k})^2{h}'
    else:
        if h == 0:
            if k == 0:
                fun = f'y={a}x^2'
            elif k > 0:
                fun = f'y={a}(x-{k})^2'
            elif k < 0:
                fun = f'y={a}(x+{-k})^2'
        elif h > 0:
            if k == 0:
                fun = f'y={a}x^2+{h}'
            elif k > 0:
                fun = f'y={a}(x-{k})^2+{h}'
            elif k < 0:
                fun = f'y={a}(x+{-k})^2+{h}'
        elif h < 0:
            if k == 0:
                fun = f'y={a}x^2{h}'
            elif k > 0:
                fun = f'y={a}(x-{k})^2{h}'
            elif k < 0:
                fun = f'y={a}(x+{-k})^2{h}'
    if fun != None:
        print("解析式为:"+fun)

# 化简type3
def huajian_type3():
    global fun
    if a == 0:
        print("该函数不存在，请检查后重试")
        fun = None
    elif a == 1:
        if x1 == 0:
            if x2 == 0:
                fun = f'y=x^2'
            elif x2 > 0:
                fun = f'y=x(x-{x2})'
            elif x2 < 0:
                fun = f'y=x(x+{-x2})'
        elif x1 > 0:
            if x2 == 0:
                fun = f'y=x(x-{x1})'
            elif x2 > 0:
                fun = f'y=(x-{x1})(x-{x2})'
            elif x2 < 0:
                fun = f'y=(x-{x1})(x+{-x2})'
        elif x1 < 0:
            if x2 == 0:
                fun = f'y=x(x+{-x1})'
            elif x2 > 0:
                fun = f'y=(x+{-x1})(x-{x2})'
            elif x2 < 0:
                fun = f'y=(x+{-x1})(x+{-x2})'
    else:
        if x1 == 0:
            if x2 == 0:
                fun = f'y={a}(x^2)'
            elif x2 > 0:
                fun = f'y={a}x(x-{x2})'
            elif x2 < 0:
                fun = f'y={a}x(x+{-x2})'
        elif x1 > 0:
            if x2 == 0:
                fun = f'y={a}x(x-{x1})'
            elif x2 > 0:
                fun = f'y={a}(x-{x1})(x-{x2})'
            elif x2 < 0:
                fun = f'y={a}(x-{x1})(x+{-x2})'
        elif x1 < 0:
            if x2 == 0:
                fun = f'y={a}x(x+{-x1})'
            elif x2 > 0:
                fun = f'y={a}(x+{-x1})(x-{x2})'
            elif x2 < 0:
                fun = f'y={a}(x+{-x1})(x+{-x2})'
    if fun != None:
        print("解析式为:"+fun)

# 绘制函数图像
def create_graph(a, b, c, d=-10, e=10):  # d,e分别是x的取值范围
    x = np.arange(d, e, 0.01)
    y = a*(x**2)+b*x+c
    plt.plot(x, y)
    plt.rcParams['font.sans-serif']=['SimHei']  #用来正常显示中文标签
    plt.rcParams['axes.unicode_minus']=False    #用来正常显示负号
    plt.title("解析式为"+fun+"的图像")
    point_x = b / (-2*a)
    point_y = a*(point_x**2)+b*point_x+c
    plt.scatter(point_x, point_y, c='r')
    plt.text(point_x, point_y, f"顶点坐标({point_x},{point_y})",
             fontsize=12, color='r', verticalalignment="top", horizontalalignment="center")
    plt.show()

def main():
    # 类型采集
    Input = input('''请输入二次函数类型：
            \t type1（一般式）:y=ax^2+bx+c      （请输入1）
            \t type2（顶点式）:y=a(x-k)^2+h     （请输入2）
            \t type3（交点式）:y=a(x-x1)(x-x2)  （请输入3）:''')
    while True:
        if Input == '1':
            solve_type1()
            huajian_type1()
            if fun != None:
                create_graph(a, b, c)
                break
        elif Input == '2':
            solve_type2()
            huajian_type2()
            # 化简得y=ax^2-2akx+k^2+h
            if fun != None:
                create_graph(a, -2*a*k, k**2+h)
                break
        elif Input == '3':
            solve_type3()
            huajian_type3()
            # 化简得y=ax^2-a(x2+x1)x+ax1x2
            if fun != None:
                create_graph(a, -a*(x2+x1), a*x1*x2)
                break
        else:
            print("请输入符合规则的字符")
            continue

try:
    main()
except Exception as error:
    import datetime
    d = datetime.datetime.now()
    year, month, day, hour, minute, second = d.year, d.month, d.day, d.hour, d.minute, d.second
    log_name = f"{year}-{month}-{day}-{hour}-{minute}-{second}"
    print(error)
    print(f"""_(¦3」∠)_，程序出错了！请到当前目录下找到{log_name}.log文件
    并反馈给开发者：QQ2330153227，请注明版本""")
    with open(f"{log_name}.log", "w", encoding="utf-8") as f:
        f.write(str(error))
