#PARKIFY ALGORITHM

This algorhitm implementation is adapted to the parking system of ITESM Campus Guadalajara,
there are 10 sections for parking around the campus.

![alt tag](https://github.com/iotchallenge2016/Parking-lot/blob/info/parkinglot.png)


The users need to find the best parking lot section according to their desination,wich is choosen 
on the mobile app.For this reason we desingned the campus as a graph,wich includes the parking lot 
sections and general areas of destination(Library,Gym,Enginnering Building).The objective is to find 
the best place depending on the proximity and occupation

![alt tag](https://github.com/iotchallenge2016/Parking-lot/blob/master/Graph.png)

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




