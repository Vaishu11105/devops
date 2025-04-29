from tkinter import *
from tkinter import messagebox
import requests

class App:

    def __init__(self):
        self.root = Tk()
        self.root.title("NLP Application")
        self.root.geometry("600x600")
        self.root.configure(bg="#34495e")
        self.main_menu()
        self.root.mainloop()

    def main_menu(self):
        self.clear_gui()

        self.root.geometry("500x600")

        heading=Label(text="Select a model")
        heading.pack(pady=(10,40))

        heading.configure(pady=20,font=("timesnewroman",40,"bold"),bg='#34495e',fg='#aab7b8')


        sentiment_btn = Button(text="Sentiment Analysis",command=self.sentiment_analysis_gui)
        sentiment_btn.pack(pady=(10,10))
        sentiment_btn.configure(height=5,width=30,font=("timesnewroman",12,"bold"))

        named_entity_btn =  Button(text="Named Entitiy Recognisation",command=self.ner_gui)
        named_entity_btn.pack(pady=(10,10))
        named_entity_btn.configure(height=5,width=30,font=("timesnewroman",12,"bold"))


        emotion_btn = Button(text="Language Detection",command=self.language_gui)
        emotion_btn.pack(pady=(10,10))
        emotion_btn.configure(height=5,width=30,font=("timesnewroman",12,"bold"))

    def sentiment_analysis_gui(self):
        self.clear_gui()

        self.root.geometry("500x450")

       

        heading = Label(text="Sentiment Analysis",bg="#34495e",fg="#aab7b8")
        heading.pack(pady=(30,10))

        heading.configure(font=("timesnewroman",25,"bold"))


        title = Label(text="Enter a paragraph",bg="#34495e",fg="#aab7b8")
        title.pack(pady=10)

        title.configure(font=("timesnewroman",15,"bold"))

        self.input = Text(self.root, width=50, height=10)
        self.input.pack()

        
        sentiment_btn = Button(text="Analyse Sentiment",command=self.perform_sentiment_analysis)
        sentiment_btn.pack(pady=20)
        sentiment_btn.configure(font=("timesnewroman",12,"bold"))


        home_btn = Button(text="Home",command=self.main_menu)
        home_btn.pack(pady=10)
        home_btn.configure(font=("timesnewroman",12,"bold"))

    def ner_gui(self):
        self.clear_gui()

        self.root.geometry("500x450")

       

        heading = Label(text="Named Entity Recognisation",bg="#34495e",fg="#aab7b8")
        heading.pack(pady=(30,10))

        heading.configure(font=("timesnewroman",25,"bold"))


        title = Label(text="Enter a paragraph",bg="#34495e",fg="#aab7b8")
        title.pack(pady=10)

        title.configure(font=("timesnewroman",15,"bold"))

        self.input = Text(self.root, width=50, height=8)
        self.input.pack()

        entity_label = Label(self.root,text="Enter entity ",font=("timesnewroma",12,"bold"),bg="#34495e",fg="#aab7b8")
        entity_label.pack(pady=10)

        

        self.entity_label_input = Entry(self.root,width=50)
        self.entity_label_input.pack(ipady=10)
        
        language_btn = Button(text="Recognise Entities",command=self.perform_ner)
        language_btn.pack(pady=10)
        language_btn.configure(font=("timesnewroman",12,"bold"))


        home_btn = Button(text="Home",command=self.main_menu)
        home_btn.pack(pady=10)
        home_btn.configure(font=("timesnewroman",12,"bold"))

    def language_gui(self):

        self.clear_gui()

        self.root.geometry("500x450")

       

        heading = Label(text="Language Detection",bg="#34495e",fg="#aab7b8")
        heading.pack(pady=(30,10))

        heading.configure(font=("timesnewroman",25,"bold"))


        title = Label(text="Enter a paragraph",bg="#34495e",fg="#aab7b8")
        title.pack(pady=10)

        title.configure(font=("timesnewroman",15,"bold"))

        self.input = Text(self.root, width=50, height=10)
        self.input.pack()

        
        # sentiment_btn = Button(text="Detect Language",command=self.perform_language_detection)
        # sentiment_btn.pack(pady=20)
        # sentiment_btn.configure(font=("timesnewroman",12,"bold"))


        home_btn = Button(text="Home",command=self.home_gui)
        home_btn.pack(pady=10)
        home_btn.configure(font=("timesnewroman",12,"bold"))

    def clear_gui(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def perform_sentiment_analysis(self):
        text = self.input.get("1.0", "end-1c")  # Get the text input for sentiment analysis
        if not text.strip():
            messagebox.showinfo("Error", "Please enter some text.")
            return

        try:
            response = requests.post("http://container2_backend:5000/nlp/sentiment", json={"text": text})
            data = response.json()

            if "sentiment" in data:
                sentiment = data["sentiment"]
                messagebox.showinfo("Sentiment Result", f"Sentiment: {sentiment}")
            else:
                messagebox.showerror("Error", "Failed to analyze sentiment.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    def perform_ner(self):
        text = self.input.get("1.0", "end-1c")  # Get the text input for Named Entity Recognition
        entity = self.entity_label_input.get()

        if not text.strip():
            messagebox.showinfo("Error", "Please enter some text.")
            return
        if(entity==""):
            messagebox.showinfo("Error", "Please enter some entity.")
            return

        try:
            response = requests.post("http://container2_backend:5000/nlp/ner", json={"text": text,"entity":entity})
            data = response.json()

            if "entities" in data:
                entities = data["entities"]
                result = "\n".join([f"{entity['text']} ({entity['start']})" for entity in entities])
                messagebox.showinfo("Named Entities", f"Entities Found:\n{result}")
            else:
                messagebox.showerror("Error", "Failed to extract entities.")
        except Exception as e:
            messagebox.showerror("Error", str(e))

    # def perform_text_generation(self):
    #     prompt = self.prompt_input.get()  # Get the text input for text generation
    #     if not prompt.strip():
    #         messagebox.showinfo("Error", "Please enter a prompt.")
    #         return

    #     try:
    #         response = requests.post("http://localhost:5001/nlp/text_generation", json={"prompt": prompt})
    #         data = response.json()

    #         if "generated_text" in data:
    #             generated_text = data["generated_text"]
    #             messagebox.showinfo("Generated Text", f"Generated Text:\n{generated_text}")
    #         else:
    #             messagebox.showerror("Error", "Failed to generate text.")
    #     except Exception as e:
    #         messagebox.showerror("Error", str(e))

def launch_gui():
    App()

if __name__ == "__main__":
    launch_gui()