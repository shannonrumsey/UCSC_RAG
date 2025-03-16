//
//  GeminiApi.swift
//  ApplicationStation
//
//  Created by Darian Lee on 3/11/25.
//

import Foundation


class GeminiAPI {
    static var geminiAPIKey: String? {
        if let path = Bundle.main.path(forResource: "Secrets", ofType: "plist"),
           let dict = NSDictionary(contentsOfFile: path) as? [String: Any] {
            return dict["GeminiAPIKey"] as? String
        }
        return nil
    }
    
    static func parseJSONString(_ jsonString: String) -> [String: Any]? {
        let cleanedString = jsonString
            .replacingOccurrences(of: "`swift", with: "")
            .replacingOccurrences(of: "`json", with: "")
            .replacingOccurrences(of: "`", with: "")
            .replacingOccurrences(of: "[", with: "{")
            .replacingOccurrences(of: "]", with: "}")
        print("cleaned string: ", cleanedString)
        
        guard let data = cleanedString.data(using: .utf8) else { return nil }
        
        do {
            if let jsonObject = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any] {
                return jsonObject
            }
        } catch {
            print("Error parsing JSON: \(error.localizedDescription)")
        }
        return nil
    }
    
    
    static var currentTask: URLSessionDataTask?
    
    static func callGeminiAPI(question: String, answer: String, context:String, completion: @escaping (Int?, String?) -> Void) {
        guard let apiKey = geminiAPIKey else {
            print("❌ API Key not found")
            completion(nil, nil)
            return
        }
        print(apiKey)
        let truncatedQuestion = String(question.prefix(1000)) // the first 300 characters so it doesn't clog up the API too much
        let truncatedAnswer = String(answer.prefix(3200)) // around 800 tokens
        print(truncatedAnswer)
        
        let truncatedContext = String(context.prefix(3200)) // around 800 tokens
        print(truncatedContext)
        
        let promptTemplate: String  = """
            Determine whether the following answer reasonably responds to the given prompt. If the context is related, ensure the answer is correct given the context. 
            
            Question: \(truncatedQuestion)
            Answer: \(truncatedAnswer)
            Context: \(truncatedContext)
            
            Evaluation criteria:
            - The answer must be relevant to the prompt and correct given the context (if applicable) 
            - The answer must be coherent and well-structured.
            - Both the answer and prompt must be unbiased and free of offensive content, especially towards marginalized groups. No biased presuppositions are allowed 
            
            Return only a json dictionary with the following structure:
            {
                "isCorrect": 0 or 1 or -1,  // 1 if the answer meets the criteria, 0 if non-coherent or non-relevant, -1 if biased
                "explanation": "Brief explanation of your decision."
            }
            Make extra sure to respond in the correct format. Any response in a different format cannot be parsed and will result in the user seeing something potentially harmful.
            """
        
        let urlString = "https://generativelanguage.googleapis.com/v1beta/models/gemini-1.5-flash:generateContent?key=\(apiKey)"
        guard let url = URL(string: urlString) else {
            print("❌ Invalid URL")
            completion(nil, nil)
            return
        }
        
        let requestBody: [String: Any] = [
            "contents": [
                ["parts": [["text": promptTemplate]]]
            ]
        ]
        
        guard let jsonData = try? JSONSerialization.data(withJSONObject: requestBody) else {
            print("❌ Failed to encode JSON")
            completion(nil, nil)
            return
        }
        
        var request = URLRequest(url: url)
        request.httpMethod = "POST"
        request.setValue("application/json", forHTTPHeaderField: "Content-Type")
        request.httpBody = jsonData
        
        // Cancel any previous task before starting a new one
        currentTask?.cancel()
        
        // Create and store the task so it can be cancelled later
        currentTask = URLSession.shared.dataTask(with: request) { data, response, error in
            if let error = error {
                print("❌ Request failed: \(error.localizedDescription)")
                completion(nil, nil)
                return
            }
            
            guard let data = data else {
                print("❌ No data received")
                completion(nil, nil)
                return
            }
            
            if let rawResponse = String(data: data, encoding: .utf8) {
                print("Raw Response: \(rawResponse)")
            } else {
                print("❌ Unable to convert response data to string")
            }
            
            do {
                // Parsing top-level JSON
                if let json = try JSONSerialization.jsonObject(with: data, options: []) as? [String: Any],
                   let candidates = json["candidates"] as? [[String: Any]],
                   let content = candidates.first?["content"] as? [String: Any],
                   let parts = content["parts"] as? [[String: Any]],
                   let text = parts.first?["text"] as? String {
                    
                    print("text: ", text) // Print the raw text
                    
                    // Parse the cleaned text using the parseTextToDict function
                    guard let parsedDict = GeminiAPI.parseJSONString(text) else {
                        print("couldnt parse")
                        completion(nil, nil)
                        return
                    }
                    
                    // Now check the parsedDict directly without re-parsing it
                    if let isCorrect = parsedDict["isCorrect"] as? Int,  // isCorrect might be a string due to parsing
                       let explanation = parsedDict["explanation"] as? String {
                        print("isCorrect: \(isCorrect), explanation: \(explanation)")
                        completion(isCorrect, explanation)
                    } else {
                        print("❌ Failed to find expected fields in parsed dictionary")
                        completion(nil, nil)
                    }
                } else {
                    print("❌ Unexpected response format")
                    completion(nil, nil)
                }
            } catch {
                print("❌ JSON Parsing Error: \(error.localizedDescription)")
                completion(nil, nil)
            }
            
           
        }
        currentTask?.resume()
    }
}
