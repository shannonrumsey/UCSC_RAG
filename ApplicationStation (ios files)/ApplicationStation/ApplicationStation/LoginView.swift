//
//  LoginView.swift
//  ApplicationStation
//
//  Created by Darian Lee on 3/8/25.
//

import SwiftUI

struct LoginView: View {
    @State private var email: String = ""
    @State private var password: String = ""
    @State private var showAlert: Bool = false
    @State private var alertMessage: String = ""
    
    @EnvironmentObject var authManager: AuthManager
    let lightBlue = Color(red: 173/255, green: 255/255, blue: 255/255)

    var body: some View {
        ZStack {
            Color.black.ignoresSafeArea()
            
            VStack(spacing: 20) {
                Text("Login")
                    .font(.largeTitle)
                    .foregroundColor(lightBlue)
                    .bold()
                
                TextField("Email", text: $email)
                    .padding()
                    .background(lightBlue.opacity(0.2))
                    .cornerRadius(8)
                    .foregroundColor(lightBlue)
                    .keyboardType(.emailAddress)
                    .autocapitalization(.none)
                    .disableAutocorrection(true)
                
                SecureField("Password", text: $password)
                    .padding()
                    .background(lightBlue.opacity(0.2))
                    .cornerRadius(8)
                    .foregroundColor(lightBlue)
                    .autocapitalization(.none)
                    .disableAutocorrection(true)
                
                Button(action: {
                    authManager.signIn(email: email, password: password) { success in
                        if !success {
                            alertMessage = "Invalid email or password."
                            showAlert = true
                        } else {
                            print("👩🏻‍🦰", authManager.user)
                        }
                    }
                }) {
                    Text("Login")
                        .frame(maxWidth: .infinity)
                        .padding()
                        .background(lightBlue)
                        .foregroundColor(.black)
                        .cornerRadius(8)
                }
                
              
            }
            .padding()
            .alert(isPresented: $showAlert) {
                Alert(title: Text("Login Failed"), message: Text(alertMessage), dismissButton: .default(Text("OK")))
            }
        }
    }
}

#Preview {
    LoginView()
        .environmentObject(AuthManager()) // Correct preview setup
}
