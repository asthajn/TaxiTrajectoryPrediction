

class Validation(object):

	def validation(self,shouldbeResult,probability, hops):
		maxProb = 0
		maxCentroid = 0.0
		for cluster_ID,value in probability.iteritems():
			for position, prob in value.iteritems():
				if prob>maxProb:
					maxProb = prob
					maxCentroid = position

		