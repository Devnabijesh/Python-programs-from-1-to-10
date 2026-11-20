import json

data = '''
[
    {"city": "Chennai", "temperature": 32, "humidity": 70},
    {"city": "Delhi", "temperature": 28, "humidity": 60},
    {"city": "Mumbai", "temperature": 30, "humidity": 80}
]
'''

weather = json.loads(data)

print("Weather Report")

for city in weather:
    print("\nCity:", city["city"])
    print("Temperature:", city["temperature"], "°C")
    print("Humidity:", city["humidity"], "%")