# Parkify
## The Application

<img src="http://i.imgur.com/MKaZBnj.png" width="400"> 

### A world in constant motion

We live in a world where being able to do things faster has become a necessity to the point where even five minutes can feel like an eternity. This is related with the fact that finding a parking space is more difficult everyday due to the constant increase of traffic; therefore, it makes this a tedious process, taking longer than what the world around us demands. Having no way to be able to explore an entire parking lot, one begins to lose time by small amounts a day until it becomes a tremendous total when adding those minutes in a lifetime; however, gas is also wasted in the process.

### What is Parkify?

Parkify is an application that aims to solve this simple activity that takes one's precious time, so you are able to find a spot to park your car in faster an effective way than by searching around. It is a simple solution which manages to separate a parking lot in different zones and tells you how many spaces are free in each of this areas. Also, when Parkify gets to know you better, it will be able to priotize the closest empty parking zones near your destination. This way, looking for a parking spot can stop being a stressful chore and become an easy daily step.

### How Parkify is achieved

This application was built from the ground up by utilizing an Intel Edison Board and simulating a parking environment with the use of sensors to mark the entry and exit of cars in an area, a database stored in a web server as well as a communication with the application through the use of .json files. To put it simply, we have an application which communicates utilizing a ssh protocol to the Edison and to a database, whenever an entry or exit sensor is triggered, the the app will change accordingly.
## Hardware and software
### Intel Edison
The Intel Edison board will be utilizing a button to count a car occupying a new space, a touch sensor to represent a car leaving a free space, and an LCD screen which lists the number of free parking spots and changes color between green, yellow, and red depending on this number, with green being more than half parking spaces available, yellow being half or less spaces available, and red when there is no availability left; The updates can only be received from the sensors after an interval of 0.05 seconds. The whole development for the Edison can be found in this link.

 [First Functional](https://github.com/dtoledo23/development_card/blob/master/firstFunctional.py "GitHub Repository")

#### Image Recognition
We have implemented the use of a camera in order to be able to detect license plates and to identify the cars entering the parking lot area; however, this feature is still in development. It will capture video constantly and will take a picture whenever a license plate enters its field of view and then it will save the image and restart the camera so it is ready to detect another plate. Though this implementation isn’t complete yet, a rough version of the code is found here:

[Camara Test](https://github.com/dtoledo23/development_card/blob/master/cameraTest.py "GitHub Repository")
### Web service
We also included within the Intel Edison, we will be using its IP address to host a web server which will be used to display the main webpage of Parkify made utilizing a Materialize template as well as giving you the option to create your own parking space for the use of the application. The css and necessary scripts for it to run correctly can be found here as well as the server:

 [Init.js](https://github.com/iotchallenge2016/development_card/blob/950f8b029e6447204472b0a2a5b5659d0c9766be/static/js/init.js "GitHub Repository")

[Main.css](https://github.com/iotchallenge2016/development_card/blob/950f8b029e6447204472b0a2a5b5659d0c9766be/static/css/main.css "GitHub Repository")

[Server](https://github.com/iotchallenge2016/development_card/blob/950f8b029e6447204472b0a2a5b5659d0c9766be/server.py "GitHub Repository")

The server will not only manage the webpage, but it will also be in charge of reading the initial state of the parking lot's areas of through a csv file through a loader py file, then we have a another py file that makes requests to the server and writes into the lcd of the Edison with the use of its sensors. Finally we have another file which states when a request is invalid.

[Invalid Request](https://github.com/iotchallenge2016/development_card/blob/950f8b029e6447204472b0a2a5b5659d0c9766be/invalid_request.py "GitHub Repository")

[Loader](https://github.com/iotchallenge2016/development_card/blob/950f8b029e6447204472b0a2a5b5659d0c9766be/loader.py "GitHub Repository")

[Requests to server](https://github.com/iotchallenge2016/Parking-lot/blob/55d001aade8c4c797b8b5044747d22ce86add645/requests_to_server.py "GitHub Repository")

## Resources
Python sensor libraries:

[Intel's Python example](https://github.com/intel-iot-devkit/upm/tree/master/examples/python "Intel's GitHub Repository")


git branches:

[Create a new branch with git and manage branches](https://github.com/Kunena/Kunena-Forum/wiki/Create-a-new-branch-with-git-and-manage-branches "Kunena's GitHub Repository")

[Git Branching Basic: Branching and Merging](https://git-scm.com/book/en/v2/Git-Branching-Basic-Branching-and-Merging "Git Webpage")


IOT internet of things:

[Internet of Things 101](https://www.gitbook.com/book/theiotlearninginitiative/internetofthings101/details "Gitbook")

##__Parking Lot__

For the construction of this software, the Tecnologico de Monterrey Campus Gualadajara's parking lot was used as a prototype example. The parking lot in this campus consists in ten different areas with the following parking spaces:

Zone | Parking Spaces
---|:---:
Medicine | 412
Visitors | 237
Congress Center | 288
Residences | 230
Civil Engineering | 291
Engineering | 446
Media | 229
Library | 269
Cafeteria | 341 
Entrance | 270

The following image is the campus' parking lot divided by zones. 

![ParkingTec](http://i.imgur.com/L5xOqdS.png)

##__How does it works?__

###__Sensors__
Through the use of sensors, our program is able to detect the movement in front of them. This with the purpose of detecting wether a car is exiting or entering a certain zone of the parking lot. Thus our main system is able to keep count of how many cars are currently in the parking lot and use that to calculate the number of free spaces. By keeping the count, we are also able to classify zones' disponibility by colors, making it easier for the user to keep track of the empty spaces through the use of different hues in an LCD screen: Red is not available, Yellow is half available and Green is more than half available. This was made by setting a maximum and minimum of Flags and assigning a value to each color: 

```python 
#Limits
MAX = 20
MIN = 0

#Limit flags

RedFlag = 0
YellowFlag = 10

 # ------ LCD -------
        #Red = 252, 18, 33
        #Amarillo = 229, 220, 22
        #Verde = 46, 254, 67

    if(lugares <= RedFlag):
        myLcd.setColor(252, 18, 3)

    elif(lugares <= YellowFlag):
        myLcd.setColor(229, 220, 22)

    else:
        myLcd.setColor(46, 254, 67)

    messages = "Disponibles: " + str(lugares) + " "
    myLcd.setCursor(0,0)
    myLcd.write(messages)
    
```
###__Inside the program__
As it was previously mentioned, a file that states when a request is invalid was created. With the purpose that if, for example, the user does not uses the application by 'get' the program will display an invalid message to the user himself. This was done effectively by writting the next code in file [server.py](https://github.com/iotchallenge2016/development_card/blob/web-service/server.py "Github repository") :

```python
def api_sections():
	if request.method == 'GET':
		data = []
		for result in mongo.db[COLLECTION_TO_USE].find():
			data.append(result)
		return Response(dumps(data), mimetype='application/json')
	else:
		raise InvalidUsage('Unsupported Method', 501)

@app.route('/sections/<sectionId>', methods = ['GET'])
```

Afterwards, by creating a class inside [invalid_request.py](https://github.com/iotchallenge2016/development_card/blob/web-service/invalid_request.py "GitHub repository") and defining the needed information the request is set as invalid: 
```python
from flask import jsonify

class InvalidRequest(Exception):
	status_code = None
	message = None
	payload = None

	def __init__(self, message, status_code, payload=None):
		Exception.__init__(self)
		self.message = message
		self.status_code = status_code
		self.payload = payload

	def to_dic(self):
		rv = dict(self.payload or ())
		rv['message'] = self.message
		return rv
```

The file [graph.py](https://github.com/iotchallenge2016/development_card/blob/web-service/graph.py "GitHub Repository") was also made in order to make it possible for the program to identify the structure of the parking lot. Hence it localizes the entrances, sections, closest parking section to the user as well for the sections surrounding that section. This was by creating a Class named 'Graph' and defining the functions needed inside that class, for example, this is how we managed to make the program find the closest parking zone to the user in case he or she is in a hurry:
```python
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
```

###__Algorithm__
<p>In order to give the best performance to Parkify App, we connected each point of the campus and divided them in parking lot or buildings. This way the program search for empty spaces in the closest parking area to the user's destination inside the campus. For example, if the user is going to the Congress Center inside the campus, Parkify will beging by searching the availability inside such parking area. This way the user knows faster that there is or there is not an empty spot near to his destination. Therefore, if the parking area is full, Parkify will suggest the second closest area. For a better explanation of the algorithm please look foward to the next image: </p>
_Green: Parking Area_ | _Yellow = Building_ | _Blue = Entrance_
<p> <img src="https://github.com/iotchallenge2016/Parking-lot/blob/master/Graph.png?raw=true" width="400"> </p>
[Click here](https://github.com/iotchallenge2016/Parking-lot/blob/Algorith-desing/README.md "GitHub Repository") for the breakdown of this same algorithm.

###__The App__
_A complementar_

###__The Web page__
[Check out our Web page!](http://10.43.51.167:5000/ "Parkify Web")
A web page for the application was made so that those who are interested in how their parking lot is being used can see it on a visual represantion of a map. It was made utilizing the front-end framework materilize to give a better user experience. It is divided into four sections: Home, View, About Us, and Documentation.

On the home page the user is prompted to upload their parking lot through a .csv file containing their initial values for how the zones are filled at the moment; reading each row in the document and identyfiyng the zone and the number of occupied and free spots in each of them. This is done with the following code in [loader.py](https://github.com/iotchallenge2016/development_card/blob/web-service/loader.py "GitHub Repository"):

```python
    with open(csvURL, 'r') as csv:
        for line in csv.readlines():
            elements = line.strip().split(',')
            if diff != int(elements[zone]):
                ocpd = sum(values)
                free = total - ocpd
                json = json + toJSON(diff,free, total)
                values = []
                total = 0
                diff = int(elements[zone])
            values.append(int(elements[avlb]))
            total += 1
            
    ocpd = sum(values)
    free = total - ocpd
    return json + toJSONfinal(diff,free, total) + "]"
```

The page _View_ is where the user is able to see in a map how the different zones are filled, represented with different colors, starting from dark red (full lot) and continuing into lighter tones of blue (empty lot). Not only os the representation made on the map, but also on cards beside it that will also be filled with this colors as well as giving the number of free place and percentage of how occupied the parking lot is and it updates every 5 seconds. This can be found in [loadCards.js](https://github.com/iotchallenge2016/development_card/blob/web-service/static/js/loadCards.js "GitHub Repository").

```javascript
var html = "";
		for (var i = data.length - 1; i >= 0; i--) {
			html += "<div class='col s12'>";
			var percentage = Math.round((data[i].max - data[i].capacity) / data[i].max * 100)
			var color = "blue-grey lighten-1";
			if (percentage > 90) {
				color = "red darken-4"
			} else if(percentage > 85) {
				color = "red darken-2"
			} else if(percentage > 70) {
				color = "red"
			} else if(percentage > 60) {
				color = "red lighten-1"
			} else if(percentage > 50) {
				color = "purple darken-1"
			} else if(percentage > 40) {
				color = "blue-grey darken-1"
			}
			html += "<div class='card "+ color +"'>";
			html += "<div class='card-content white-text'>";
			html += "<div class='card-title'>" + data[i].section.replace("P_", "Estacionamiento ") + "</div>";
			html += "<p>Lugares Disponibles: " + (data[i].max - (data[i].max - data[i].capacity)).toString() + "</p>";
			html += "<p>Ocupación: " + percentage + "%</p>"
			html += "</div>"
			html += "</div>"
			html += "</div>";
		}
		console.log('Refreshing')
		$('#cards-container').html(html);
```
In the next section _About Us_ we have a short description of what Parkify is as well as what our objective is, followed by all the members in the team. Also in this page, a short video is includedin which we present the way the problem parkify is trying to solve and the solution we are offering. The last section, _Documentation_, holds a list of all the available commands that can be given to the application and what each of these is for, making it easy of the user to navigate and work in a way he sees fit.

###__Model__
_A complementar_



