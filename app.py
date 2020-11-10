from flask import Flask, request, Response
import json
import random

app = Flask(__name__)
animal_list = ["Monkey", "Cat", "Tiger", "Loin", "Horse", "Elephant", "Cow", "Sheep", "Zebra", "Owl"]

@app.route("/animals", methods=["GET", "POST", "PATCH", "DELETE"])
def animals():
    if request.method == "GET":
        r_number=random.randrange(len(animal_list))
        random_animal=animal_list[r_number]
        return Response(json.dumps(animal_list, default=str), mimetype="application/json", status=200)

    elif request.method == "POST":
        animal_list.append("Snake")
        return Response("Added Snake to the list", mimetype = "text/html", status=201)
    
    elif request.method == "PATCH":
        animal_list.remove("Owl")
        animal_list.insert(10,"Snowy Owl")
        return Response("Owl is changed to Snowy Owl", mimetype="text/html", status=201)
    
    elif request.method == "DELETE":
        animal_list.remove("Monkey")
        return Response("Oh! Monkey is no more in the animal's list", mimetype="text/html", status=201)
    else:
        return Response("Something went wrong...", mimetype="text/html", status=201)