import numpy
import csv
import math

def readCSV(fileLoc):
    with open(fileLoc,"r") as train:
        reader = csv.reader(train)
        count = 0
        limitrow = 10                                       #count of rows to be considered
        n = 0
        numOfRows = 0
        numOfCols = 0
        minX = 0
        minY = 10000
        maxX = -100000
        maxY = 0
        diffX = 0
        diffY = 0
        cellSize = 0 

        for row in reader:
            count = count+1
            if (count == 1):                                #ignore the first row i.e. header row of the csv file
                continue                        
            if (row[8] == '[]'):
                continue
        
            #if count > limitrow:                           #if you no not wish to approximate on whole data
            #    break
            
            coordPairs = eval(row[8])
            for i in range(len(coordPairs)-1):    
                n = n+1
                (X,Y) = coordPairs[i][0], coordPairs[i][1]
                (nextX,nextY) = coordPairs[i+1][0], coordPairs[i+1][1]
                diffX = diffX+ math.fabs(nextX - X)
                diffY = diffY+ math.fabs(nextY - Y)

                if(minX > X):
                    minX = X
                if (minY > Y):
                    minY = Y    

                if (maxX < X):
                    maxX = X
                if (maxY < Y):
                    maxY = Y  

        cellSize = (diffX + diffY)/(2*n)    
        numOfRows = (maxY-minY) / cellSize
        numOfCols = (maxX-minX) / cellSize
        print "Maximum and minimum coordinates : ", maxX ," , ", maxY ," and " , minX ," , ", minY 
        print "the cell size is ", cellSize
        print "Number of rows = ",numOfRows
        print "Number of columns = ", numOfCols

        #with open('gridParameters.csv' , 'wb') as outFile:
            #param = csv.writer(outFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
            #param.writerow(['cellSize'])
        #f = open('../results/gridParameters.csv' , 'wb')
        #f.write("Cell Size : " + str(cellSize) + "\nMaximum x,y [" + str(maxX) + " , "+ str(maxY) + "] \nMinimum x,y [" + str(minX) + " , " + str(minY) +"]\nNumber of Rows : "+ str(numOfRows) +"\nNumber of Columns : "+ str(numOfCols)) 
        #f.close()
        return {'maxX':maxX, 'maxY' : maxY, 'minX' :minX, 'minY':minY, 'cellSize':cellSize, 'numOfRows':numOfRows, 'numOfCols':numOfCols}
