import csv
import createGrid
from findSimilar import Similarity
import pickle
import gridcomponents

try:
    f = open('../preprocessed_data/grid_components.txt', 'rb')
except IOError:
    gridComp = gridcomponents.readCSV("../data/training.csv")
    f = open('../preprocessed_data/grid_components.txt', 'wb')
    pickle.dump(gridComp,f)
    f.close()
else:
    gridComp = pickle.load(f)
    f.close()
finally:  
    minX,minY = gridComp['minX'], gridComp['minY']
    cellSize = gridComp['cellSize']
    numOfCols = int(gridComp['numOfCols'])
    numOfRows = int(gridComp['numOfRows'])

try:
    f = open('../preprocessed_data/grid.txt', 'rb')
except IOError:
    grid = createGrid.create_grid("../data/training.csv",minX,minY,cellSize,numOfCols,numOfRows)
    f = open('../preprocessed_data/grid.txt', 'wb')
    pickle.dump(grid,f)
    f.close()
else:
    grid = pickle.load(f)
    f.close()

similar = Similarity()

similar.readtest("../data/test.csv",cellSize,numOfCols,minX,minY,grid)
