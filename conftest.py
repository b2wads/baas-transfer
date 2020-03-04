import json
import os

ENV = "TEST"
os.environ["ENV"] = ENV

VALUES = {"ACCOUNT_SERVICE_ADDRESS": "http://accounts.api"}


for name, value in VALUES.items():
    os.environ[f"{ENV}_{name}"] = os.getenv(f"{ENV}_{name}", value)

assert os.environ["ENV"] == "TEST"
