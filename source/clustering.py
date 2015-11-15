from cluster.method.hierarchical import HierarchicalClustering
from cluster.method.kmeans import KMeansClustering
import numpy as np
import math
from Prediction import Prediction
from lib import FunctionLib
import scipy.cluster.hierarchy
import scipy.spatial.distance
import datetime

class HClustering(object):
    def makeClusters(self,IncomingDict,grid,decision,threshold,old_wt):
        #print "Incoming Dict : " ,IncomingDict

        nxtCells = []
        noneCells =[]
        cnt = 0
        for trajID in IncomingDict:
            #Adding the cells to a list to be clustered
            nxtCell = IncomingDict[trajID].get('nextKey')
            weight = IncomingDict[trajID].get('weight')
            #noneCells.append(nxtCell)
            if nxtCell is not None and weight > 4.0:
                x = int(nxtCell%4456)
                y = int(nxtCell/4456)
                nxtCells.append((x,y))
                #nxtCells.append(nxtCell)
                cnt = cnt +1
        #print "Next Cells : ",nxtCells
        #print "None Cells : ",noneCells
        print "\nNext Cells : ",nxtCells
        print "\nNumber of Points to be clustered : ",cnt
        print "\nStart Clustering : ",datetime.datetime.now()

        if nxtCells != []:
            distances = scipy.spatial.distance.cdist(nxtCells, nxtCells, 'cityblock') #Create a matrix of distance between points
            print "\nMatrix Size : ",distances.shape
            finalClusters = scipy.cluster.hierarchy.fclusterdata(distances,1)
            #print "Final Cluters : ",finalClusters

        # To form dict for Prediction Input
        clusterID = 0
        #currentCluster ={}
        max = 0
        dup = 0
        predictionInput ={}
        # To form dict for Prediction Input
        for clusterKey in finalClusters:
            if clusterKey in predictionInput:
                dup = dup +1
            #currentCluster.setdefault(clusterKey,[]).append(nxtCells[i]) #To append row,col to the dict
            cellKey = FunctionLib().reverseCell(nxtCells[clusterID])
            predictionInput.setdefault(clusterKey,[]).append(cellKey) #To append cellKey to the dict
            if clusterKey > max :
                max = clusterKey
            clusterID=clusterID+1

        #print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
        decision = decision+1
        print "\nMaximum Key : ",max
        print "\nDuplicates : ",dup
        print "\nTotal Points clustered : ",max+dup
        print "\nTally Correct : ",max+dup==clusterID
        print "\nCluster Output :",predictionInput
        print "\nEnd Clustering : ",datetime.datetime.now()

        #print predictionInput
        predictObject = Prediction()
        prob,IncomingDict,t_wt = predictObject.predict(IncomingDict,predictionInput,grid)
        print "Total weight is :",t_wt
        print "\nDecision taken: ",decision , " as ",prob

        if(decision == threshold or (old_wt/t_wt)>2):
            return prob,decision
        else:
            print "\nInside else for prediction\n"
            prob,decision = self.makeClusters(IncomingDict,grid,decision,threshold,t_wt)

        return prob,decision