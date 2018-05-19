'''
@author：KongWeiKun
@file: bayes.py
@time: 18-5-13 下午9:10
@contact: kongwiki@163.com
'''
"""
朴素贝叶斯
"""
import numpy as np

def loadDataSet():
    postingList = [['my', 'dog', 'has', 'flea', 'problems', 'help', 'please'],
                   ['maybe', 'not', 'take', 'him', 'to', 'dog', 'park', 'stupid'],
                   ['my', 'dalmation', 'is', 'so', 'cute', 'I', 'love', 'him'],
                   ['stop', 'posting', 'stupid', 'worthless', 'garbage'],
                   ['mr', 'licks', 'ate', 'my', 'steak', 'how', 'to', 'stop', 'him'],
                   ['quit', 'buying', 'worthless', 'dog', 'food', 'stupid']]
    classVec = [0, 1, 0, 1, 0, 1]  # 1 is abusive, 0 not
    return postingList, classVec

def createVocabList(dataSet):
    """创建一个包含在所有文档中出现的不重复的列表"""
    vocabSet = set([])
    for document in dataSet:
        vocabSet = vocabSet | set(document)  # 两个集合的并集
    return list(vocabSet)

def setOfWord2Vec(vocabList,inputSet):
    """
    文字转化为数字
    :param vocabList:词汇表 
    :param inputSet: 文档
    :return: returnVec: 文档向量
    """
    returnVec = [0]*len(vocabList) #创建一个所有元素都为0的向量 并且向量的长度与词汇表的长度相同
    for word in inputSet:
        # 若文档中的单词出现在词汇表中 则向量对应的位置置一
        if word in vocabList:
            returnVec[vocabList.index(word)] = 1
        else:
            print('the word: %s is not in my Vocabulary!'%word)
    return returnVec

def trainNB0(trainMatrix,trainCategory):
    """
    
    :param trainMatrix: 
    :param trainCategory: 
    :return: 
    """
    numTrainDocs = len(trainMatrix)
    numWords = len(trainMatrix[0])
    pAbusive = sum(trainCategory)/float(numTrainDocs)
    p0Num = np.zeros(numWords); p1Num = np.zeros(numWords)
    p0Denom = 0.0; p1Denom = 0.0
    for i in range(numTrainDocs):
        if trainCategory[i] == 1:
            p1Num += trainMatrix[i]
            p1Denom += sum(trainMatrix[i])
        else:
            p0Num += trainMatrix[i]
            p0Denom += sum(trainMatrix[i])
    p1Vect = p1Num/p1Denom
    p0Vect = p0Num/p0Denom
    return p0Vect,p1Vect,pAbusive


if __name__ == '__main__':
    listOPosts,listClasses = loadDataSet()
    myVocabList = createVocabList(listOPosts)
    # print(setOfWord2Vec(myVocabList,listOPosts[0]))
    trainMat = []
    for postinDoc in listOPosts:
        trainMat.append(setOfWord2Vec(myVocabList,postinDoc))
    print(trainMat)
    print(len(trainMat))
    print("category",listOPosts)
    print(listClasses)
    print(sum(listClasses))
    p0v,p1v,pAb = trainNB0(trainMat,listClasses)
    print(pAb)