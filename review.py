from textblob import TextBlob


def long_review(hotel_data, to_html=False):
    """
    Generates a long review of the hotel based on hotel data.

    Args:
        hotel_data (dict): Dictionary containing hotel name, location and
            survey answers.

    Kwargs:
        to_html (bool): If True, the review will be returned to support html tags ( can also be used for saving to text file). If False,
            the review will be returned as plain text suitable for console printing.

    Returns:
        str: A long review of the hotel.
    """
    try:
        # Extract hotel details and survey answers
        hotel_name = hotel_data["Hotel Name"].title()
        location = hotel_data["Location"].title()
        friend_recommendation = hotel_data[
            "Q14. You will recommend this hotel facility to your friends."
        ]

        # Responses to specific questions (Q1 - Q13)
        location_rating = hotel_data["Q1. Location and accessibility was as expected."]
        service_rating = hotel_data["Q2. Quality of service was as expectation."]
        comfort_rating = hotel_data["Q3. Room comfort and cleanliness was suitable."]
        facilities_rating = hotel_data["Q4. Facilities and amenities was proper."]
        food_rating = hotel_data["Q5. Food and beverage options was as expectation."]
        staff_behavior_rating = hotel_data[
            "Q6. Staff Behavior and management was good."
        ]
        safety_rating = hotel_data[
            "Q7. Safety and security was as per norms of the hospitality."
        ]
        fitness_center_rating = hotel_data[
            "Q8. Fitness center facility was as expected."
        ]
        language_staff_rating = hotel_data[
            "Q9. Foreign Language Knowledge Staff facility availability."
        ]
        transport_rating = hotel_data["Q10. Transport facility was as expectation."]
        wifi_rating = hotel_data["Q11. Internet and Wi-Fi facility was good."]
        entertainment_rating = hotel_data[
            "Q12. All the entertainment facilities was good."
        ]
        value_for_money_rating = hotel_data[
            "Q13. Value for money saved as compare to other."
        ]

        # Generate a more verbose review based on ratings
        review = f"Hotel Review for {hotel_name} located in {location}:\n\n"

        review += "The hotel has "
        review += "excellent " if location_rating >= 4 else "subpar "
        review += "location and accessibility. "

        review += "Service quality was "
        review += "top-notch " if service_rating >= 4 else "lacking "
        review += "and met expectations. "

        review += "Rooms were "
        review += (
            "comfortable and clean " if comfort_rating >= 4 else "not up to standard "
        )
        review += "for a cozy stay. "

        review += "Facilities were "
        review += "excellent " if facilities_rating >= 4 else "below average "
        review += "and met expectations. "

        review += "Food and beverage options were "
        review += "great " if food_rating >= 4 else "inadequate "
        review += "with a variety of choices. "

        review += "Staff behavior was "
        review += (
            "friendly and professional "
            if staff_behavior_rating >= 4
            else "unremarkable "
        )
        review += "during the stay. "

        review += "Safety and security were "
        review += "well maintained " if safety_rating >= 4 else "a concern "
        review += "throughout the hotel. "

        review += "The fitness center was "
        review += "well-equipped " if fitness_center_rating >= 4 else "lacking "
        review += "and as expected. "

        review += "Staff's foreign language knowledge was "
        review += "sufficient " if language_staff_rating >= 4 else "insufficient "
        review += "for international guests. "

        review += "Transport facilities were "
        review += "excellent " if transport_rating >= 4 else "poor "
        review += "and easily accessible. "

        review += "Wi-Fi service was "
        review += "reliable " if wifi_rating >= 4 else "unreliable "
        review += "and met expectations. "

        review += "Entertainment facilities were "
        review += "enjoyable " if entertainment_rating >= 4 else "lacking "
        review += "and added value to the stay. "

        review += "Overall, the value for money was "
        review += "excellent " if value_for_money_rating >= 4 else "not satisfactory "
        review += "compared to other options in the area. "

        # Friend recommendation part
        review += "\n\n"
        review += "I would " if friend_recommendation >= 4 else "I might hesitate to "
        review += "recommend this hotel to friends and family for a pleasant stay."

    except KeyError as e:
        print(f"Missing key in hotel data: {e}")
        return "Error generating review due to missing data."

    # Perform sentiment analysis
    blob = TextBlob(review)
    sentiment = blob.sentiment.polarity

    if to_html:
        # Modify the review based on sentiment
        if sentiment > 0:
            review += "\n\n<p class='green' > <b> Overall, the sentiment is positive. </b> </p>"
        elif sentiment < 0:
            review += "\n\n<p class='red' > <b> Overall, the sentiment is negative. </b> </p>"
        else:
            review += "\n\n<p class='orange' > <b> Overall, the sentiment is neutral. </b> </p>"

    else:
        # Modify the review based on sentiment
        if sentiment > 0:
            review += "\n\n\033[1;32mOverall, the sentiment is positive.\033[0m"
        elif sentiment < 0:
            review += "\n\n\033[1;31mOverall, the sentiment is negative.\033[0m"
        else:
            review += "\n\n\033[1mOverall, the sentiment is neutral.\033[0m"

    return review


def short_review(hotel_data):
    """
    Generates a short review of the hotel based on hotel data.

    Args:
        hotel_data (dict): Dictionary containing hotel name and location.

    Returns:
        str: A short review of the hotel.
    """
    
    # Extract hotel details and survey answers
    hotel_name = hotel_data["Hotel Name"].title()
    location = hotel_data["Location"].title()

    return "\n\t The hotel" + "\033[31;1m " + hotel_name + "\033[0m" + " is located in " + "\033[33;1m" + location + " \033[0m \n"
