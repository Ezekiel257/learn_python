import os
import json
import csv
import time

# Define the directory where your JSON files are located
ABSOLUTE_PATH = r"C:\Users\HP\Desktop\Data-Engineering-with-ALTSchool\Assessment\fintech"
CARDS_PATH = "events/cards"
USERS_PATH = "events/users"


def load_json_data(folder_path):
    data_list = []

    # Iterate through the files in the directory
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        # Load the JSON data from the file
        with open(file_path, 'r') as json_file:
            data = json.load(json_file)

        # flatten json data
        payload = data['payload']
        metadata = data['metadata']

        flattened_data = {
            **payload,
            **metadata,
            'type': payload.get('type'),  # Ensure type is included
            'event_id': metadata.get('event_id'),
            'event_at': metadata.get('event_at'),
        }

        data_list.append(flattened_data)

    return data_list


def store_data_as_json(data, output_filename):
    # Dump data into a json file
    with open(output_filename, 'w') as json_file:
        json.dump(data, json_file)


def process_data_to_csv(data, csv_filename):
    # Open the CSV file for writing
    with open(csv_filename, 'w', newline='') as csvfile:
        # Create a CSV writer object
        csv_writer = csv.writer(csvfile)

        # Write the header row
        header = data[0].keys()
        csv_writer.writerow(header)

        # Write the data rows
        for item in data:
            csv_writer.writerow(item.values())

    print(f"Data has been successfully converted to CSV and saved in {csv_filename}")


def main():
    # Load users data
    users_data = load_json_data(os.path.join(ABSOLUTE_PATH, USERS_PATH))
    store_data_as_json(users_data, 'users_data.json')
    process_data_to_csv(users_data, 'users_data.csv')

    # Load cards data
    cards_data = load_json_data(os.path.join(ABSOLUTE_PATH, CARDS_PATH))
    store_data_as_json(cards_data, 'cards_data.json')
    process_data_to_csv(cards_data, 'cards_data.csv')


if __name__ == "__main__":
    main()
