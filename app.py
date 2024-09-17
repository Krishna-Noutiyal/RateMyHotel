from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
from predict import predict_single_rating

app = Flask(__name__)
# Question list for feedback
questions_list = [
"Location and accessibility was as expected.",
"Quality of service was as expectation.",
"Room comfort and cleanliness was suitable.",
"Facilities and amenities was proper.",
"Food and beverage options was as expectation.",
"Staff Behavior and management was good.",
"Safety and security was as per norms of the hospitality.",
"Fitness center facility was as expected.",
"Foreign Language Knowledge Staff facility availability.",
"Transport facility was as expectation.",
"Internet and Wi-Fi facility was good.",
"All the entertainment facilities was good.",
"Value for money saved as compare to other.",
"You will recommend this hotel facility to your friends."
]


# Home route
@app.route("/", methods=["GET", "POST"])
def home():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        # Append user data to database.csv
        df = pd.DataFrame([[name, email]], columns=["Name", "Email"])
        df.to_csv("Data/database.csv", mode="a", header=False, index=False)
        return redirect(url_for("feedback"))
    return render_template("home.html")


# Feedback route
@app.route("/feedback", methods=["GET", "POST"])
def feedback():
    if request.method == "POST":
        hotel_name = request.form["hotel_name"]
        location = request.form["location"]
        country = request.form["country"]
        questions_answers = [request.form[f"q{i}"] for i in range(1, 15)]

        # Create temp.csv with user feedback
        feedback_data = [hotel_name, location, country] + questions_answers
        df = pd.DataFrame(
            [feedback_data],
            columns=[
                "Hotel Name",
                "Location",
                "Country",
                "Q1. " + questions_list[0],
                "Q2. " + questions_list[1],
                "Q3. " + questions_list[2],
                "Q4. " + questions_list[3],
                "Q5. " + questions_list[4],
                "Q6. " + questions_list[5],
                "Q7. " + questions_list[6],
                "Q8. " + questions_list[7],
                "Q9. " + questions_list[8],
                "Q10. " + questions_list[9],
                "Q11. " + questions_list[10],
                "Q12. " + questions_list[11],
                "Q13. " + questions_list[12],
                "Q14. " + questions_list[13],
            ],
        )
        df.to_csv("Data/temp.csv", index=False)
        return redirect(url_for("thankyou"))

    # Pass the question list to the template when rendering
    return render_template("feedback.html", question_list=questions_list)


# Thank You route
@app.route("/thankyou")
def thankyou():
    # Use predict_single_rating function to get the predicted rating
    rating = predict_single_rating("./Data/temp.csv")
    return render_template("thankyou.html", rating=rating)


if __name__ == "__main__":
    app.run(debug=True)
