import spacy
import re
import webbrowser

nlp = spacy.load("en_core_web_sm")

responses = {
    "greet": {
        "response": "Hello! How can I help you today?",
        "doc_link": None
    },
    "hello": {
        "response": "Hello! How can I help you today?",
        "doc_link": None
    },
    "bye": {
        "response": "Goodbye! Have a great day!",
        "doc_link": None
    },
    "help": {
        "response": "I can answer your questions. Try asking about something more specific!",
        "doc_link": None
    },
    "default": {
        "response": "I'm sorry, I didn't understand that. Could you rephrase?",
        "doc_link": None
    },
    
    # Java-related responses
    "if statement": {
        "response": "An if statement in Java allows conditional execution of code blocks based on boolean expressions.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html"
    },
    "if else": {
        "response": "An if-else statement provides an alternative block of code to execute when the condition is false.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html"
    },
    "nested if": {
        "response": "A nested if statement is an if statement inside another if statement to check multiple conditions.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/if.html"
    },
    "for loop": {
        "response": "A for loop in Java is used to iterate over a range of values with a defined condition and increment.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/for.html"
    },
    "while loop": {
        "response": "A while loop executes a block of code as long as the condition remains true.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/while.html"
    },
    "do while loop": {
        "response": "A do-while loop executes at least once before checking the condition.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/while.html"
    },
    "switch": {
        "response": "A switch statement in Java allows multi-way branching based on variable values.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/switch.html"
    },
    "break": {
        "response": "The break statement terminates a loop or switch statement prematurely.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/branch.html"
    },
    "continue": {
        "response": "The continue statement skips the current iteration and moves to the next.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/branch.html"
    },
    "array": {
        "response": "An array in Java is a collection of elements of the same data type stored in contiguous memory locations.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/arrays.html"
    },
    "arraylist": {
        "response": "An ArrayList in Java is a resizable array implementation of the List interface.",
        "doc_link": "https://docs.oracle.com/javase/8/docs/api/java/util/ArrayList.html"
    },
    "string": {
        "response": "A String in Java is an object representing a sequence of characters.",
        "doc_link": "https://docs.oracle.com/javase/8/docs/api/java/lang/String.html"
    },
    "char": {
        "response": "The char data type in Java represents a single 16-bit Unicode character.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html"
    },
    "int": {
        "response": "The int data type in Java is a 32-bit signed integer.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html"
    },
    "double": {
        "response": "The double data type in Java represents floating-point numbers with double precision.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html"
    },
    "boolean": {
        "response": "A boolean in Java holds only two values: true or false.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/datatypes.html"
    },
    "class": {
        "response": "A class in Java is a blueprint for creating objects, defining properties, and behaviors.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/classes.html"
    },
    "object": {
        "response": "An object is an instance of a class that holds its own state and behaviors.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/objects.html"
    },
    "inheritance": {
        "response": "Inheritance in Java allows a class to acquire properties and methods from another class.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/IandI/subclasses.html"
    },
    "polymorphism": {
        "response": "Polymorphism in Java enables methods to have different implementations based on the object calling them.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/IandI/polymorphism.html"
    },
    "method overloading": {
        "response": "Method overloading allows multiple methods in the same class with the same name but different parameters.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/methods.html"
    },
    "method overriding": {
        "response": "Method overriding occurs when a subclass provides a specific implementation of a method already defined in its superclass.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/IandI/override.html"
    },
    "constructor": {
        "response": "A constructor in Java is a special method used to initialize objects.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/constructors.html"
    },
    "static method": {
        "response": "A static method in Java belongs to the class rather than any object instance.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/classvars.html"
    },
    "final keyword": {
        "response": "The final keyword in Java is used to declare constants and prevent method overriding.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/IandI/final.html"
    },
    "abstract class": {
        "response": "An abstract class in Java cannot be instantiated and may have abstract methods.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/IandI/abstract.html"
    },
    "interface": {
        "response": "An interface in Java defines a contract for classes to implement without providing concrete method definitions.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/IandI/createinterface.html"
    },
    "public keyword": {
        "response": "The public keyword in Java makes a class or method accessible from anywhere.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html"
    },
    "private keyword": {
        "response": "The private keyword restricts access to a class's members within the same class.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html"
    },
    "protected keyword": {
        "response": "The protected keyword allows access within the same package and subclasses.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html"
    },
    "this keyword": {
        "response": "The this keyword in Java refers to the current instance of a class.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/thiskey.html"
    },
    "super keyword": {
        "response": "The super keyword refers to the parent class of an object.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/IandI/super.html"
    },
    "encapsulation": {
        "response": "Encapsulation is the principle of wrapping data and methods into a single unit (class) in Java.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/concepts/object.html"
    },
    "getter and setter": {
        "response": "Getters and setters are methods used to access and modify private class fields in Java.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/accesscontrol.html"
    },
    "try catch": {
        "response": "A try-catch block in Java is used to handle exceptions and prevent program crashes.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/essential/exceptions/try.html"
    },
    "throws keyword": {
        "response": "The throws keyword in Java declares exceptions that a method might throw.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/essential/exceptions/declaring.html"
    },
    "scanner": {
        "response": "The Scanner class in Java is used to take user input from the console.",
        "doc_link": "https://docs.oracle.com/javase/8/docs/api/java/util/Scanner.html"
    },
    "random": {
        "response": "The Random class in Java is used to generate pseudo-random numbers.",
        "doc_link": "https://docs.oracle.com/javase/8/docs/api/java/util/Random.html"
    },
    "recursion": {
        "response": "Recursion is a technique where a function calls itself to solve a problem iteratively.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/javaOO/recursion.html"
    },
    "OOP": {
        "response": "Java is an object-oriented programming language that follows principles like encapsulation, inheritance, and polymorphism.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/concepts/"
    },
    "JVM": {
        "response": "The Java Virtual Machine (JVM) is responsible for running Java bytecode on any platform.",
        "doc_link": "https://docs.oracle.com/javase/specs/jvms/se8/html/"
    },
    "JDK": {
        "response": "The Java Development Kit (JDK) provides tools necessary for developing and running Java programs.",
        "doc_link": "https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html"
    },
    "JRE": {
        "response": "The Java Runtime Environment (JRE) is a set of libraries required to run Java applications.",
        "doc_link": "https://docs.oracle.com/javase/8/docs/technotes/guides/install/install_overview.html"
    },
    "main method": {
        "response": "The main method in Java serves as the entry point for a program's execution.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/getStarted/cupojava/win32.html"
    },
    "print statement": {
        "response": "System.out.println() is used in Java to print output to the console.",
        "doc_link": "https://docs.oracle.com/javase/8/docs/api/java/io/PrintStream.html#println--"
    },
    "modulus operator": {
        "response": "The modulus operator (%) in Java returns the remainder of a division operation.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html"
    },
    "bitwise operator": {
        "response": "Bitwise operators in Java perform operations on binary numbers.",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html"
    },
    "logical operators": {
        "response": "Logical operators in Java include && (AND), || (OR), and ! (NOT).",
        "doc_link": "https://docs.oracle.com/javase/tutorial/java/nutsandbolts/operators.html"
    }
}

def preprocess_input(user_input):
    doc = nlp(user_input.lower())
    tokens = [token.lemma_ for token in doc if not token.is_stop and not token.is_punct]
    processed_tokens = set()
    processed_tokens.add(user_input.lower())
    processed_tokens.add(" ".join(user_input.lower().split()))
    
    for token in doc:
        if not token.is_stop and not token.is_punct:
            processed_tokens.add(token.lemma_) 
            processed_tokens.add(token.text)    
            if token.pos_ == "NOUN":
                processed_tokens.add(token.lemma_ + "s")
                processed_tokens.add(token.lemma_ + "es")

    full_phrase = " ".join(tokens)
    processed_tokens.add(full_phrase)
    processed_tokens.update(tokens)
    
    words = user_input.lower().split()
    if len(words) > 1:
        processed_tokens.add(" ".join(reversed(words)))
        processed_tokens.add("-".join(words))
        processed_tokens.add("_".join(words))
    
    return processed_tokens

def get_response(user_input):
    processed_tokens = preprocess_input(user_input)
    user_input_lower = user_input.lower()
    
    for key in responses:
        key_lower = key.lower()
        if key_lower in processed_tokens or key_lower in user_input_lower:
            return responses[key]["response"], responses[key]["doc_link"]
    
    best_match = None
    best_match_score = 0
    input_words = set(user_input_lower.split())
    
    for key in responses:
        key_lower = key.lower()
        key_words = set(key_lower.split())
        match_score = len(key_words.intersection(input_words)) / len(key_words)
        
        if match_score > best_match_score and match_score > 0.5:
            best_match = key
            best_match_score = match_score
    
    if best_match:
        return responses[best_match]["response"], responses[best_match]["doc_link"]
    
    for key in responses:
        key_lower = key.lower()
        key_words = set(key_lower.split())
        if any(word in input_words for word in key_words):
            return responses[key]["response"], responses[key]["doc_link"]
    
    return responses["default"]["response"], responses["default"]["doc_link"]

def chat():
    print("Chatbot: Hello! I'm your Java programming assistant. How can I help you today?")
    last_doc_link = None
    
    while True:
        user_input = input("\nYou: ").strip()
        
        if user_input.lower() == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        
        if not user_input:
            print("Chatbot: I didn't receive any input. Please ask me a question about Java programming!")
            continue
        
        if user_input.lower() == "yes" and last_doc_link:
            print("Chatbot: Opening the documentation for you...")
            webbrowser.open(last_doc_link)
            last_doc_link = None
            print("Chatbot: What else would you like to know about Java?")
            continue
            
        if user_input.lower() == "no" and last_doc_link:
            print("Chatbot: Alright! What else would you like to know about Java?")
            last_doc_link = None
            continue
            
        response, doc_link = get_response(user_input)
        print("Chatbot:", response)
        
        if doc_link:
            last_doc_link = doc_link
            print("Chatbot: Would you like to know more about this topic? (Type 'yes' to view the documentation)")
        else:
            last_doc_link = None

if __name__ == "__main__":
    chat()
