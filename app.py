from flask import Flask, render_template, request
from pipeline.prediction_pipeline import hybrid_recommendation

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    recommendations = None
    message = None

    if request.method == 'POST':
        try:
            # Get user ID from the form
            user_id = int(request.form.get("userID", 0))

            if user_id <= 0:
                message = "Please enter a valid user ID."
            else:
                recommendations = hybrid_recommendation(user_id)
                if not recommendations:
                    message = f"No recommendations found for user ID {user_id}."
        except ValueError:
            message = "User ID must be an integer."
        except Exception as e:
            print("Error occurred:", e)
            message = "An unexpected error occurred. Check the console for details."

    return render_template('index.html', recommendations=recommendations, message=message)


if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=5000)
