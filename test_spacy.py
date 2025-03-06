import spacy

# Load the English language model
nlp = spacy.load("en_core_web_sm")

def process_text(text):
    # Process the input text
    doc = nlp(text)
    
    # Print the tokens and their parts of speech
    print("\nAnalysis Results:")
    print("-" * 30)
    for token in doc:
        print(f"{token.text}: {token.pos_}")
    
    # Print additional linguistic features
    print("\nNamed Entities:")
    print("-" * 30)
    for ent in doc.ents:
        print(f"{ent.text}: {ent.label_}")
    
    print("\nDependencies:")
    print("-" * 30)
    for token in doc:
        print(f"{token.text} -> {token.dep_} -> {token.head.text}")

def main():
    print("Welcome to the Text Analysis Tool!")
    print("Enter 'quit' to exit")
    
    while True:
        # Get user input
        user_input = input("\nEnter your text: ").strip()
        
        # Check if user wants to quit
        if user_input.lower() == 'quit':
            print("Goodbye!")
            break
        
        # Process the input if it's not empty
        if user_input:
            process_text(user_input)
        else:
            print("Please enter some text!")

if __name__ == "__main__":
    main() 