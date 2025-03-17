//
//  MessageStruct.swift
//  ApplicationStation
//
//  Created by Darian Lee on 3/8/25.
//

import Foundation
import FirebaseFirestore


// This is the format our conversations with the Rag agent will be stored in 
struct Message: Hashable{
    var message: String
    var timeStamp: Timestamp
    init(message: String, timeStamp: Timestamp) {
            self.message = message
            self.timeStamp = timeStamp
        }
}
