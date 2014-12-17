import numpy



class VectorialCuantification():

	def __init__(self,N,maxK):

		self.N = N
		self.centers = []
		self.trainingVectors = []
		self.maxK = maxK
		self.gammaK = None

	def getGammaK(self):
	
		return self.gammaK

	def setGammaK(self,floatGamma):
		self.gammaK = floatGamma

	def addInitialCenter(self,cVector):

		self.centers.append(cVector)

	def addTrainingVector(self,tVector):

		self.trainingVectors.append(tVector)

	def trainCenter(self,xVector):
		updateIndex = self.nearestCenter(xVector)
		print "centro elegido: ", updateIndex
		self.updateCenter(updateIndex,xVector)

	def nearestCenter(self,xVector):

		mini = float('inf')
		index = None
		for i in range(len(self.centers)): 
			dist = numpy.linalg.norm(numpy.subtract(xVector,self.centers[i]))
			print "distancia al centro ", i ," igual a ",dist
			if(dist < mini):
				mini = dist
				index = i
		return index

	def updateCenter(self,index,xVector):

		self.centers[index] = numpy.add(self.centers[index],(numpy.dot(self.gammaK,numpy.subtract(xVector,self.centers[index]))))
		

	def clasify(self,xVector):

		return nearestCenter(xVector)

	def generateTraining(self):

		for k in range(self.maxK):
			for tVector in self.trainingVectors:
				self.trainCenter(tVector)

	def getCenters(self):

		return self.centers

'''Ejemplo diapositiva 19 '''
lloyd = VectorialCuantification(2,2)
lloyd.setGammaK(0.1)
#centros
lloyd.addInitialCenter([1,4])
lloyd.addInitialCenter([7,2])
#vectores de entrenamiento
lloyd.addTrainingVector([1,1])
lloyd.addTrainingVector([1,3])
lloyd.addTrainingVector([1,5])
lloyd.addTrainingVector([2,2])
lloyd.addTrainingVector([2,3])
lloyd.addTrainingVector([6,3])
lloyd.addTrainingVector([6,4])
lloyd.addTrainingVector([7,1])
lloyd.addTrainingVector([7,3])
lloyd.addTrainingVector([7,5])
lloyd.generateTraining()
print lloyd.getCenters()