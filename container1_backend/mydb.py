import json
import os

class Database:
    def __init__(self, filename="/app/data/database.json"):  # Default to a path inside the container
        self.filename = filename

        # If the file doesn't exist, create an empty JSON file
        if not os.path.exists(self.filename):
            with open(self.filename, "w") as f:
                json.dump({}, f)

    def add_data(self, email, password):
        with open(self.filename, "r") as f:
            data = json.load(f)

        if email in data:
            return False
        else:
            data[email] = password
            with open(self.filename, "w") as f:
                json.dump(data, f)
            return True

    def validate_credentials(self, email, password):
        with open(self.filename, "r") as f:
            data = json.load(f)

        return data.get(email) == password
