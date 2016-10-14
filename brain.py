from pyNeuron import Neuron, Cluster

n1 = Neuron()
n2 = Neuron(connections=[n1])
n3 = Neuron(connections=[n1,n2])
n4 = Neuron(connections=[n3])

n1.connect(n2)

# n1.connect(n4)


neurons = [n1, n2, n3, n4]

cluster = Cluster(neurons=neurons)


for el in neurons:
	print(el.connections)

data = 2 + 3



def square(x):
	return x * x


session = cluster.submit(data=data, task=square)

print(session)


c2 = Cluster(neurons=[])
c2.genNeurons(count=10)

print(c2.showNetwork())

# print('n1', n1.getLocalData())
# print('n2', n2.getLocalData())
# print('n3', n3.getLocalData())
# print('n4', n4.getLocalData())
