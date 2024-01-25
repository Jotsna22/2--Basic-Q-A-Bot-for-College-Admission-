import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

class AdmissionChatbot:
    def __init__(self):
        self.context = {}
        nltk.download('punkt')
        nltk.download('stopwords')
        nltk.download('wordnet')
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def start_conversation(self):
        print("Welcome to College Admission Chatbot! How can I assist you today?")
        while True:
            user_input = input("You: ").lower()
            response = self.generate_response(user_input)
            print("Chatbot:", response)

    def preprocess_text(self, text):
        tokens = word_tokenize(text)
        tokens = [self.lemmatizer.lemmatize(token) for token in tokens if token.isalnum()]
        tokens = [token for token in tokens if token not in self.stop_words]
        return tokens

    def generate_response(self, user_input):
        user_tokens = self.preprocess_text(user_input)
        if "admission" in user_tokens:
            return "Our college offers admission in various programs. What specific information do you need?"
        elif "requirements" in user_tokens:
            return "Admission requirements typically include academic transcripts, standardized test scores, letters of recommendation, and a personal statement. Do you need more details?"
        elif "procedures" in user_tokens:
            return "The admission process involves submitting an application, paying the application fee, and providing necessary documents. Deadlines vary for different programs. Would you like to know the deadline for a particular program?"
        elif "deadline" in user_tokens:
            return "The deadlines vary depending on the program. Please provide the name of the program you're interested in."
        elif "engineering" in user_tokens and "program" in user_tokens:
            self.context['program'] = 'Engineering'
            return "The deadline for the Engineering program is March 15th. Do you have any other questions?"
        elif "business" in user_tokens and "program" in user_tokens:
            self.context['program'] = 'Business'
            return "The deadline for the Business program is February 28th. Do you have any other questions?"
        elif "thank" in user_tokens or "bye" in user_tokens:
            return "You're welcome! If you have any more questions, feel free to ask. Goodbye!"
        else:
            return "I'm sorry, I couldn't understand that. Can you please rephrase your question?"

if __name__ == "__main__":
    chatbot = AdmissionChatbot()
    chatbot.start_conversation()
