# coding=utf-8
import numpy as np
import operator


class Knn(object):
    def __init__(self):
        pass

    # 样本数据集
    def createDateSet(self):
        group = np.array([[1.0, 1.1], [1.0, 1.0], [0, 0.1], [0, 0.0]])
        labels = ['A', 'A', 'B', 'B']
        return group, labels

    # 数据分类方法
    def classify0(self, inx, dataSet, labels, k):
        # 读取样本数据集的行数
        dataSetSize = dataSet.shape[0]
        # 将要分类的数据复制4行一列，与样本数据进行相减运算
        diffMat = np.tile(inx, (dataSetSize, 1)) - dataSet
        sqDiffMat = diffMat ** 2
        # axis=1 表示行向
        sqDistances = sqDiffMat.sum(axis=1)
        distances = sqDistances ** 0.5
        # 将计算出的数据，根据数据索引进行从小到大排序
        sortDistIndcies = distances.argsort()
        # 建立一个空的字典
        classCount = {}
        for i in range(k):
            # 从小到大从计算结果中取值取值
            sortd = sortDistIndcies[i]
            # 取出标签中的对应值
            votaIlabel = labels[sortd]
            c = classCount.get(votaIlabel, 0)
            classCount[votaIlabel] = c + 1
        # sorted(iterable, cmp, key=None, reverse=False)
        # iterable：指定为要排序的list或iterable对象
        # reverse：是一个bool变量，表示升序还是降序排列，默认为false(升序排列)，定义为True时表示降序排列
        # operator模块提供的itemgetter函数用于获取对象的哪些维的数据，参数为一些序号（即需要获取的数据在对象中的序号）
        sortedClassCount = sorted(classCount.items(), key=operator.itemgetter(1), reverse=True)
        return sortedClassCount[0][0]

    # 文件读取方法
    def fileLoadMatrix(self, fileName):
        f = open(fileName)
        arrayOlines = f.readlines()
        numberOfLines = len(arrayOlines)
        returnMat = np.zeros((numberOfLines, 3))
        classLabelVector = []
        index = 0
        for line in arrayOlines:
            line = line.strip()
            listFormLine = line.split('\t')
            returnMat[index, :] = listFormLine[0:3]
            classLabelVector.append(int(listFormLine[-1]))
            index += 1
        return returnMat, classLabelVector

    # 归一化数据集 将数据处理在（0,1）之间
    def autoNorm(self, dataSet):
        # min(0) 表示从列向求最小值
        minValues = dataSet.min(0)
        maxValues = dataSet.max(0)
        ranges = maxValues - minValues
        normDataSet = np.zeros(np.shape(dataSet))
        m = dataSet.shape[0]
        normDataSet = dataSet - np.tile(minValues, (m, 1))
        normDataSet = normDataSet / np.tile(ranges, (m, 1))
        return normDataSet, ranges, minValues
