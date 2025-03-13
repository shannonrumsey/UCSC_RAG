//
//  DataManager.swift
//  ApplicationStation
//
//  Created by Darian Lee on 3/8/25.
//

import Foundation
import Foundation
import FirebaseFirestore
import FirebaseAuth
import FirebaseCore
import SwiftUI



class DataManager: ObservableObject {
    let database: Firestore
    @Published var messages: [Message] = [] // fetched messages sorted by time
    
    
    init(){
        
        self.database = Firestore.firestore()
    }
    
    // for getting all the messages as a list sorted by timestamp
    func loadMessages(completion: @escaping () -> Void){
        guard var userID = Auth.auth().currentUser?.uid else {
            print("no user id found inside func getLanguages()")
            completion()
            return
        }
        
       
        
        database.collection("Users").document(userID).collection("RagMessages")
            .order(by: "timestamp")
            .addSnapshotListener { querySnapshot, error in
                guard let documents = querySnapshot?.documents else {
                    print("Error fetching documents: \(String(describing: error))")
                    return
                }
                
                var messages: [Message] = []
                for document in documents {
                    print(document)
                    let data = document.data()
                    if let messageText = data["message"] as? String,
                       let timestamp = data["timestamp"] as? Timestamp {
                        let message = Message(message: messageText, timeStamp: timestamp)
                        messages.append(message)
                        
                    }
                    
                    
                }
                print("messages loaded")
                self.messages = messages
                print(self.messages)
                completion()
                
                
            }
    }
    
    
    // gets the list of messages under Users/user_id/RagMessages
    //appends the given message to the list
    // saves the list
    func saveMessages(messages:[Message], completion: @escaping () -> Void){
        guard var userID = Auth.auth().currentUser?.uid else {
            print("no user id found")
            completion()
            return
        }
        
        for message in messages{
            
            let messageData: [String: Any] = [
                "message": message.message,
                "timestamp": message.timeStamp
            ]
            database.collection("Users").document(userID).collection("RagMessages")
                .addDocument(data: messageData) { error in
                    if let error = error {
                        print("Error saving message: \(error)")
                    } else {
                        print("Message saved successfully")
                    }
                    completion()
                }
        }
    }
        
        
        
        
    
}
