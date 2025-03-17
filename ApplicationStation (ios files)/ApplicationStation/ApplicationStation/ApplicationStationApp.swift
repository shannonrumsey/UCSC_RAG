//
//  ApplicationStationApp.swift
//  ApplicationStation
//
//  Created by Darian Lee on 3/8/25.
//

import SwiftUI
import FirebaseCore
@main

struct ApplicationStationApp: App {
    init() { // <-- Add an init
        FirebaseApp.configure() // <-- Configure Firebase app
    }
    @StateObject private var authManager = AuthManager()
    @StateObject private var dataManager = DataManager()
    var body: some Scene {
        WindowGroup {
            if authManager.user != nil {
                RagChat()
                    .environmentObject(authManager)
                    .environmentObject(dataManager)
            }
            else{
                CreateAccount()
                    .environmentObject(authManager)
                    //.environmentObject(dataManager)
            }
        }
    }
}
