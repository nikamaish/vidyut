# Flask Firestore Data Generator

This project is a Flask application that generates random data entries and stores them in a Firestore database. It also provides an API to retrieve the stored data in JSON format.

## Features

- **Background Data Generation**: Continuously generates random data entries and stores them in Firestore every 5 seconds.
- **Data Retrieval**: Provides an API endpoint to retrieve all data entries from Firestore in JSON format.

## Requirements

- Python 3.6+
- Flask
- Firebase Admin SDK
- A Firebase project with Firestore enabled

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/nikamaish/vidyut.git
```

### 2. Create a Virtual Environment and Install Dependencies
```sh
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Firebase Setup
Go to the Firebase Console and create a new project (or use an existing one).
Enable Firestore in your Firebase project.
Generate a private key for the Firebase Admin SDK and download the JSON file.
Save the JSON file in the root directory of your project and rename it to serviceAccountKey.json.


### 4. Run the Flask Application
```sh
python app.py
```

The application should now be running on http://127.0.0.1:5000.
## 1. Start Data Generation
Endpoint: /add_data
Method: POST
Starts the background task to generate and add data to Firestore every 5 seconds.

```sh
curl -X POST http://127.0.0.1:5000/add_data
```

## 2. Retrieve Data
Endpoint: /get_data
Method: GET
Retrieves all data entries from Firestore in JSON format.

```sh
curl -X GET http://127.0.0.1:5000/get_data
```


## How to Use
Start the Flask Application: Run the application using python app.py.
Start Data Generation: Send a POST request to /add_data to start generating and storing data.
Retrieve Data: Send a GET request to /get_data to retrieve all stored data in JSON format.
