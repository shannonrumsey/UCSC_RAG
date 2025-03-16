//
//  AuthManager.swift
//  ApplicationStation
//
//  Created by Darian Lee on 3/8/25.
//



import Foundation
import FirebaseAuth

class AuthManager: ObservableObject{ // Conform to ObservableObject

    @Published var user: User? = nil


    init() {

        self.user = Auth.auth().currentUser

 
                Auth.auth().addStateDidChangeListener { _, user in
                    self.user = user
                }
            
    }

    // https://firebase.google.com/docs/auth/ios/start#sign_up_new_users
    func signUp(email: String, password: String, completion: @escaping (Error?) -> Void) {
        Task {
            do {
                let authResult = try await Auth.auth().createUser(withEmail: email, password: password)
                DispatchQueue.main.async {
                    self.user = authResult.user // Update @Published property
                    completion(nil)
                }
            } catch {
                DispatchQueue.main.async {
                    completion(error)
                }
            }
        }
    }

    // https://firebase.google.com/docs/auth/ios/start#sign_in_existing_users
    func signIn(email: String, password: String, completion: @escaping (Bool) -> Void) {
            Task {
                do {
                    let authResult = try await Auth.auth().signIn(withEmail: email, password: password)
                    DispatchQueue.main.async {
                        self.user = authResult.user // Update @Published property
                        completion(true)
                    }
                } catch {
                    print(error)
                    DispatchQueue.main.async {
                        completion(false)
                    }
                }
            }
        }
    

    func signOut() {
        do {
            try Auth.auth().signOut()
            DispatchQueue.main.async {
                self.user = nil // Update @Published property
            }
        } catch {
            print(error)
        }
    }
}
