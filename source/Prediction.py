import os
import math

class Prediction(object):

	# def __init__(self):

	def predict(self,partial , cluster,grid): #partial is the set of trajectories , cluster is list of list of cluster cells coming from Hushmija - has centroid also
		
		t_wt,weightsAndCentroid = self.clusterWeight(partial,cluster)
		prob = {} # dictionary with probability of different clusters and cluster weighted mean
		for key,value in cluster.iteritems():
			prob[key] = {}
			prob[key]['prob'] = weightsAndCentroid[key]['weight']/t_wt
			prob[key]['position'] = weightsAndCentroid[key]['centroid']
			#prob[key]['cluster'] = value['centroid']

		#print "\n \nProb for prediction :",prob

		partial = self.updateWeightAndNextKey(partial,cluster, weightsAndCentroid,t_wt,grid)

		return prob,partial,t_wt

	# def totalWeight(self, partial):
	# 	t_wt = 0 # total of weights
	# 	for t_id,v_id in partial.iteritems():
	# 		t_wt = t_wt+v_id['weight']
	# 	return t_wt

	def clusterWeight(self,partial, cluster):
		weightsAndCentroid = {} # weight of individual cluster
		t_wt = 0
		for key, value in cluster.iteritems(): # key is the cluster number
			c_wt = 0
			combined_wt =0
			#sum_cell = 0
			for point in value['points']:
				for traj, traj_data in partial.iteritems():
					if traj_data['nextKey'] == point:
						c_wt = c_wt + traj_data['weight']
						combined_wt = combined_wt + point*traj_data['weight']
			# weights['key'] = c_wt
			# centroid['key'] = combined_wt/sum_cell
			weightsAndCentroid[key] = {}
			weightsAndCentroid[key]['weight'] = c_wt
			weightsAndCentroid[key]['centroid'] = math.ceil(combined_wt/c_wt)

			#print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@ \n",weightsAndCentroid[key]['centroid'] , weightsAndCentroid[key]['weight']
			t_wt = t_wt+c_wt
		return t_wt,weightsAndCentroid

	def updateWeightAndNextKey(self, partial,cluster, c_wt , t_wt,grid):
		for traj, value in partial.iteritems():
			for key, cluster_points in cluster.iteritems():
				if traj in cluster_points:
					value['weight'] = value['weight'] + c_wt[key]['weight']/t_wt #+ (c_wt[partial[traj]['currentKey']]['weight']/t_wt) -------update here
			oldNextKey = partial[traj]['nextKey']
			if oldNextKey == None:
				continue
			partial[traj]['nextKey'] = grid[oldNextKey][traj]['nextKey']
			partial[traj]['currentKey'] = oldNextKey
		return partial
 
