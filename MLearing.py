from MachineLearning.Knn import *
import matplotlib
import matplotlib.pyplot as plt
import numpy as np

knn = Knn()
'''
group, labels = knn.createDateSet()
a = knn.classify0([0, 0], group, labels, 4)
print(a)
'''


def datingClassTest():
    horatio = 0.10
    datingDigMat, classLabels = knn.fileLoadMatrix('datingTestSet.txt')
    normDataSet, ranges, minValues = knn.autoNorm(datingDigMat)
    m = normDataSet.shape[0]
    numTestVecto = int(m * horatio)
    errorCount = 0.0
    for i in range(numTestVecto):
        classifiterResult = knn.classify0(normDataSet[i, :], normDataSet[numTestVecto:m, :],
                                          classLabels[numTestVecto:m],
                                          3)
        print('the classfiter came back with %d , the real answer is %d ' % (classifiterResult, classLabels[i]))
        if classifiterResult != classLabels[i]:
            errorCount += 1.0
    print('the total error rate is %f' % (errorCount / float(numTestVecto)))

    fig = plt.figure()
    ax = fig.add_subplot(111)
    # ax.scatter(returnMat[:, 1], returnMat[:, 2])
    ax.scatter(normDataSet[:, 1], normDataSet[:, 2], 15.0 * np.array(classLabels), 15.0 * np.array(classLabels))
    plt.show()


datingClassTest()
