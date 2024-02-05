import json
import os
import pickle


FILENAME = "trains.dat"
# Find the folder of this script
script_dir = os.path.dirname(os.path.abspath(__file__))
# Form the path to the file located in this folder
file_path = os.path.join(script_dir, FILENAME)

# Create the file if it doesn't exist
if not os.path.exists(file_path):
    open(file_path, "x")


def get_data():
    data = {}
    with open(file_path, "rb") as file:
        try:
            data = pickle.load(file)
        except EOFError:
            pass
    return data


def save_data(data):
    with open(file_path, "wb") as file:
        pickle.dump(data, file)


def add_train(*, name, _from, to, time):
    """Add train infromation to the data"""

    data = get_data()
    _id = len(data)
    data[_id] = {"name": name, "from": _from, "to": to, "time": time}
    save_data(data)


name = input("Enter the name of the train: ")
_from = input("Enter FROM: ")
to = input("Enter TO: ")
time = input("Enter the time of departure: ")
print()

add_train(name=name, _from=_from, to=to, time=time)

print("All available trains:")
print(json.dumps(get_data(), indent=4))
