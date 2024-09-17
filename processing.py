# Step 2: Preprocessing
# Mapping textual responses to numerical values for each question
rating_map = {
    "strongly agree": 5,
    "agree": 4,
    "neutral": 3,
    "disagree": 2,
    "strongly disagree": 1,
}


def map_rating(dataframe):
    """
    Maps the textual responses to numerical values for each question.
    
    "strongly agree": 5,\n
    "agree": 4,\n
    "neutral": 3,\n
    "disagree": 2,\n
    "strongly disagree": 1,\n

    Args:
        dataframe (pd.DataFrame): The input DataFrame to be mapped.

    Returns:
        pd.DataFrame: The Mapped DataFrame.
    """

    # Convert all responses to lowercase and apply mapping
    question_columns = [col for col in dataframe.columns if col.startswith("Q")]  # Detect question columns dynamically
    for col in question_columns:
        dataframe[col] = dataframe[col].map(rating_map)  # Apply the mapping

    return dataframe
