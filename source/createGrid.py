import csv
import math
from lib import FunctionLib

def create_grid(fileLoc,minX,minY,cellSize,numOfCols,numOfRows):
    csvfile = open(fileLoc)
    data = csv.reader(csvfile)
    labels = next(data)
    grid = {}

    #hardcoding to avoid running grid computations
    # minX,minY = [-9.137097 , 38.715066]
    # cellSize = 0.000835417147072
    # numOfCols = 167851
    # numOfRows = 405962
    for row in data:
        grid = insertIntoGrid(grid,row, minX,minY,cellSize,numOfCols,numOfRows)

    return grid

def insertIntoGrid(grid,traj_data,minX,minY,cellSize,numOfCols,numOfRows ):
    
        trip_id = traj_data[0]
        timestamp = int(traj_data[5])
        polyline = traj_data[8]
        polyline = eval(polyline)
        length = len(polyline)
        ts = timestamp

        for i in range(length):
            key = FunctionLib().generateCell(polyline[i],cellSize,numOfCols,minX,minY)
            ts = (ts+15*i)
            #print key
            if key not in grid:
                grid[key] = {}
            
            if i<(length-1):
                vector = FunctionLib().getVector(polyline[i],polyline[i+1])
                next_key = FunctionLib().generateCell(polyline[i+1],cellSize,numOfCols,minX,minY)
                grid[key][trip_id] = {'vector':vector,'nextKey':next_key,'timestamp':ts}
            else:
                grid[key][trip_id] = {'vector':None,'nextKey':None,'timestamp':ts}
        return grid
