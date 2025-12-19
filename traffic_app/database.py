from pymongo import MongoClient
from traffic_app.config import MONGO_URL, DATABASE_NAME

client = MongoClient(MONGO_URL)
db = client[DATABASE_NAME]

vehicle_logs = db["vehicle_logs"]
accident_logs = db["accident_logs"]
signal_logs = db["signal_logs"]
stolen_vehicles = db["stolen_vehicles"]
