import streamlit as st
from pymongo import MongoClient

# Connect to MongoDB (use your MongoDB Atlas URI if you're using cloud)
from config import MONGO_URI
client = pymongo.MongoClient(MONGO_URI)
db = client['quizdb']
quiz_collection = db['quiz']

# Add Sidebar navigation
menu = ["Take The Quiz", "Add Quiz"]
choice = st.sidebar.selectbox("Menu", menu)

# Quiz taking functionality
if choice == "Take Quiz":
    st.title("MongoDB-Based Quiz App")

    # Fetch the quiz data from MongoDB
    quiz_data = list(quiz_collection.find({}))

    # Initialize a variable to count correct answers
    correct_answers = 0

    # Create a form for the quiz
    with st.form("quiz_form"):
        st.write("Answer the following questions:")

        # Dictionary to store user answers
        user_answers = {}

        # Loop through the quiz data fetched from MongoDB
        for i, q in enumerate(quiz_data):
            # Show the question and options (using radio buttons for multiple choice)
            user_answers[q['question']] = st.radio(q['question'], q['options'], key=i)

        # Submit button
        submit_button = st.form_submit_button("Submit Quiz")

    # If the form is submitted, calculate the result
    if submit_button:
        st.write("### Quiz Results")
        for q in quiz_data:
            if user_answers[q['question']] == q['answer']:
                correct_answers += 1
                st.success(f"Correct! {q['question']}")
            else:
                st.error(f"Wrong! {q['question']}. The correct answer is {q['answer']}.")

        # Display the total score
        st.write(f"Your score: {correct_answers}/{len(quiz_data)}")

    # Optional: Add a reset button to allow users to retake the quiz (refresh page)
    if st.button("Retake Quiz"):
        st.experimental_rerun()

# Add Quiz Functionality
elif choice == "Add Quiz":
    st.title("Add a New Quiz Question")

    # Input fields for adding a new quiz question
    question = st.text_input("Enter the quiz question")
    option1 = st.text_input("Option 1")
    option2 = st.text_input("Option 2")
    option3 = st.text_input("Option 3")
    option4 = st.text_input("Option 4")
    correct_answer = st.selectbox("Select the correct answer", [option1, option2, option3, option4])

    # Store the options in a list
    options = [option1, option2, option3, option4]

    if st.button("Add Question"):
        if question and all(options) and correct_answer:
            # Prepare the document to insert into MongoDB
            new_quiz_data = {
                "question": question,
                "options": options,
                "answer": correct_answer
            }
            # Insert the new question into the 'quiz' collection
            quiz_collection.insert_one(new_quiz_data)
            st.success("Quiz question added successfully!")
        else:
            st.error("Please fill in all fields before submitting.")
