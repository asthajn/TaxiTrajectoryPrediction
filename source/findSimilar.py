import csv
from lib import FunctionLib
import numpy as np
import math
from constants import JOIN_WEIGHT

class Similarity(object):

    def readtest(self,fileLoc,cellSize,numOfCols,minX,minY,grid):
        csvfile = open(fileLoc)
        data = csv.reader(csvfile)
        labels = next(data)
        partial = {}

        for traj_data in data:
	        trip_id = traj_data[0]
	        timestamp = int(traj_data[5])
	        polyline = traj_data[8]
	        polyline = eval(polyline)
	        length = len(polyline)
	        ts = timestamp
                partial = {}
	        for testPt in range(len(polyline)):
	        	key = FunctionLib().generateCell(polyline[testPt],cellSize,numOfCols,minX,minY)
	        	if testPt < (len(polyline) -1):
                            vector = FunctionLib().getVector(polyline[testPt],polyline[testPt+1])
                            nextKey = FunctionLib().generateCell(polyline[testPt+1],cellSize,numOfCols,minX,minY)
                        else:
                            vector = None
                            nextKey = None
                        ts = (ts+15*testPt)
	        	partial = self.distNeighbour({'vector':vector,'nextKey':nextKey,'timestamp':ts},key,numOfCols,grid, partial)

    def distNeighbour(self,selfData,key,numOfCols,grid, partial):
    	neighbour_list =[key+1,key-1,key+numOfCols,key-numOfCols, key+numOfCols+1 , key-numOfCols+1 , key+numOfCols-1 , key-numOfCols-1, key]

    	for key_grid,value_grid in grid.iteritems():
    		if key_grid in neighbour_list:
    			for traj,value in value_grid.iteritems():
                            if traj not in partial:
                                partial[traj] = {'nextKey':value['nextKey'],'weight':0, 'currentKey' :key_grid}
                            cosineDist = FunctionLib().getCosineDistance(value['vector'],selfData['vector'])
                            partial[traj]['weight']= partial[traj]['weight'] + JOIN_WEIGHT + cosineDist

                for traj in partial:
                    if traj not in value_grid:
                        oldNextKey = partial[traj]['nextKey']
                        if oldNextKey == None:
                            continue
                        partial[traj]['nextKey'] = grid[oldNextKey][traj]['nextKey']
                        partial[traj]['currentKey'] = oldNextKey
 
    	return partial





            
        
        
        
