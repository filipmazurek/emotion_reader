import requests

# send HTTP request to IFTTT to fire an event
event_name = "emotionExample"
f = open("webhook_key.txt", 'r')
key = f.read(22)
r = requests.post("https://maker.ifttt.com/trigger/" + event_name + "/with/key/" + key)
