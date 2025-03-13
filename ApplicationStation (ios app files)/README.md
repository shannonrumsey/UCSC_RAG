# ApplicationStation  

This repository contains all the code necessary to connect the RAG model to our iOS app.  

## Usage  

To use this application, you must obtain an API key from Gemini and store it in a file named `secrets.plist`. Additionally, the app is registered with Firebase for backend services.  

The app uses a Flask API to connect to the RAG model locally. To set this up:  
1. Ensure Flask is installed in your Python environment.  
2. Run `local_api.py` from the root of the repository.  

## Repository Structure 

ApplicationStation/  
│── ApplicationStation/                # iOS project files  
│   ├── ApplicationStation/  
│   │   ├── Assets.xcassets/  
│   │   ├── PreviewContent/  
│   │   ├── GeminiAPI.swift            # Contains all code related to fetching responses from Gemini API
│   │   ├── RagChat.swift              # Contains code for the UI interface where the user interacts with our model
│   │   ├── RagAPI.swift               # Contains API calls to our local model
│   │   ├── SecretsFile.swift          # Connects to secrets.plist (not included in repo) to get our Gemini API key
│   │   ├── DataManager.swift          # Contains backend code related to storing and fetching messages from FireBase
│   │   ├── AuthManager.swift          # Contains all code regarding user authentication 
│   │   ├── LoginView.swift            # Contains the UI for the login screen
│   │   ├── CreateAccount.swift        # Contains UI for create account screen
│   │   ├── MessageStruct.swift        # Contains code for the message struct (how messages are stored in Firebase)
│   ├── ApplicationStationTests/  
│   ├── ApplicationStationUITests/  
│   ├── ApplicationStation.xcodeproj/   
│── README.md 
