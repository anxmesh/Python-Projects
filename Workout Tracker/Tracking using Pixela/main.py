import requests
from datetime import datetime

# Change the username and token to your own token of choice; token must be between 8-128 characters long
pixela_endpoint = "https://pixe.la/v1/users"
pixela_token = "YOUR TOKEN HERE"
USERNAME = "YOUR USERNAME HERE"
GRAPH_ID = "graph1"

Headers = {
    "X-USER-TOKEN": pixela_token
}

# Creating a user on Pixela
user_params ={
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# Run this line to create your own user; run it only once, and then comment out
response = requests.post(url=pixela_endpoint, json=user_params)
print(response.text)


# Creating a graph
graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config ={
    "id": GRAPH_ID,
    "name": "Workout Tracker",
    "unit": "Mins",
    "type": "float",
    "color": "momiji"
}

# run this line to create your own graph; run it once whenever you wish to create a graph, and then comment out until
# needed again
graph_response = requests.post(url=graph_endpoint, json=graph_config, headers=Headers)
print(graph_response.text)

# Visit the following link to view the graph: https://pixe.la/v1/users/animeshupreti/graphs/graph1.html
# Change the USERNAME and GRAPHID to your own username and graph ID



# Adding a pixel/entry to the graph
entry_endpoint= f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}"

today = datetime.now()

entry_config = {
    "date": today.strftime("%Y%m%d"),
    "quantity": "54",
}

#run this line to enter pixels onto the graph as required. Change the data in 'entry_config' as required.
entry_response = requests.post(url=entry_endpoint, json=entry_config, headers=Headers)
print(entry_response.text)



# Modifying/updating an entry/pixel
update_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

updated_config = {
    "quantity": "55"
}

# run this line to update the pixel on the date specified in 'today'. Change as required
modify_response = requests.put(url=update_endpoint, json=updated_config, headers=Headers)
print(modify_response.text)


# Deleting an entry/pixel
delete_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs/{GRAPH_ID}/{today.strftime('%Y%m%d')}"

# run this line to del3te the pixel on the date specified in 'today'. Change
delete_response = requests.delete(url=update_endpoint, headers=Headers)
print(delete_response.text)
