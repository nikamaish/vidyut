# Flask Firestore Data Generator

This project is a Flask application that generates random data entries and stores them in a Firestore database. It also provides an API to retrieve the stored data in JSON format.

## Features

- **Background Data Generation**: Continuously generates random data entries and stores them in Firestore every 5 seconds.
- **Data Retrieval**: Provides an API endpoint to retrieve all data entries from Firestore in JSON format.

## Requirements

- Python 3.6+
- Flask
- Firebase Admin SDK
- `requests` library (optional, for testing with Python)
- A Firebase project with Firestore enabled

## Setup

### 1. Clone the Repository

```sh
git clone https://github.com/yourusername/flask-firestore-data-generator.git
cd flask-firestore-data-generator



```
curl -X POST http://127.0.0.1:5000/add_data
```


```
curl -X GET http://127.0.0.1:5000/get_data
```
