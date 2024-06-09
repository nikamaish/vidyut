from flask import Flask, request, jsonify
import firebase_admin
from firebase_admin import credentials, firestore
from datetime import datetime
import threading
import time
import pytz
from data_generator import generate_random_data  # Import the function

app = Flask(__name__)

# Initialize Firestore DB
cred = credentials.Certificate('serviceAccountKey.json')
firebase_admin.initialize_app(cred)
db = firestore.client()
timezone = pytz.timezone('Asia/Kolkata')

def add_data_to_firestore(data_entries):
    try:
        # Create a new collection named 'entries'
        collection_ref = db.collection('entries')

        # Add each main data entry to Firestore
        for main_entry in data_entries:
            # Generate a list of 5 sub-entries
            sub_entries = []
            for i in range(5):
                sub_entry = {
                    'sub_entry_id': f'sub_entry_{i+1}',
                    'data': f'This is sub entry {i+1} of {main_entry["main_entry_id"]}',
                }
                sub_entries.append(sub_entry)

            # Create a Unix timestamp-based document ID
            timestamp = int(time.time())
            main_entry_data = {
                'main_entry_id': main_entry['main_entry_id'],
                'sub_entries': sub_entries,
                'timestamp': datetime.now(timezone)
            }

            # Add the main entry with sub-entries to Firestore using the Unix timestamp as the document ID
            collection_ref.document(str(timestamp)).set(main_entry_data)

        return {"success": True, "message": "Data added successfully"}

    except Exception as e:
        return {"success": False, "message": str(e)}

def background_task():
    while True:
        # Generate and add 5 main entries
        random_data = generate_random_data()
        add_data_to_firestore(random_data['data'][:5])
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

@app.route('/get_data', methods=['GET'])
def get_data():
    try:
        # Fetch data from Firestore
        collection_ref = db.collection('entries')
        docs = collection_ref.stream()

        # Prepare the data to be returned as JSON
        entries = []
        for doc in docs:
            doc_dict = doc.to_dict()
            doc_dict['id'] = doc.id  # Include the document ID
            entries.append(doc_dict)

        return jsonify({"success": True, "data": entries}), 200

    except Exception as e:
        return jsonify({"success": False, "message": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
