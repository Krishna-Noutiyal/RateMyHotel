import pandas as pd
import joblib
import processing, filtering

def predict_single_rating(
    csv_path,
    modal_name="linear_regressor_v01",
):
    """

    Tests the trained model using the specified number of samples from the test set.

    Args :
        csv_path (str): The path to the CSV file containing the test data.

        modal_name (str): The name of the trained model stored in the Models folder. (default: 'linear_regressor_v01').

    Returns :
        rating (float): Returns the predicted rating of the review.

    """

    # Load the testing data
    data = pd.read_csv(csv_path, encoding="ISO-8859-1")

    # Step 1: Filter the data
    data = filtering.filter_data(data)

    # Step 2: Map text ratings to numerical values
    data = processing.map_rating(data)

    # Load the model and feature columns from file
    model, feature_columns = load_model("./Models/" + modal_name)

    # Extract features from the data DataFrame
    sample_features = data.iloc[0]
    # Predict the overall rating using the stored feature columns
    predicted_rating = predict_overall_rating(
        model, sample_features, feature_columns
    )

    return float((predicted_rating))


def predict_overall_rating(model, input_data, feature_columns=None):
    """
    Predicts the overall rating using the trained model.

    Args:
        model (sklearn model): The trained model.
        input_data (pd.DataFrame or dict): A row of input data (can be a dictionary or DataFrame).
        feature_columns (list): The columns that were used for training the model.
                                This ensures the new data matches the original training data.

    Returns:
        float: The predicted overall rating.
    """
    # If input_data is a dictionary, convert it to a DataFrame
    if isinstance(input_data, dict):
        input_data = pd.DataFrame([input_data])
    elif isinstance(input_data, pd.Series):
        input_data = pd.DataFrame([input_data])

    # Align the new data's columns with the trained model's features
    if feature_columns is not None:
        input_data = input_data[
            feature_columns
        ]  # Select only the features used for training

    # Predict the rating
    prediction = model.predict(input_data)
    return round(prediction[0], 2)


def load_model(model_file):
    """
    Loads a stored model using joblib.

    Args:
        model_file (str): The path to the stored model.

    Returns:
        model: The loaded machine learning model.
        list: The feature columns used for training the model.
    """
    model = joblib.load(model_file)

    # Assuming that the model was trained using specific features,
    # load these features from the model object (or store them separately during training)
    try:
        feature_columns = (model.feature_names_in_)  # Some sklearn models store feature names
    except AttributeError:
        feature_columns = None  # In case feature names aren't available in the model

    return model, feature_columns
