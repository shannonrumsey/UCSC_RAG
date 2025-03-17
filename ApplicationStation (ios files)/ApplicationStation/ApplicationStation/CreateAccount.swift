import SwiftUI

struct CreateAccount: View {
    @State private var email: String = ""
    @State private var password: String = ""
    @EnvironmentObject var authManager: AuthManager

    let lightBlue = Color(red: 173/255, green: 255/255, blue: 255/255)
    
    let images = ["outside", "break_room", "yellow_room", "hallway"]
    @State private var currentIndex = 0
        
        // Таймер для автоматической смены изображений
        let timer = Timer.publish(every: 3, on: .main, in: .common).autoconnect()

        var body: some View {
            NavigationView {
                ZStack {
                    Color.black
                        .ignoresSafeArea()
                    
                    VStack() {
                        // Карусель изображений с автоматическим переключением
                        TabView(selection: $currentIndex) {
                            ForEach(0..<images.count, id: \.self) { index in
                                Image(images[index])
                                    .resizable()
                                    .scaledToFill()
                                    .frame(width: UIScreen.main.bounds.width, height: 250)
                                    //.clipShape(RoundedRectangle(cornerRadius: 25)) // Круглые углы

                                    .clipped()
                                    .tag(index)  // Устанавливаем тег для каждого изображения
                            }
                        }
                        .tabViewStyle(PageTabViewStyle())
                        .frame(height: 200)
                        .cornerRadius(25)
                        .onReceive(timer) { _ in
                            // Логика автопереключения
                            withAnimation {
                                currentIndex = (currentIndex + 1) % images.count
                            }
                        }
                    
   
                    Text("Welcome to the ApplicationStation")
                        .font(.largeTitle)
                        .fontWeight(.bold)
                        .foregroundColor(.yellow)
                        .multilineTextAlignment(.center)
                        .padding()
                    
                    Text("UCSC NLP's central application hub")
                        .font(.headline)
                        .foregroundColor(lightBlue)
                        .multilineTextAlignment(.center)
                    
                    NavigationLink(destination: LoginView()) {
                        Text("Login")
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(lightBlue)
                            .foregroundColor(.black)
                            .cornerRadius(10)
                    }
                    .padding(.horizontal)
                    
                    Text("Sign Up")
                        .font(.title2)
                        .fontWeight(.semibold)
                        .foregroundColor(.yellow)
                        .padding(.top, 20)
                    
                    TextField("Email", text: $email)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                        .padding(.horizontal)
                        .background(Color.black)
                        .foregroundColor(.black)
                    
                    SecureField("Password", text: $password)
                        .textFieldStyle(RoundedBorderTextFieldStyle())
                        .padding(.horizontal)
                        .background(Color.black)
                        .foregroundColor(.black)
                    
                    Button(action: {
                        // Sign-up action
                        authManager.signUp(email: email, password: password) { error in
                            if let error = error {
                                print(error)
                            } else {
                                // After successful sign-up, you can call sign-in
                                authManager.signIn(email: email, password: password) { success in
                                    if !success {
                                        print("Sign-in failed")
                                    } else {
                                        print("👩🏻‍🦰", authManager.user)
                                    }
                                }
                            }
                        }
                    }) {
                        Text("Create Account")
                            .frame(maxWidth: .infinity)
                            .padding()
                            .background(Color.yellow)
                            .foregroundColor(.black)
                            .cornerRadius(10)
                    }
                    .padding(.horizontal)
                }
                .padding()
                .background(Color.black.edgesIgnoringSafeArea(.all))
            }
        }
    }
}

#Preview {
    CreateAccount()
        .environmentObject(AuthManager()) // Correct preview setup
}
