import csv
import math

import gridcomponents

def create_grid(fileLoc):
    csvfile = open(fileLoc)
    data = csv.reader(csvfile)
    labels = next(data)
    grid = {}
    #gridComp = gridcomponents.readCSV(fileLoc)
    #minX,minY = gridComp['minX'], gridComp['minY']
    #cellSize = gridComp['cellSize']
    #numOfCols = gridComp['numOfCols']
    #numOfRows = gridComp['numOfRows']

    #hardcoding to avoid running grid computations
    minX,minY = [-9.137097 , 38.715066]
    cellSize = 0.000835417147072
    numOfCols = 167851
    numOfRows = 405962
    for row in data:
        grid = insertIntoGrid(grid,row, minX,minY,cellSize,numOfCols,numOfRows)

    return grid

def insertIntoGrid(grid,traj_data,minX,minY,cellSize,numOfCols,numOfRows ):
    
        trip_id = traj_data[0]
        timestamp = traj_data[5]
        polyline = traj_data[8]
        polyline = eval(polyline)
        length = len(polyline)

        for i in range(length):
            row = int((polyline[i][0]-minX)/cellSize)
            col = int((polyline[i][1]-minY)/cellSize)
            key = row*numOfCols + col
            #print key
            if key not in grid:
                grid[key] = {}
            
            if i<(length-1):
                grid[key][trip_id] = polyline[i+1]
            else:
                grid[key][trip_id] = None
        return grid
