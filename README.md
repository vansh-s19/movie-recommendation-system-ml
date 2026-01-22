🎬 Movie Recommendation System (Machine Learning)

📌 Project Overview

This project is a Content-Based Movie Recommendation System built using Machine Learning techniques.
It recommends movies similar to a user’s favorite movie by analyzing movie metadata such as genres, cast, director, keywords, and tagline.

The system uses TF-IDF Vectorization and Cosine Similarity to measure similarity between movies and suggest the most relevant ones.

⸻

🚀 How It Works
	1.	Movie data is loaded from a CSV file.
	2.	Important textual features are selected:
	•	Genres
	•	Keywords
	•	Tagline
	•	Director
	•	Cast	
    3.	Missing values are replaced with empty strings.
	4.	All selected features are combined into a single text column.
	5.	Text data is converted into numerical vectors using TF-IDF.
	6.	Cosine Similarity is applied to find similar movies.
	7.	The user enters a movie name.
	8.	The system finds the closest match and recommends top 20 similar movies.

⸻

🧠 Machine Learning Concepts Used
	•	Content-Based Filtering
	•	TF-IDF Vectorization
	•	Cosine Similarity
	•	Natural Language Processing (NLP)

⸻

🛠️ Technologies & Libraries
	•	Python
	•	Pandas
    •	NumPy
	•	Scikit-learn
	•	Difflib

⸻

📂 Project Structure
Movie Recommendation System/
│
├── data/
│   └── movies.csv
│
├── model/
│   └── movie_recommendation_system.py
│
└── README.md


⸻

🧪 How to Run the Project
	1.	Clone the repository:\git clone 
    https://github.com/vansh-s19/movie-recommendation-system.git
    	
    2.	Navigate to the project directory:
    cd movie-recommendation-system

    3.	Install required libraries:
    pip install pandas numpy scikit-learn

    4.	Run the program:
    python movie_recommendation_system.py

    5.	Enter your favorite movie name when prompted.


⸻

💡 Sample Input
Enter your favourite movie name : Avatar

📤 Sample Output
Movies Suggested for you :

1. Guardians of the Galaxy
2. Star Wars
3. Avengers: Infinity War
...


⸻

✅ Features
	•	Accurate similarity-based recommendations
	•	Handles spelling mistakes using close match detection
	•	Simple command-line interface
	•	Beginner-friendly ML project

⸻

📈 Future Improvements
	•	Add a web interface (Flask / Streamlit)
	•	Improve recommendations using user ratings
	•	Optimize performance for large datasets
	•	Add poster and trailer support using APIs

⸻

👨‍🎓 Author

Vansh Saxena
Student | Machine Learning Enthusiast

⸻

📄 License

This project is for educational purposes and open for learning and improvement.
