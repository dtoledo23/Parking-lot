import openalpr_api


apiclient = openalpr_api.DefaultApi()
plates_image = "plates4.jpg"
response = apiclient.recognize_post("sk_DEMODEMODEMODEMODEMODEMO", "plate,color,make,makemodel", image=plates_image, country="mx")


for plate_obj in response.plate.results:
	print "Plate:      %s - %f percent" % (plate_obj.plate, plate_obj.confidence)

print "Color:      %s - %f percent" % (response.color[0].value, response.color[0].confidence)
print "Make:       %s - %f percent" % (response.make[0].value, response.make[0].confidence)
print "Make-model: %s - %f percent" % (response.makemodel[0].value, response.makemodel[0].confidence)

