import os
import csv
from collections import defaultdict
import numpy as np
import createGrid
import math

class Similarity(object):

	#def __init__() #---------------- make numofcols, cellsize as global

    def readtest(self,fileLoc,cellSize,numOfCols,minX,minY,grid):
        csvfile = open(fileLoc)
        data = csv.reader(csvfile)
        labels = next(data)
        partial = {}

        for traj_data in data:
        	#print line
        	#print ";;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;;"
	        trip_id = traj_data[0]
	        timestamp = int(traj_data[5])
	        polyline = traj_data[8]
	        polyline = eval(polyline)
	        length = len(polyline)
	        ts = timestamp

	        for testPt in range(len(polyline)):
	        	key = self.generateCell(polyline[testPt],cellSize,numOfCols,minX,minY)
	        	if testPt < (len(polyline) -1):
                            vector = [(polyline[testPt+1][0] - polyline[testPt][0]),(polyline[testPt+1][1] - polyline[testPt][1])]
                        else:
                            vector = None
                        ts = (ts+15*testPt)
	        	partial = self.distNeighbour([vector,ts],key,numOfCols,grid)

	        break	


    def generateCell(self,testPt,cellSize,numOfCols,minX,minY):
        row = int((testPt[0]-minX)/cellSize)
        col = int((testPt[1]-minY)/cellSize)
        key = row*numOfCols + col
        print "Key is" , key
        return key


    def distNeighbour(self,selfData,key,numOfCols,grid):
    	partial = {}
    	partial[key]={}
    	#ctr =0
    	neighbour_list =[key+1,key-1,key+numOfCols,key-numOfCols, key+numOfCols+1 , key-numOfCols+1 , key+numOfCols-1 , key-numOfCols-1, key]

    	for key_grid,value_grid in grid.iteritems():
    		if key_grid in neighbour_list:
    			#print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    ", ctr,key_grid
    			for traj,value in value_grid.iteritems():
                            if value[0] == None or selfData[0] == None:
                                continue
                            val = np.dot(value[0],selfData[0])/(math.sqrt((value[0][0]*value[0][0])+(value[0][1]*value[0][1])) * math.sqrt((selfData[0][0]*selfData[0][0])+(selfData[0][1]*selfData[0][1])))
                                  
    			partial[key].update(value_grid)
	    		#ctr = ctr+1

    	return partial

    #def getTimeNeighbour():





            
        
        
        
