from jinja2 import Template, Environment, FileSystemLoader
import os


def save_or_print_results(results, to_html=False, html_filename="results.html"):
    """
    Saves the results to an HTML file or prints them to the console based on the given option.

    Args:
        results (list of dict): List of result dictionaries to be included.
        to_html (bool): If True, save the results to an HTML file. Otherwise, print to the console.
        html_filename (str): The name of the file to save the results.
    """

    if to_html:
        __output_html(results, filename=html_filename)
        print(f"Results saved to {html_filename}")
    else:
        __output_console(results)



def __output_rating():
    pass
def __output_html(results, filename="results.html"):
    """
    Saves the results to an HTML file with toggle folding and formatting.

    Args:
        results (list of dict): List of result dictionaries to be included in the HTML file.
        filename (str): The name of the file to save the results.
    """
    # Set up Jinja2 environment and load the template
    file_loader = FileSystemLoader("./Template")  # Template directory
    env = Environment(loader=file_loader)
    template = env.get_template("main.html")

    # Prepare results with row_id
    for idx, result in enumerate(results):
        # devides the index by 3 to get the row id for 3 rows
        result["row_id"] = idx // 3  # Assign row_id for grouping in 3 rows

    # Add overall accuracy
    overall_predicted_rating = round(sum(result['Predicted Rating'] for result in results) / len(results),2)
    overall_calculated_rating = round(sum(result['Original Rating'] for result in results) / len(results),2)
    overall_accuracy = round(sum(result["Accuracy"] for result in results) / len(results),2)

    # Render the HTML content
    html_content = template.render(
        total_reviews= len(results),
        results=results,
        overall_accuracy=overall_accuracy,
        overall_predicted_rating=overall_predicted_rating,
        overall_calculated_rating=overall_calculated_rating
    )

    # Save to HTML file
    with open("./Output/" + filename, "w", encoding="utf-8") as file:
        file.write(html_content)


def __output_console(results):
    """
    Prints the results to the console.

    Args:
        results (list of dict): List of result dictionaries to be printed.
    """
    # Add overall accuracy
    overall_predicted_rating = round(
        sum(result["Predicted Rating"] for result in results) / len(results), 2
    )
    overall_calculated_rating = round(
        sum(result["Original Rating"] for result in results) / len(results), 2
    )
    overall_accuracy = round(
        sum(result["Accuracy"] for result in results) / len(results), 2
    )

    for result in results:
        print(f"\033[1m{result['Index']}\033[0m")
        print(f"\n\033[31;1m{result['Hotel Name']}\033[0m : ")
        print(
            f"Predicted Overall Rating: \033[1m{result['Predicted Rating']} ⭐\033[0m")

        print(f"\033[1mActual Rating : {result['Original Rating']}\033[0m ⭐")

        print(f"\033[1;37mAccuracy:\033[0m \033[32m{result['Accuracy']:.2f}%\033[0m")

        print(f"{result['Review']}\n")

    print(f"\nPredicted Rating: \033[1m{overall_predicted_rating}%\033[0m\n")
    print(f"Calcualted Rating: \033[1m{overall_calculated_rating}%\033[0m\n")
    print(f"\nAccuracy: \033[1m{overall_accuracy}%\033[0m\n")
