from util import *
import matplotlib.pyplot as plt
import cv2
def find_point(point):
    int_x = int(ceil(point[0]) * (point[0] >= 0) + floor(point[0]) * (point[0] <= 0))
    int_y = int(ceil(point[1]) * (point[1] >= 0) + floor(point[1]) * (point[1] <= 0))
    return [int_x, int_y]

def graph(dataSet, cluster, centroids, method):
    plt.subplot(2, 1, method)
    plt.ylim(-3.5, 6.5)
    M = shape(dataSet)[0]  #M个样本点
    #画点
    legend_flag1 = False
    legend_flag2 = False
    for i in range(M):
        point = dataSet[i, :].A[0]
        x = point[0]
        y = point[1]
        mytype = point[2]
        if mytype == 1:
            if legend_flag1:
                plt.scatter(x, y, c='b')
            else:
                legend_flag1=True
                plt.scatter(x, y, c='b', label='Type1(actual)')
        elif mytype == 2:
            if legend_flag2:
                plt.scatter(x, y, c='g')
            else:
                legend_flag2=True
                plt.scatter(x, y, c='g', label='Type2(actual)')
            plt.scatter(x, y, c='g')
    #标注聚类中心 和聚类最大误差
    c = shape(centroids)[0]  #c个聚类中心
    for i in range(c):
        point = centroids[i, :].A[0]  #第i类的聚类中心
        x = point[0]
        y = point[1]
        name = 'center' + str(i + 1)
        if i == 0:
            plt.scatter(x, y, marker='x', c='r', s=30, label=name)
        elif i == 1:
            plt.scatter(x, y, marker='D', c='r', s=30, label=name)


    #画点集凸包
    calSet = (delete(dataSet[:], -1, axis=1)).A #点集坐标
    axis_list0 = array([[centroids.A[0][0], centroids.A[0][1]]])
    axis_list1 = array([[centroids.A[1][0], centroids.A[1][1]]])
    for i in range(M):
        if cluster.A[i][0] == 0: #第i个样本被分类为类型0
            axis_list0 = append(axis_list0, [calSet[i]], axis=0)
        elif cluster.A[i][0] == 1: #类型1
            axis_list1 = append(axis_list1, [calSet[i]], axis=0)
    axis_list0 = array(list(map(find_point, axis_list0)))
    axis_list1 = array(list(map(find_point, axis_list1)))

    hull0 = cv2.convexHull(axis_list0, clockwise=True, returnPoints=True)
    hull0 = squeeze(hull0)
    plt.plot(hull0[:, 0], hull0[:, 1], 'b')
    plt.plot([hull0[-1,0], hull0[0,0]], [hull0[-1,1], hull0[0,1]], 'b', label='Type1(judge)')

    hull1 = cv2.convexHull(axis_list1, clockwise=True, returnPoints=True)
    hull1 = squeeze(hull1)
    plt.plot(hull1[:, 0], hull1[:, 1], 'g')
    plt.plot([hull1[-1, 0], hull1[0, 0]], [hull1[-1, 1], hull1[0,1]], 'g', label='Type2(judge)')


    if method == 1:
        plt.title('Cent_Aver')
    elif method == 2:
        plt.title('Cent_Start')

    plt.legend(loc=0, ncol=3)

    return


def graph2(dataSet, cluster, centroids, method):
    plt.subplot(2, 1, method)
    M = shape(dataSet)[0]  #M个样本点
    #画点
    legend_flag1 = False
    legend_flag2 = False
    legend_flag3 = False
    legend_flag4 = False
    for i in range(M):
        point = dataSet[i, :].A[0]
        x = point[0]
        y = point[1]
        mytype = point[2]
        if mytype == 1:
            if legend_flag1:
                plt.scatter(x, y, c='b')
            else:
                legend_flag1=True
                plt.scatter(x, y, c='b', label='Type1(actual)')
        elif mytype == 2:
            if legend_flag2:
                plt.scatter(x, y, c='g')
            else:
                legend_flag2=True
                plt.scatter(x, y, c='g', label='Type2(actual)')
            plt.scatter(x, y, c='g')
        elif mytype == 3:
            if legend_flag3:
                plt.scatter(x, y, c='y')
            else:
                legend_flag3=True
                plt.scatter(x, y, c='y', label='Type3(actual)')
            plt.scatter(x, y, c='y')
        elif mytype == 4:
            if legend_flag4:
                plt.scatter(x, y, c='m')
            else:
                legend_flag4=True
                plt.scatter(x, y, c='m', label='Type4(actual)')
            plt.scatter(x, y, c='m')
    #标注聚类中心 和聚类最大误差
    c = shape(centroids)[0]  #c个聚类中心
    for i in range(c):
        point = centroids[i, :].A[0]  #第i类的聚类中心
        x = point[0]
        y = point[1]
        name = 'center' + str(i + 1)
        if i == 0:
            plt.scatter(x, y, marker='x', c='r', s=50, label=name)
        elif i == 1:
            plt.scatter(x, y, marker='D', c='r', s=50, label=name)
        elif i == 2:
            plt.scatter(x, y, marker='^', c='r', s=50, label=name)
        elif i == 3:
            plt.scatter(x, y, marker='v', c='r', s=50, label=name)
    '''
    #画点集凸包
    calSet = (delete(dataSet[:], -1, axis=1)).A #点集坐标
    axis_list0 = array([[centroids.A[0][0], centroids.A[0][1]]])
    axis_list1 = array([[centroids.A[1][0], centroids.A[1][1]]])
    for i in range(M):
        if cluster.A[i][0] == 0: #第i个样本被分类为类型0
            axis_list0 = append(axis_list0, [calSet[i]], axis=0)
        elif cluster.A[i][0] == 1: #类型1
            axis_list1 = append(axis_list1, [calSet[i]], axis=0)
    axis_list0 = array(list(map(find_point, axis_list0)))
    axis_list1 = array(list(map(find_point, axis_list1)))

    hull0 = cv2.convexHull(axis_list0, clockwise=True, returnPoints=True)
    hull0 = squeeze(hull0)
    plt.plot(hull0[:, 0], hull0[:, 1], 'b')
    plt.plot([hull0[-1,0], hull0[0,0]], [hull0[-1,1], hull0[0,1]], 'b', label='Type1(judge)')

    hull1 = cv2.convexHull(axis_list1, clockwise=True, returnPoints=True)
    hull1 = squeeze(hull1)
    plt.plot(hull1[:, 0], hull1[:, 1], 'g')
    plt.plot([hull1[-1, 0], hull1[0, 0]], [hull1[-1, 1], hull1[0,1]], 'g', label='Type2(judge)')
    
    if method == 1:
        plt.title('CMeans')
    elif method == 2:
        plt.title('Bin-CMeans')
    '''
    #plt.legend(loc=0, ncol=3)
    if method == 1:
        plt.title('')
    elif method == 2:
        plt.title('')

    return


if __name__ == '__main__':
    #setName = 'type1'
    #数据产生，需要根据需求先运行该部分代码
    #pts_circle(3, 3, 1.5, 100, 1, setName)
    #pts_circle(3, 8, 1.5, 10, 2, setName)
    #pts_circle(8, 1, 1.5, 10, 3, setName)
    #pts_circle(10, 6, 1.5, 100, 4, setName)

    fig = plt.figure()
    plt.subplots_adjust(left=0.04, top=0.96, right=0.96, bottom=0.04, wspace=0.01, hspace=0.5)
    plt.figure(figsize=(8, 8))
    dataSet = mat(loadDataSet('type1'))
    calSet = delete(dataSet[:], -1, axis=1)
    centroids, cluster = CMeans(calSet, 4, createCent=Cent_Rand) #取样本平均值作为聚合中心
    graph2(dataSet, cluster, centroids, 1)

    dataSet = mat(loadDataSet('type2'))
    calSet = delete(dataSet[:], -1, axis=1)
    centroids, cluster = CMeans(calSet, 4, createCent=Cent_Rand)  # 取样本平均值作为聚合中心
    graph2(dataSet, cluster, centroids, 2)

    #plt.savefig('cmp2.svg')
    plt.show()



    '''
    dataSet = mat(loadDataSet(setName))
    calSet = delete(dataSet[:], -1, axis=1)
    centroids, cluster = CMeans(calSet, 4, createCent=Cent_Rand) #取样本平均值作为聚合中心
    graph(dataSet, cluster, centroids, 1)


    #centroids, cluster = CMeans(calSet, 2, createCent=Cent_Start) #取前两个样本作为聚合中心
    graph(dataSet, cluster, centroids, 2)
    #plt.savefig('1.svg')
    plt.show()
    '''

    '''
    dataSet = mat(loadDataSet(setName))
    calSet = delete(dataSet[:], -1, axis=1)
    centroids, cluster = CMeans(calSet, 4, createCent=Cent_Rand)
    graph2(dataSet, cluster, centroids, 1)
    centroids, cluster = Bin_CMeans(calSet, 4)
    graph2(dataSet, cluster, centroids, 2)
    plt.savefig(setName + '.svg')
    plt.show()
    '''
