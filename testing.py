import pandas as pd
import processing, filtering, predict, review, output, analytics



if __name__ == "__main__":
    print("\n\033[1mTesting the model\033[0m\n")

    # Call the testing function with appropriate parameters
    t = predict.predict_single_rating("./Data/temp.csv", modal_name="linear_regressor_v01")

    # t = predict.predict_single_rating(model_file="./Models/linear_regressor_v01", csv_file ="./Data/temp.csv")
    print(t)
