from scipy.cluster.hierarchy import *
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import os


mat = np.load('data/matrix.npy')
methods = {'single':'hamming',
           'complete':'hamming',
           'average':'hamming',
           'ward':'euclidean' }


class HierBicluster(object):
    '''
    
    '''
    def __init__(self, mat, method, metric):
        self.mat = mat
        self.method = method
        self.metric = metric
        self.ZR = linkage(mat, method, metric)
        self.ZC = linkage(np.transpose(mat),method, metric)
        self.hR = np.unique(self.ZR[:,2])
        self.hC = np.unique(self.ZC[:,2])

        # self.hR = np.append([0.0],np.unique(self.ZR[:,2]))
        # self.hC = np.append([0.0],np.unique(self.ZC[:,2]))

        # self.hR = self._getHeight(np.unique(self.ZR[:,2]))
        # self.hC = self._getHeight(np.unique(self.ZC[:,2]))

    # def _getHeight(self, arr):
    # 	return arr if arr[0] else arr[1:]

    def row_clustersByHeight(self,hei):
    	cutree = cut_tree(self.ZR, height = hei)
    	clus = []
    	labels = np.unique(cutree)
    	for label in labels:
    		l = np.where(cutree == label)[0]
    		if len(l) > 1:
    			clus.append(l)
    	return clus

    def column_clustersByHeight(self,hei):
    	cutree = cut_tree(self.ZC, height = hei)
    	clus = []
    	labels = np.unique(cutree)
    	for label in labels:
    		l = np.where(cutree == label)[0]
    		if len(l) > 1:
    			clus.append(l)
    	return clus


    def bi_ByHeights(self,rh,ch):
    	r_clus = self.row_clustersByHeight(rh)
    	c_clus = self.column_clustersByHeight(ch)
    	rows = {f"[{','.join(map(str, clus))}]" : clus for clus in r_clus}
    	cols = {f"[{','.join(map(str, clus))}]" : clus for clus in c_clus}
    	return rows,cols

    def oneRation_ByHeights(self,rh,ch):
    	rows,cols = self.bi_ByHeights(rh,ch)
    	# mat = np.empty((len(rows),len(cols)))
    	df = pd.DataFrame(np.empty((len(rows),len(cols))), 
    			index=rows.keys(),columns=cols.keys())
    	for row in rows.keys():
    		for col in cols.keys():
    			submat = self.mat[rows[row]][:,cols[col]]
    			count = np.count_nonzero(submat==0)
    			df.loc[row,col] = 1 - float(count) / float(submat.size)

    	return df


    def __repr__(self):
    	return self.method



if __name__ == "__main__":
	clus = HierBicluster(mat,'single','hamming')
	print(clus.hR)
	print(clus.row_clustersByHeight(clus.hR[1]))
	print(clus.column_clustersByHeight(clus.hC[1]))

	print(clus.oneRation_ByHeights(clus.hR[1],clus.hC[1]))


