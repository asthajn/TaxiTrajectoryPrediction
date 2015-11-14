def read(self,fileLoc):
	csvfile = open(fileLoc)
	data = csv.reader(csvfile)

	original_dest = {}
	ctr = 0
	
	cellSize = 0.00085
	numOfCols = 4456
	minX = -9.8
	minY = 36.7

	for line in data:
		ctr = ctr+1
		original_dest[ctr]={}
		dest = eval(line)
		for hops in range(len(dest)):
			original_dest[ctr] = {'hop':hops+1,'original_dest':FunctionLib().generateCell(dest[hops],cellSize,numOfCols,minX,minY)}

	return original_dest