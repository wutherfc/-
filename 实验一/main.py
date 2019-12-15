import numpy as np
import matplotlib.pyplot as plt
def load_data():
    input_data = [[1,0], [1,1], [0,2], [2,1], [2,2], [1,3]]
    labels = [0, 0, 0, 1, 1, 1]
    return input_data, labels

#线性不可分样本
def load_data2():
    input_data = [[0,0], [1,1], [0,1], [1,0]]
    labels = [0, 0, 1, 1]
    return input_data, labels

def train_pre(input_data, labels,iteration, w0,rate):
    #增值模式
    for (num, label) in enumerate(labels):
        input_data[num].append(1)
        if label == 1:
            for counter, i in enumerate(input_data[num]):
                input_data[num][counter] = -1*(i)
    #print(input_data)

    w = w0
    counter = -1
    error = 0
    for i in range(iteration):
        error = 0
        samples = zip(input_data, labels)
        for (input_i, label)in samples:
            result = input_i*w
            result = float(sum(result))
            if result <= 0:
                w = w + rate*np.array(input_i)
                error = 1
            counter += 1
            #print("迭代次数：%s, 当前权向量：%s" % (counter, w))
        if error == 0:
            print("运算已经收敛，迭代次数：%s" %(counter))
            return w
    print("未收敛，迭代次数：%s" %(counter))
    return w

def graph(w, input_data, labels):
    plt.xlabel("x1")
    plt.ylabel("x2")
    flag_1 = False
    flag_2 = False
    #画散点
    for (data_i, label) in zip(input_data, labels):
        if label == 0:
            if flag_1 == False:
                plt.scatter(data_i[0], data_i[1], s=40, c="red", label='X1')
                flag_1 = True
            else:
                plt.scatter(data_i[0], data_i[1], s=40, c="red")
        elif label == 1:
            if flag_2 == False:
                plt.scatter(data_i[0], data_i[1], s=40, c="blue", label='X2')
                flag_2 = True
            else:
                plt.scatter(data_i[0], data_i[1], s=40, c="blue")
    #画判别函数
    x = np.linspace(-0.5,1.5,100)
    y = np.linspace(-0.5,1.5,100)
    x, y = np.meshgrid(x,y)
    f = w[0]*x + w[1]*y + w[2]
    plt.contour(x, y, f, 0)
    plt.legend()


if __name__ == '__main__':
    fig = plt.figure()
    plt.subplots_adjust(left=0.04, top=0.96, right=0.96, bottom=0.04, wspace=0.4, hspace=0.5)
    plt.figure(figsize=(12, 12))
    input_data, labels = load_data()
    compute_data = []
    for each in input_data:
        compute_data.append(each[:])
    w0 = np.ones(len(input_data[0]) + 1)  # 初始权向量

    rate = 0.01
    # type1
    print('输入样本：%s' % (compute_data))
    print('样本类别：%s' % (labels))
    w0 = np.array([1, 1, 1])
    w = train_pre(compute_data, labels, 2500, w0, rate)
    plt.title('Max iterations = 10000')
    graph(w, input_data, labels)

    print('初始权向量：%s，变化率：%s' % (w0, rate))
    print('分界面方程：%s*x1+%s*x2+%s' % (w[0], w[1], w[2]))
    print('\n')

    plt.show()


