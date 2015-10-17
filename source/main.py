import csv
import createGrid
from findSimilar import Similarity

import gridcomponents

gridComp = gridcomponents.readCSV("../data/training.csv")
minX,minY = gridComp['minX'], gridComp['minY']
cellSize = gridComp['cellSize']
numOfCols = int(gridComp['numOfCols'])
numOfRows = int(gridComp['numOfRows'])

#minX,minY = [-9.137097 , 38.715066]
#cellSize = 0.000835417147072
#numOfCols = 167851
#numOfRows = 405962

grid = createGrid.create_grid("../data/training.csv",minX,minY,cellSize,numOfCols,numOfRows)
count = 0

# for key,value in grid.iteritems():
#     count = count+1
#     print "\nAstha\n\n",key ,"\nvalues\n", value
#     for innerkey,innervalue in value.iteritems():
#         if innervalue[0] == None:
#             continue
#         else:
#             print "inner" , innerkey , "\nvalue\n" , innervalue[1]
#     if count == 10:
#         break



similar = Similarity()
# minX,minY = [-9.137097 , 38.715066]
# cellSize = 0.0835417147072
# numOfCols = 167851
# numOfRows = 405962
similar.readtest("../data/test.csv",cellSize,numOfCols,minX,minY,grid)
