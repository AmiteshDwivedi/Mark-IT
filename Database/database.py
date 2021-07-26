import pyrebase

config = {
    "apiKey": "AIzaSyBttgLVbtWWdtRhos39BzbqvQZDIJaIe5U",
    "authDomain": "mark-it-ec28b.firebaseapp.com",
    # firebase storage
    # "databaseURL": "gs://mark-it-ec28b.appspot.com",
    # firebase realtime database
    "databaseURL": "https://mark-it-ec28b-default-rtdb.firebaseio.com",
    "projectId": "mark-it-ec28b",
    "storageBucket": "mark-it-ec28b.appspot.com",
    "messagingSenderId": "187768173767",
    "appId": "1:187768173767:web:e9ba36b17e9112fc6cfae2",
    "measurementId": "G-42HYDHB4Q1"
}

firebase = pyrebase.initialize_app(config)

# firebase storage

# storage = firebase.storage()
#
# path_on_cloud = "Attendance/Attendance.csv"
# path_local = "Attendance.csv"
# storage.child(path_on_cloud).put(path_local)


# firebase realtime database

db = firebase.database()
data = {'age': 40, 'address': "New York", 'employed': True, 'Name': 'Gaurav'}
db.push(data)