from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import threading
import time

app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()

def add_data_to_firestore(data_entries):
    try:
        # Create a new collection named 'entries'
        collection_ref = db.collection('entries')

        # Add each main data entry to Firestore
        for main_entry in data_entries:
            # Generate a list of 5 sub-entries with timestamps
            sub_entries = []
            for i in range(5):
                sub_entry = {
                    'sub_entry_id': f'sub_entry_{i+1}',
                    'data': f'This is sub entry {i+1} of {main_entry["main_entry_id"]}',
                    'timestamp': datetime.now()
                }
                sub_entries.append(sub_entry)

            # Add the main entry with sub-entries to Firestore
            main_entry_data = {
                'main_entry_id': main_entry['main_entry_id'],
                'sub_entries': sub_entries,
                'timestamp': datetime.now()
            }
            collection_ref.add(main_entry_data)

        return {"success": True, "message": "Data added successfully"}

    except Exception as e:
        return {"success": False, "message": str(e)}

def generate_random_data():
    data = []
    main_entry_names = ['entry_name_1', 'entry_name_2', 'entry_name_3', 'entry_name_4', 'entry_name_5']
    for name in main_entry_names:
        main_entry = {
            'main_entry_id': name
        }
        data.append(main_entry)
    return {'data': data}

def background_task():
    while True:
        random_data = generate_random_data()
        add_data_to_firestore(random_data['data'])
        time.sleep(5)

@app.route('/')
def hello():
    return "It works!"

@app.route('/add_data', methods=['POST'])
def start_background_task():
    try:
        # Start the background task in a separate thread
        thread = threading.Thread(target=background_task)
        thread.daemon = True
        thread.start()
        return jsonify({"success": True, "message": "Data added successfully"}), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
