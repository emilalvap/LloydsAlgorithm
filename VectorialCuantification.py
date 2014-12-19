import numpy

'''Container class for Lloyds algorithm:
 -> N equals de dimension of vectors to process
 -> maxK is the number of max iterations to calculate
 '''

class VectorialCuantification():

	def __init__(self,N,maxK,tolerance):

		self.N = N
		self.centers = []
		self.centersNames = []
		self.trainingVectors = []
		self.maxK = maxK
		self.gammaK = None
		self.tolerance = tolerance

	def getGammaK(self):
	
		return self.gammaK

	def setGammaK(self,floatGamma):
		self.gammaK = floatGamma

	def addInitialCenter(self,cVector,cName):

		self.centers.append(cVector)
		self.centersNames.append(cName)

	def addTrainingVector(self,tVector):

		self.trainingVectors.append(tVector)

	def trainCenter(self,xVector):

		updateIndex = self.nearestCenter(xVector)
		return self.updateCenter(updateIndex,xVector)

	def nearestCenter(self,xVector):

		mini = float('inf')
		index = None
		for i in range(len(self.centers)): 
			dist = numpy.linalg.norm(numpy.subtract(xVector,self.centers[i]))
			if(dist < mini):
				mini = dist
				index = i
		return index

	def updateCenter(self,index,xVector):

		tolerance = numpy.linalg.norm(numpy.subtract(self.centers[index],xVector))
		self.centers[index] = numpy.add(self.centers[index],(numpy.dot(self.gammaK,numpy.subtract(xVector,self.centers[index]))))
		return tolerance

	def clasify(self,xVector):

		return self.centersNames[self.nearestCenter(xVector)]

	def generateTraining(self):

		toleranceBreak = False

		for k in range(self.maxK):
			for tVector in self.trainingVectors:
				tolerance = self.trainCenter(tVector)
				
				if(tolerance < self.tolerance):
					toleranceBreak = True
					break
			if(toleranceBreak==True):
				break

		if(toleranceBreak==True):
			print "Iteraciones rotas por limite de tolerancia"

	def getCenters(self):

		return self.centers

'''Ejemplo diapositiva 19 '''
toleranceLimit = numpy.power(10,-10)
lloyd = VectorialCuantification(2,2,toleranceLimit)
lloyd.setGammaK(0.1)
#centers
lloyd.addInitialCenter([1,4],"Clase 1")
lloyd.addInitialCenter([7,2],"Clase 2")
#training vectors
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
#value generation
lloyd.generateTraining()
print "Ejemplo diapositiva 19:"
print ">>>> Valores de los centros"
print lloyd.getCenters()
print ">>>> Test de valores"
print "[6,2] pertenece a ",lloyd.clasify([6,2])