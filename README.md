# Project Overview
This project is a simple Quiz App built using Streamlit for the frontend and MongoDB for backend data storage. 
The app allows users to take a quiz and displays their score after submission. The quiz questions and answers are stored in MongoDB.

# Features
Users can take a quiz and receive their score immediately.
Admin can add new quiz questions dynamically.
Questions and answers are stored in MongoDB.
Real-time result calculation.

Frontend: Streamlit
Backend: MongoDB
Language: Python 3.8+


# Taking the Quiz:
When you open the app, you’ll see a list of quiz questions.
Select your answers and click the Submit button.

Your score will be displayed based on the number of correct answers.


# Admin Section:
To add a new quiz, go to the Admin Section from the sidebar.
Input the quiz question, answer choices, and correct answer, then click Add Question.
The new question will be added to the quiz database and can be seen by users.
![Uploading image.png…]()

# Database Configuration
The quiz data (questions and answers) is stored in MongoDB. You can either use a local MongoDB instance or connect to a cloud-based MongoDB Atlas database.

Configuring MongoDB:
If using a local MongoDB:
By default, the app connects to a MongoDB instance running on localhost:27017.
You can change the connection string in the app.py file to match your MongoDB configuration.
