import pyrebase
import firebase_admin
from firebase_admin import credentials, firestore

firebaseConfig = {
  'apiKey': "AIzaSyAClsdr7MwNndWFc7_L-BlZRNLeMjsxxxQ",
  'databaseURL': "https://bilimdi-platform.firebaseio.com",
  'authDomain': "edication-ce7a0.firebaseapp.com",
  'projectId': "edication-ce7a0",
  'storageBucket': "edication-ce7a0.firebasestorage.app",
  'messagingSenderId': "336523450386",
  'appId': "1:336523450386:web:c63104c263520f594c60cb",
  'measurementId': "G-GLKBYPXMPC"
}

firebase = pyrebase.initialize_app(firebaseConfig)
auth = firebase.auth()

cred = credentials.Certificate("/Users/nazerke/Desktop/bilimdi_platforma/edu_platform/edication-ce7a0-firebase-adminsdk-fbsvc-b596336647.json")
firebase_admin.initialize_app(cred)
db = firestore.client()
