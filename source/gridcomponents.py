import os
import numpy
import csv
import re

class calcgrid(object)
    def readCSV():
        with open("../data/training.csv","r") as train:
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
            #print "I am here"  

            for row in reader:
                count = count+1
                if (count == 1):                                #ignore the first row i.e. header row of the csv file
                    continue                        
                if (row[8] == '[]'):
                    continue
        
                #if count > limitrow:                           #if you no not wish to approximate on whole data
                    #break
                internalCount = 0
                for coord in re.sub(r"\[\[|]]",'',row[8]).split('], ['):
                    #print count
                    n = n+1
                    internalCount = internalCount+1
                    if (internalCount == 1):
                        (initX , initY) = map(float,coord.strip().split(','))
                        continue    

                    (nextX,nextY) = map(float,coord.strip().split(','))
                    
                    if (nextX > initX):
                        diffX = diffX+ (nextX - initX)
                    else:
                        diffX = diffX + (initX - nextX) 

                    if (nextY > initY):
                        diffY = diffY+ (nextY - initY)
                    else:
                        diffY = diffY + (initY - nextY) 

                    if(minX > nextX):
                        minX = nextX
                    if (minY > nextY):
                        minY = nextY    

                    if (maxX < nextX):
                        maxX = nextX
                    if (maxY < nextY):
                        maxY = nextY
                    
                    initX = nextX
                    initY = nextY   

                internalCount = 0
                    #print "Coordinates : ",x,y
            cellSize = (diffX + diffY)/(2*n)    

            numOfRows = (maxY-minY)*100 / cellSize
            numOfCols = (maxX-minX)*100 / cellSize
            print "Maximum and minimum coordinates : ", maxX ," , ", maxY ," and " , minX ," , ", minY 
            print "the cell size is ", cellSize
            print "Number of rows = ",numOfRows
            print "Number of columns = ", numOfCols
            
            #with open('gridParameters.csv' , 'wb') as outFile:
                #param = csv.writer(outFile, delimiter=' ', quotechar='|', quoting=csv.QUOTE_MINIMAL)
                #param.writerow(['cellSize'])
            f = open('../results/gridParameters.csv' , 'wb')
            f.write("Cell Size : " + str(cellSize) + "\nMaximum x,y [" + str(maxX) + " , "+ str(maxY) + "] \nMinimum x,y [" + str(minX) + " , " + str(minY) +"]\nNumber of Rows : "+ str(numOfRows) +"\nNumber of Columns : "+ str(numOfCols))
            f.close()

            return (cellSize, maxX, maxY , minx, minY, numOfRows, numOfCols)