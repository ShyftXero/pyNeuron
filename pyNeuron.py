import uuid


class Cluster:
	"""a cluster is a collection of Neurons.

	a Neuron can belong to multiple clusters.
	"""

	def __init__(self, neurons=[]):
		self.neurons = neurons
		

	def submit(self, data, task):
		task_id = uuid.uuid4()
		for neuron in self.neurons:
			neuron.consume(data, task)

		return task_id


	def genNeurons(self, count=10):
		"""Creates a given number of Neurons, creates a connection to another Neuron, and adds them to the cluster.  
		"""
		for i in range(1,count):
			# the i * 3 % len(neurons) should prevent index and bound errors but still provide 'interesting' connections
			n = Neuron(connections=[i * 3 % (len(self.neurons) + 1)])
			self.neurons.append(n)

	def showNetwork(self):
		return self.neurons

class Neuron:
	"""
	Neuron is a fundamental object that is uniquely identified and connected to other Neurons. 
	Neuron is aware of its sibling Neurons and whether or not it has a path to a given Neuron. 

	A Neuron
	id = unique id
	coords = tuple to help express the concept of weight. Further two points are the more expensive the path is.
	connection = dict of {Neuron's id : 'x,y,z coords of this Neuron'
	clusters = dict of clusters of Neurons; this is for having multiple brains in a brain.
	data = data that is local to this neuron. could describe state, efficiency, features, etc.
	"""

	#As the Neuron is created do things things.

	id = None
	connections = None
	data = None
	clusters = None
	coords = None

	def __init__(self, connections=[], clusters={}, coords=(0,0,0), data=None):
		self.id = id(self)
		self.connections = connections 
		self.data = data
		self.clusters = clusters
		self.coords = coords

	#human readable representation of this Neuron
	# def __repr__(self): 
	# 	return	str(self))

	def connect(self, Neuron):
		self.connections.append(Neuron)
		return True

	def disconnect(self, Neuron):
		if id(Neuron) in self.connections:
			del self.connections[Neuron.id]
			return	True
		return False

	def joinCluster(self, clusterID):
		return True

	def leaveCluster(self, clusterID):
		return True

	def getConnections(self):
		return self.connections

	def getLocalData(self):
		return self.data

	def setLocalData(self, data):
		self.data = data
		return True

	def calcDistance(self, Neuron):
		"""returns the distance from this Neuron to another Neuron. """
		# TODO: implement the math to figure this out. 
		# returns 0 to help propagate
		return 0

	def propogate(self, data, reach=0):
		"""send this data in a forward direction to all Neurons connected to this Neuron
		data = the data to send out.
		reach = how far to reach out to other nodes to send data.
		"""
		# print('propagating message to other Neurons:', data)
		#iterate the list of this Neuron's connections
		# print(self.connections)
		for neuron in self.connections:
			#neuron = objects_by_id(neuron.id)
			#if it is close enough to reach ; remember to actually implement calcDistance
			if self.calcDistance(neuron) <= reach:
				#call consume method on every Neuron in its network
				# print('pushing', data, 'to', neuron)
				# neuron = Neuron(id=neuron)
				
				neuron.setLocalData(data)
				try:
					neuron.propogate(data)
				except RecursionError:
					return

				#send the message down the line
				# if self.id != id(neuron):
				# 	neuron.consume(data)

		
	#generic calculations for the Neuron. Just eval python for the time being.
	def consume(self, data, task, forward=False):
		"""Consume and process data
		what does it mean to consume or process data?
		Presently, we just eval the code. 
		"""

		print('Running task:', task.__name__, "on Neuron:", self)
		result = task(data)
		print("Result", result)
		self.setLocalData(result)
		self.propogate(result)
		# for neuron in self.connections:
		# 	if self.id != id(neuron):
		# 		neuron.consume(result)	

		

