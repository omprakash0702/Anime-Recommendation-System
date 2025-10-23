🧠 Anime Recommendation System using Flask + ML  
A Flask-based web application that recommends anime titles based on user input using machine learning. It leverages content-based filtering with cosine similarity on anime metadata to provide personalized suggestions. The project follows MLOps principles and integrates Comet ML for experiment tracking.

🎭 Features  
- Real-time anime recommendations — enter an anime user Id  and get  suggestions instantly  
- Flask web interface — lightweight and interactive  
- ML-powered — uses preprocessed data and cosine similarity to generate recommendations  
- Comet ML integration — track experiments, model versions, and metrics  
- Modular MLOps structure — organized folders for artifacts, config, logs, pipelines, source code, templates, and static assets  
- Easy to expand — add hybrid models, poster images, or user feedback integration  

🛠 Project Structure  
Anime-Recommendation-System/ contains app.py (Flask entry point), artifacts/ (saved models and similarity matrices), config/ (constants and paths), logs/ (log files), pipeline/ (recommendation scripts), src/ (preprocessing and utility code), static/ (CSS, JS, images), templates/ (HTML templates home.html and recommend.html), tester.py (local testing), requirements.txt (dependencies), and README.md (project documentation)  

🚀 How to Run  
Clone the repository, navigate into the folder, create and activate a virtual environment, install dependencies, and run the Flask app: `git clone https://github.com/omprakash0702/Anime-Recommendation-System.git`, `cd Anime-Recommendation-System`, `python -m venv venv`, `venv\Scripts\activate` (Windows) or `source venv/bin/activate` (Linux/Mac), `pip install -r requirements.txt`, `python app.py`. Open your browser at http://127.0.0.1:5000/ and enter an anime title to get recommendations instantly.  

🚀 Requirements  
Python 3.10+, Flask, pandas, numpy, scikit-learn, pickle, comet_ml, Windows 10/11, Linux, or macOS  

👤 Author  
Omprakash — GitHub: [https://github.com/omprakash0702](https://github.com/omprakash0702)  

⭐ If you like this project, give it a star on GitHub!
