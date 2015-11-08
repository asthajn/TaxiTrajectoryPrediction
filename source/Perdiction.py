import os


class Prediction(object):

	# def __init__(self):

	def predict(partial , cluster,grid): #partial is the set of trajectories , cluster is list of list of cluster cells coming from Hushmija - has centroid also
		t_wt,weights = totalWeight(partial)
		prob = {}
		for key,value in cluster.iteritems():
			prob[key] = weights['key']/t_wt
			prob[key]['cluster'] = value['centroid']

		partial = updateWeightAndNextKey(partial,cluster, weights,t_wt,grid)

		return prob,partial

	# def totalWeight(self, partial):
	# 	t_wt = 0 # total of weights
	# 	for t_id,v_id in partial.iteritems():
	# 		t_wt = t_wt+v_id['weight']
	# 	return t_wt

	def clusterWeight(self,partial, cluster, t_wt):
		weights = {} # weight of individual cluster
		for key, value in cluster.iteritems(): # key is the cluster number
			c_wt = 0
			for point in value['points']:
				for traj, traj_data in partial.iteritems():
					if traj_data['nextKey'] == point:
						c_wt = c_wt + traj_data['weight']
			weights['key'] = c_wt
			t_wt = t_wt+c_wt
		return t_wt,weights

	def updateWeightAndNextKey(self, partial,cluster, c_wt , t_wt,grid):
		for traj, value in partial.iteritems():
			value['weight'] = value['weight'] + (c_wt['key']/t_wt)
		    oldNextKey = partial[traj]['nextKey']
            if oldNextKey == None:
                continue
            partial[traj]['nextKey'] = grid[oldNextKey][traj]['nextKey']
            partial[traj]['currentKey'] = oldNextKey
        return partial
 
