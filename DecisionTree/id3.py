'''
@author：KongWeiKun
@file: id3.py
@time: 18-4-11 下午8:22
@contact: kongwiki@163.com
'''
'''
id3 实现
'''

## 定义节点类 二叉树
class Node:

    def __init__(self,root=True,label=None,feature_name=None,feature=None):
        self.root = root
        self.label = label
        self.feature_name = feature_name
        self.feature = feature
        self.tree = {}
        self.result = {'label':self.label,'feature':self.feature,'tree':self.tree}

    def __repr__(self):
        return '{}'.format(self.result)

    def add_node(self,val,node):
        self.tree[val] = node

    def predict(self,features):
        if self.root is True:
            return self.label
        return self.tree[features[self.feature]].predict(features)

class DTree:

    def __init__(self,epsilon=0.1):
        self.epsilon = epsilon
        self._tree = {}

