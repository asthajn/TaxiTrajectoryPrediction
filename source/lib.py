import math
import numpy as np

class FunctionLib(object):
    
    def generateCell(self,pt,cellSize,numOfCols,minX,minY):
        row = int((pt[0]-minX)/cellSize)
        col = int((pt[1]-minY)/cellSize)
        key = row*numOfCols + col
        #print "Key is" , key
        return key

    def reverseCell(self,tuple):
        key = tuple[1]*4456+tuple[0]
        return key

    def vectorMagnitude(self,vector):
        return math.sqrt((vector[0]*vector[0])+(vector[1]*vector[1]))

    def getCosineDistance(self,vector1, vector2):
        if vector1 == None or vector2 == None:
            return 0
        else:
            magnitude = self.vectorMagnitude(vector1)*self.vectorMagnitude(vector2)
            if magnitude == 0:
                return 0
            return np.dot(vector1,vector2)/(self.vectorMagnitude(vector1)*self.vectorMagnitude(vector2))

    def getVector(self,point1,point2):
        return [(point2[0] - point1[0]),(point2[1] - point1[1])]
