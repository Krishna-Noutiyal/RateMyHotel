def accuracy(test_features, predicted_rating):
    """
    Calculate the accuracy of the model by comparing the predicted rating
    with the actual rating derived from the test data.

    Parameters
    ----------
    test_features : pandas.Series
        The test data to use for calculating the accuracy.
    predicted_rating : float
        The predicted rating of the model.

    Returns
    -------
    accuracy : float
        The accuracy of the model in percentage.
    rating : int
        The actual rating derived from the test data.
    """
    # Testing the model
    # numeric_columns = test_features.select_dtypes(include=[int]).columns
    # rating = test_features[numeric_columns].apply(
    #     lambda x: x.mean(skipna=True), axis=1
    # )[0]

    total=0
    for i in test_features:
        if not isinstance(i,str):
            total +=i

    rating = total/14



    rating : int = round(rating,2)
    accuracy : float = abs((abs(predicted_rating - rating) / rating * 100) - 100)

    # print(f"Rating: {rating}")
    # print(f"Predicted Rating: {predicted_rating}")

    # print(f"Accuracy: {round(accuracy,2)}%")

    return (accuracy, rating)
