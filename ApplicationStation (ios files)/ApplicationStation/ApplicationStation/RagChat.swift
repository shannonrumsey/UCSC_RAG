import SwiftUI
import FirebaseFirestore

struct RagChat: View {
    @EnvironmentObject var authManager: AuthManager
    @EnvironmentObject var dataManager: DataManager
    @State private var userMessage: String = ""
    @State private var isLoading: Bool = false
    @State private var showError: Bool = false
    @State private var errorMessage: String = ""
    @State private var errorTitle: String = "Error"
    @State private var goToForum: Bool = false
    
    let lightBlue = Color(red: 173/255, green: 255/255, blue: 255/255)
    
    var body: some View {
        ZStack {
     
            Color.black.ignoresSafeArea()
            
            VStack {
        
                HStack {
                    Button(action: {
                        authManager.signOut()
                    }) {
                        Text("Logout")
                            .padding()
                            .foregroundColor(.white)
                    }
                    Spacer()
                    Button(action: {
                        print("Forum tapped")
                    }) {
                        Text("Forum")
                            .padding()
                            .foregroundColor(.white)
                    }
                }
                .padding(.top, 40)
                .padding(.horizontal)
                
       
                ScrollView {
                    VStack(alignment: .leading) {
                        ForEach(dataManager.messages, id: \ .self) { message in
                            HStack(alignment: .bottom) {
                                Text(message.message)
                                    .padding()
                                    .foregroundColor(lightBlue)
                                    .background(message.message.starts(with: "User") ? Color.gray.opacity(0.3) : Color.clear)
                                    .cornerRadius(10)
                                Spacer()
                                Text(formatTimestamp(message.timeStamp))
                                    .font(.caption)
                                    .foregroundColor(.gray)
                                    .padding(.trailing, 10)
                            }
                            .padding(.bottom, 5)
                        }
                    }
                    .padding(.top, 80)
                    .padding(.horizontal)
                }
                
           
                HStack {
                    TextField("Ask a question...", text: $userMessage)
                        .padding()
                        .background(Color.white.opacity(0.3))
                        .cornerRadius(10)
                        .foregroundColor(.white)
                        .padding(.horizontal)
                    
                    Button(action: {
                        if !userMessage.isEmpty {
                            isLoading = true
                            let newMessage = Message(message: "User: " + userMessage, timeStamp: Timestamp(date: Date()))
                            
                            RagAPI.askQuestion(question: newMessage.message) { answer, context in
                                let cleanAnswer = (answer ?? "")
                                    .replacingOccurrences(of: "Answer: ", with: "")
                                    .replacingOccurrences(of: "User:", with: "")
                                    .replacingOccurrences(of: "A:", with: "")
                                    .replacingOccurrences(of: "Agent:", with: "")
                                let newAnswer = Message(message: "AI: " + cleanAnswer, timeStamp: Timestamp(date: Date()))
                                
                                GeminiAPI.callGeminiAPI(question: newMessage.message, answer: newAnswer.message, context: context ?? "") { isCorrect, explanation in
                                    isLoading = false
                                    
                                    guard let isCorrect = isCorrect, let explanation = explanation else {
                                        goToForum = true
                                        return
                                    }
                                    
                                    if isCorrect == 1  {
                                        dataManager.saveMessages(messages: [newMessage, newAnswer]) {
                                            dataManager.loadMessages {
                                                userMessage = ""
                                            }
                                        }
                                    } else if isCorrect == 0 {
                                        goToForum = true

                                    } else if isCorrect == -1 {
                                        errorMessage = "Your prompt was detected as containing inappropriate or biased content. UCSC respects students of all nationalities, religions, orientations, genders, and backgrounds. Please ensure that your prompt aligns with our community guidelines and promotes inclusivity and respect."
                                        errorTitle = "❗️Inappropriate content detected❗️"
                                        showError = true
                                    }
                                }
                            }
                        }
                    }) {
                        Text("Send")
                            .padding()
                            .foregroundColor(.black)
                            .background(lightBlue)
                            .cornerRadius(10)
                            .padding(.trailing)
                    }
                }
                .padding(.bottom)
            }
            .onAppear {
                dataManager.loadMessages{
                    
                }
            }
            
            if goToForum {
                ZStack {
                    Color.black.opacity(0.6).edgesIgnoringSafeArea(.all) // затемнение фона
                    
                    VStack(spacing: 20) {
                        Text("The model does not have information about this question.")
                            .font(.headline)
                            .multilineTextAlignment(.center)
                            .foregroundColor(.black)
                        
                        Text("Consider asking in a forum for more insights.")
                            .font(.subheadline)
                            .multilineTextAlignment(.center)
                            .foregroundColor(.black)
                        
                        Button(action: {
                           print("went to forum")
                            goToForum = false
                            }
                        ) {
                            Text("Go to Forum")
                                .font(.headline)
                                .foregroundColor(.white)
                                .padding()
                                .frame(width: 200)
                                .background(Color.black)
                                .cornerRadius(10)
                        }
                    }
                    .padding()
                    .background(Color.white)
                    .cornerRadius(12)
                    .shadow(radius: 10)
                    .frame(width: 300)
                }
            }

            if isLoading {
                ZStack {
                    Color.black.opacity(0.6).edgesIgnoringSafeArea(.all)
                    ProgressView("Loading answer...")
                        .progressViewStyle(CircularProgressViewStyle(tint: Color.black))
                        .padding()
                        .background(Color.gray.opacity(1))
                        .cornerRadius(10)
                        .shadow(radius: 5)
                        .font(.headline)
                        .foregroundColor(.black)
                        .frame(width: 250, height: 100)
                }
            }
        }
        .alert(isPresented: $showError) {
            Alert(title: Text("Error"), message: Text(errorMessage), dismissButton: .default(Text("OK")))
        }
    }
    
    private func formatTimestamp(_ timestamp: Timestamp) -> String {
        let date = timestamp.dateValue()
        let formatter = DateFormatter()
        formatter.dateFormat = "HH:mm"
        return formatter.string(from: date)
    }
}

#Preview {
    RagChat()
        .environmentObject(AuthManager())
        .environmentObject(DataManager())
}

