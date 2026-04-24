 Task Management App (ML-Based)
 # Overview
This is a simple **Task Management System** built using **Python and Machine Learning**.
The application automatically assigns a **priority level (High, Medium, Low)** to tasks based on their description.
# Features
* Add tasks with automatic priority detection
* Remove tasks
* View all tasks
* Machine Learning-based classification
* Stores data in a CSV file
# Technologies Used
* Python
* Pandas
* Scikit-learn
* TF-IDF Vectorizer
* Naive Bayes Algorithm
# Installation
1. Install Required Packages
pip install pandas scikit-learn
# ▶️ How to Run
python main.py
# Usage

1. Select an option from the menu:
   * 1 → Add Task
   * 2 → Remove Task
   * 3 → List Tasks
   * 4 → Exit
2. When adding a task:
   * Enter task description
   * App will automatically assign priority
# How It Works
1. Task text is converted into numbers using **TF-IDF**
2. A **Naive Bayes model** calculates probabilities
3. The highest probability determines the priority:
   * High
   * Medium
   * Low
## 📁 File Structure
project-folder/
│
├── main.py
├── tasks.csv
└── README.md

## 📊 Example

Input:
submit assignment today
Output:
Priority: High


## 👩‍💻 Author

Your Name

---
