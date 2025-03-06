# Library Imports
import spacy
import re
import webbrowser
import streamlit as st

# Load English SpaCy
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
    processed_tokens = set() # remove tokens
    processed_tokens.add(user_input.lower()) # put use input in lower case
    processed_tokens.add(" ".join(user_input.lower().split()))

    for token in doc:
        if not token.is_stop and not token.is_punct:
            processed_tokens.add(token.lemma_) # lemmatized input
            processed_tokens.add(token.text)
            if token.pos_ == "NOUN":
                processed_tokens.add(token.lemma_ + "s")
                processed_tokens.add(token.lemma_ + "es")

    full_phrase = " ".join(tokens)
    processed_tokens.add(full_phrase)
    processed_tokens.update(tokens)

    words = user_input.lower().split()
    if len(words) > 1:
        # edge conditions
        # No (in chatbot response to say end loop)
        # what is if-else (doesnt work)
        # what's an if-else (doesnt work)
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
            return responses[key]["response"], responses[key]["doc_link"] # return key response, and response link

    best_match = None
    best_match_score = 0
    # input_words = set(user_input_lower.split())
    input_words = set(re.split("\n|\f|\t| |-|_", user_input_lower))

    for key in responses:
        key_lower = key.lower()
        key_words = set(key_lower.split())
        match_score = len(key_words.intersection(input_words)) / len(key_words)

        if match_score > best_match_score and match_score > 0.5: # matches user input to the key and yields a score for how much it matches. Returns the best possible response.
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
    # Description
    st.title("Java Programming Assistant 🤖")
    st.markdown("**Ask the Chatbot :rainbow[anything] about Java!**")

    # Add the Session State variables
    # ... removes the need for a while loop to wait for user input and manages state
    if 'conversation' not in st.session_state: # entire conversation history as list
        st.session_state.conversation = [":rainbow[Chatbot]: Hello! I'm your Java programming assistant. How can I help you today? 🙂"]
    if 'last_doc_link' not in st.session_state: # doc links for responses
        st.session_state.last_doc_link = None
    if 'user_input' not in st.session_state: # user input
        st.session_state.user_input = ""
    if 'remove_send_button' not in st.session_state: # control state of button upon exit of chat
        st.session_state.remove_send_button = False

    # Display Entire Conversation
    for res in st.session_state.conversation:
        st.write(res)

    # Text Field for User Input
    # ... sets value of state variable 'user_input'
    user_input = st.text_input("Enter your question", placeholder="Type 'bye' to exit chat", value=st.session_state.user_input, key="user_input")

    # Chat
    if not st.session_state.remove_send_button: # display 'send' button when remove_send_button = false
        if st.button("Send"):
            user_input = user_input.strip() # trim user input
            if user_input:
                st.session_state.conversation.append(f"**You**: {user_input}") # display user input

                # Exit
                if user_input.lower() in ["bye", "goodbye", "finish", "end", "see you", "clear", "close", "i'm done", "im done", "quit", "nothing", "exit"]:
                    st.session_state.conversation.append(":rainbow[**Chatbot**]: You can always come back to ask me questions if you need. ✅")
                    st.session_state.remove_send_button = True  # hide 'send' button to disallow further input
                    print("Chatbot: Goodbye! Have a great day!")

                # Open Doc Link
                if user_input.lower() == "yes" and st.session_state.last_doc_link:
                    st.session_state.conversation.append(":rainbow[**Chatbot**]: Opening the documentation for you...")
                    print("Chatbot: Opening the documentation for you...")
                    webbrowser.open(st.session_state.last_doc_link)  # takes you to that respective doc link (that matches the response)
                    st.session_state.last_doc_link = None
                    st.session_state.conversation.append(":rainbow[**Chatbot**]: What else would you like to know about Java?")
                    print("Chatbot: What else would you like to know about Java?")

                # Do Not Open Doc Link
                if user_input.lower() == "no" and st.session_state.last_doc_link:
                    st.session_state.conversation.append(":rainbow[**Chatbot**]: Alright! What else would you like to know about Java?")
                    print("Chatbot: Alright! What else would you like to know about Java?")
                    st.session_state.last_doc_link = None

                # Handle Proper Keyword Response
                response, doc_link = get_response(user_input)
                st.session_state.conversation.append(":rainbow[**Chatbot**]: " + response) # display appropriate response from chatbot
                if doc_link:
                    st.session_state.last_doc_link = doc_link
                    st.session_state.conversation.append(":rainbow[**Chatbot**]: Would you like to know more about this topic? (Type 'yes' to view the documentation)")
                    print("Chatbot: Would you like to know more about this topic? (Type 'yes' to view the documentation)")
                else:
                    st.session_state.last_doc_link = None

                # Update UI
                st.rerun()

    # Restart Chatbot
    if st.session_state.remove_send_button is True:
         if st.button("Restart Chatbot", type="primary"):
            st.session_state.clear() # clear conversation history
            st.session_state.remove_send_button = False # start the (chat) if not st.session_state.remove_send_button... again
            st.rerun() # UI update


# MAIN
# ... run chatbot
if __name__ == "__main__":
    chat()