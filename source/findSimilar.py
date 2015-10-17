import os
import csv
from collections import defaultdict

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

	        for testPt in polyline:
	        	key = self.generateCell(testPt,cellSize,numOfCols,minX,minY)
	        	#print "Cols", numOfCols
	        	partial = self.distNeighbour(key,numOfCols,grid)
	        	#print partial
	        	break
	        break	


    def generateCell(self,testPt,cellSize,numOfCols,minX,minY):
        row = int((testPt[0]-minX)/cellSize)
        col = int((testPt[1]-minY)/cellSize)
        key = row*numOfCols + col
        print "Key is" , key
        return key


    def distNeighbour(self,key,numOfCols,grid):
    	#print numOfCols
    	partial = {}

    	partial[key]={}
    	ctr =0
    	neighbour_list =[key+1,key-1,key+numOfCols,key-numOfCols, key+numOfCols+1 , key-numOfCols+1 , key+numOfCols-1 , key-numOfCols-1, key]

    	for key_grid,value_grid in grid.iteritems():
    		#print "Checking if key exists \n"
    		#print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa    ",key_grid , "     " , key
    		if key_grid in neighbour_list:
    			#print "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa    ",value_grid,"\n"
    			print "@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@    ", ctr,key_grid
    			partial[key].update(value_grid)
	    		#	print "------------------------------------------------------------------------------" , partial[key]
	    		ctr = ctr+1
    	#print partial
    	return partial
    	#print "list" , neighbour_list[2]
    	# for neighbour in neighbour_list:
    	# 	if grid[neighbour] == {}:
	    # 		partial[key]=grid[neighbour]
	    		#print "\n",neighbour


    #def getTimeNeighbour():





            
        
        
        
