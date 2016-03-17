#PARKIFY ALGORITHM

This algorhitm implementation is adapted to the parking system of ITESM Campus Guadalajara,
there are 10 sections for parking around the campus.

<p align="center">
  <img src="https://github.com/iotchallenge2016/Parking-lot/blob/info/parkinglot.png"/>
</p>

The users need to find the best parking lot section according to their desination,wich is choosen 
on the mobile app.For this reason we desingned the campus as a graph,wich includes the parking lot 
sections and general areas of destination(Library,Gym,Enginnering Building).The objective is to find 
the best place depending on the proximity and occupation

<p align="center">
  <img src="https://github.com/iotchallenge2016/Parking-lot/blob/master/Graph.png"/>
</p>

Green nodes represent the parking lot sections,the yellow ones the destination areas and the 
blue node is the entrance.Wich is the starting point in the graph.

The desing of the graph is made on the data base,each parking lot section is define by it's
name,the max capacity and the ocuppation number of spaces at the moment.

```JSON
[
  {
    "max": 291,
    "section": "P_Civil",
    "capacity": 150
  },
  {
    "max": 446,
    "section": "P_Ingenieria",
    "capacity": 40
  }
]
```
For the graph representation in the data base, parking lot sections and destinations are defined with 
their neighbors,the type and name.For each neighbor there's a cost connection,so at the end we have a 
weighted graph.

```JSON

  {
    "neighbors": [
      [
        "P_Entrance",
        10
      ]
    ],
    "type": "landmark",
    "entrance": true,
    "place": "Entrance"
  },
  {
    "neighbors": [
      [
        "P_Residencias",
        10
      ],
      [
        "P_Entrance",
        15
      ]
    ],
    "type": "landmark",
    "entrance": false,
    "place": "Residencias"
  }
]
```
The algorithm works by applying the shortest path solution by Dijkstra,the entrance node is always the beginning,
then we pass the destination node(choosen in the app) and by the wheights of the connections the Dijktra algorithm 
finds theshorthest path,wich includes destination nodes and parking sections as well.

We move trought this path from destination to entrance and the node that appears, of type "parking" ,will be the 
most recomandable parking section for the user.About the capacity for each section,the algorithm is capable of decide if the choosen parking section on the shorthest path, is already full or beyond the tolerance point;if that happens is choosen the closest neighbor of that parking section that is available;this process is repeated if it's needed,until a better parking section is found.

##### Algorithm Code

```python
import networkx as nx

class Graph:
	g = None
	sections = None

	def __init__(self, places, sections):
		self.g = nx.Graph()
		self.sections = sections
		for i in places:
			self.g.add_node(i['place'], type=i['type'], entrance=i['entrance'])
			if (self.g.node[i['place']]['type'].upper() == 'PARKING'):
				self.g.node[i['place']]['section'] = self.find_section(i['place'])
			for j in i['neighbors']:
				self.g.add_edge(i['place'], j[0], weight=j[1])

	def get_closest_parking_section(self, dstNodeId, tolerance=5):
		paths = []
		for i in self.find_entrances():
			path = nx.dijkstra_path(self.g, i, dstNodeId)
			while (self.g.node[path[-1]]['type'].upper() != 'PARKING'):
				path.pop()
			paths.append(path)

		destinations = []
		for i in xrange(0, len(paths)):
			destinations.append(paths[i][-1])

		for i in xrange(0,len(destinations)):
			section = self.g.node[destinations[i]]['section']
			free = float(section['capacity']) / section['max'] * 100
			prevFound = [destinations[i]]
			while (free < tolerance):
				destinations[i] = self.find_neighbor_with_parking_spots(destinations[i], exclude=prevFound)
				prevFound.append(destinations[i])
				section = self.g.node[destinations[i]]['section']
				free = float(section['capacity']) / section['max'] * 100

		if len(destinations) == 1:
			destinations = destinations[0]

		return destinations

	def find_neighbor_with_parking_spots(self, nodeId, exclude=[]):
		for nid in self.g.neighbors(nodeId):
			if self.g.node[nid]['type'].upper() == 'PARKING' and nid not in exclude:
				return nid
		return None

	def find_entrances(self):
		entrances = []
		for i in self.g.nodes(data=True):
			if 'entrance' in i[1] and i[1]['entrance']:
				entrances.append(i[0])
		return entrances

	def find_section(self, name):
		for i in self.sections:
			if name == i['section']:
				return i
		return None

	def text(self):
		text = 'Nodes: \n'
		for i in self.g.nodes(data=True):
			text += str(i) + '\n'
		text += '\nEdges:\n'
		for i in self.g.edges(data=True):
			text+= str(i) + '\n'
		text+= '\n'
		return text

	def html_text(self):
		return self.text().replace('\n','<br>')

	def to_dict(self):
		return {'nodes': self.g.nodes(data=True), 'edges': self.g.edges(data=True)}

	def display(self):
		print self.text()

 
```





