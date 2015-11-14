from cluster.method.hierarchical import HierarchicalClustering
from cluster.method.kmeans import KMeansClustering
import numpy as np
import math
from Prediction import Prediction
from lib import FunctionLib

class HClustering(object):

	# threshold = 2
	# decision = 0
	
	def makeClusters(self,IncomingDict,grid,decision,threshold):
        #print "----------------------------------------------------------------------------------------------------------------"
        #print "Incoming Dict : " ,IncomingDict

		nxtCells = []
		noneCells =[]
		cnt = 0

		for trajID in IncomingDict:
			#Adding the cells to a list to be clustered
			nxtCell = IncomingDict[trajID].get('nextKey')

			weight = IncomingDict[trajID].get('weight')
			noneCells.append(nxtCell)
			if nxtCell is not None and weight > 4.0:
				x = int(nxtCell%4456)
				y = int(nxtCell/4456)
				nxtCells.append((x,y))
				#nxtCells.append(nxtCell)
				cnt = cnt +1
		#print "Next Cells : ",nxtCells
		#print "None Cells : ",noneCells
		print "Number of Points to be clustered : ",cnt



		if nxtCells != []:
			#cl = HierarchicalClustering(nxtCells, lambda x,y: abs(x-y),None,3) #abs(x-y) gives the Manhattan distance between x and y
			cl = KMeansClustering(nxtCells,None)
			#finalClusters = cl.getlevel(10) #Threshold value given to prune clusters
			finalClusters = cl.getclusters(20)
			print "Final Cluters : ",finalClusters

		# To form dict for Prediction Input
		clusterID = 1
		predictionInput ={}
		# To form dict for Prediction Input
		for cluster in finalClusters:
			#print "------------------------------------------------------"
			#print cluster
			currentCluster=[]
			for eachTuple in cluster:
				cellKey = FunctionLib().reverseCell(eachTuple)
				currentCluster.append(cellKey)
			print currentCluster
			predictionInput[clusterID] = {}
			predictionInput[clusterID]['centroid'] = math.ceil(np.mean(currentCluster))
			predictionInput[clusterID]['points'] = currentCluster
			clusterID = clusterID+ 1
		print "++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++"
		decision = decision+1
		
		#print predictionInput
		predictObject = Prediction()
		prob,IncomingDict = predictObject.predict(IncomingDict,predictionInput,grid)
		print "\nDecision taken: ",decision , " as ",prob

		if(decision == threshold):
			return
		else:
			print "\nInside else for prediction\n"
			self.makeClusters(IncomingDict,grid,decision,threshold)

