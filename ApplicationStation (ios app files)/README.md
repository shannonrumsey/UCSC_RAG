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
│   │   ├── GeminiAPI.swift            
│   │   ├── RagChat.swift              
│   │   ├── RagAPI.swift               
│   │   ├── SecretsFile.swift          
│   │   ├── DataManager.swift          
│   │   ├── AuthManager.swift          
│   │   ├── LoginView.swift            
│   │   ├── CreateAccount.swift        
│   │   ├── MessageStruct.swift        
│   ├── ApplicationStationTests/  
│   ├── ApplicationStationUITests/  
│   ├── ApplicationStation.xcodeproj/   
│── README.md 


### File Descriptions  

- **GeminiAPI.swift** – Contains all code related to fetching responses from the Gemini API.  
- **RagChat.swift** – Contains code for the UI interface where users interact with the model.  
- **RagAPI.swift** – Handles API calls to the local RAG model.  
- **SecretsFile.swift** – Connects to `secrets.plist` (not included in the repo) to retrieve the Gemini API key.  
- **DataManager.swift** – Backend logic for storing and fetching messages from Firebase.  
- **AuthManager.swift** – Manages user authentication.  
- **LoginView.swift** – UI for the login screen.  
- **CreateAccount.swift** – UI for the account creation screen.  
- **MessageStruct.swift** – Defines the structure for storing messages in Firebase.  
