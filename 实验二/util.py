from numpy import *

#产生数据集
#在(x-x0)^2+(y-y0)^2 <= r^2 的圆内取n个点

def pts_circle(x0, y0, r, n, seq,filename):
    #在单位圆内随机取n个点
    t = random.random(size=n) * 2 * pi
    len = random.random(size=n)
    x = r * len * cos(t) + x0
    y = r * len * sin(t) + y0
    f = open(filename, 'a')
    for i in range(n):
        txt = str(x[i]) + '\t' + str(y[i]) + '\t' + str(seq) + '\n'
        f.write(txt)
    f.close()
    return (x, y)


#加载数据集，按tab分割
def loadDataSet(fileName):
    dataSet = []#行数为样本数，列数为样本维度
    f = open(fileName, 'r')
    for line in f.readlines():
        current = line.strip().split('\t')
        dataSet.append(list(map(float, current)))
    return dataSet

#计算两向量的欧式距离的平方
def dist2(vecA, vecB):
    return sum(power((vecA - vecB), 2))

#选取c个初始聚合中心
def Cent_Rand(dataSet, c):
    n = shape(dataSet)[1] #维度
    centroids = mat(zeros([c, n]))
    for j in range(n):
        minj = min(dataSet[:, j])
        maxj = max(dataSet[:, j])
        rangej = float(maxj - minj)
        centroids[:, j] = mat(minj + rangej * random.rand(c, 1))
    #print(centroids)
    return centroids

def Cent_Aver(dataSet, c):
    n = shape(dataSet)[1]  # 维度
    M = shape(dataSet)[0]
    centroids = mat(zeros([c, n]))

    cent1 = array([[0,0]])
    cent2 = array([[0,0]])
    for j in range(M):
        p = random.rand()
        if p > 1/c:
            cent1 = append(cent1, [dataSet.A[j]], axis=0)
        else:
            cent2 = append(cent2, [dataSet.A[j]], axis=0)
    cent1 = delete(cent1, 0, axis=0)
    cent1 = delete(cent1, 0, axis=0)
    centroids[0, :] = mean(mat(cent1), axis=0)
    centroids[1, :] = mean(mat(cent2), axis=0)
    #print("Cent_Aver:")
    #print(centroids)
    return centroids


def Cent_Start(dataSet, c):
    n = shape(dataSet)[1]
    #选前c个样本点作为初始聚合中心
    centroids = mat(zeros([c, n]))
    for i in range(c):
        centroids[i, :] = dataSet[i, :]
    print("Cent_Start:")
    print(centroids)
    return centroids


def CMeans(dataSet, c, distMeans=dist2, createCent=Cent_Aver):
    M = shape(dataSet)[0] #样本数
    cluster = mat(zeros([M, 2])) #m行2列的矩阵，第一列存放该样本属于的类别，第二列存放数据到中心的距离
    centroids = createCent(dataSet, c)
    flag = True #表示聚类在迭代后是否发生变化
    iter = 0
    while flag:
        flag = False
        iter += 1
        for i in range(M):  #把M个样本点分到里其最近的中心
            minDist = inf
            minIndex = -1
            for j in range(c):
                distJ = distMeans(dataSet[i, :], centroids[j, :])
                if distJ < minDist:
                    minDist = distJ
                    minIndex = j
            if cluster[i, 0] != minIndex:
                flag = True  #分类发生变化，需要继续迭代
            cluster[i, :] = minIndex, minDist

        #重新计算聚合中心
        for cent in range(c):
            ptsInClust = dataSet[nonzero(cluster[:, 0].A == cent)[0]] #提取每一类中的样本
            centroids[cent, :] = mean(ptsInClust, axis=0) #计算更新中心点
        #print("迭代次数:" + str(iter))
        #print("聚合中心:")
        #print(centroids)
    return centroids, cluster


def Bin_CMeans(dataSet, c, distMeans=dist2):
    M = shape(dataSet)[0] #样本数

    #初始化第一个聚类中心
    centroid0 = mean(dataSet, axis=0).tolist()[0]
    centList = [centroid0]
    cluster = mat(zeros([M, 2]))  # m行2列的矩阵，第一列存放该样本对应的聚类中心，第二列存放数据到中心的距离的平方
    for j in range(M):
        cluster[j, 1] = distMeans(centroid0, dataSet[j, :])
    #依次生成c个聚类中心
    while(len(centList)<c):
        lowestSSE = inf
        for i in range(len(centList)):
            pts_Curr_Cluster = dataSet[nonzero(cluster[:, 0].A == i)[0], :]
            #应用c=2的C_Means
            centroidMat, splitCluster = CMeans(pts_Curr_Cluster, 2)
            SSE_split = sum(splitCluster[:, 1])
            SSE_not_split = sum(cluster[nonzero(cluster[:, 0].A != i)[0], 1])
            if SSE_split + SSE_not_split < lowestSSE:
                bestCentTosplit = i
                bestNewCents = centroidMat
                bestClustAss = splitCluster.copy()
                lowestSSE = SSE_not_split + SSE_split
        #转换类别，类别为1->下一类，类别为0->当前类
        bestClustAss[nonzero(bestClustAss[:, 0].A == 1)[0], 0] = len(centList)
        bestClustAss[nonzero(bestClustAss[:, 0].A == 0)[0], 0] = bestCentTosplit

        #替换中心点
        centList[bestCentTosplit] = bestNewCents[0, :].tolist()[0]
        centList.append(bestNewCents[1, :].tolist()[0])
        #
        cluster[nonzero(cluster[:, 0].A == bestCentTosplit)[0], :] = bestClustAss

    return mat(centList), cluster