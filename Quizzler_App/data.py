import requests
import time

parameters = {
    "amount": "10",
    "type": "boolean",
}

question_data = []


def fetch_questions():
    global question_data
    try:
        # Make an API request
        response = requests.get("https://opentdb.com/api.php", params=parameters)

        # Check for rate limiting (HTTP 429)
        if response.status_code == 429:
            print("Rate limit reached. Retrying after 5 seconds...")
            time.sleep(5)  # Wait 5 seconds before retrying
            return fetch_questions()  # Retry fetching the questions

        response.raise_for_status()  # Raise an error for other HTTP errors
        data = response.json()

        # Parse the results
        for item in data["results"]:
            question_data.append({
                "question": item["question"],
                "correct_answer": item["correct_answer"]
            })
    except requests.exceptions.RequestException as e:
        print(f"An error occurred: {e}")


# Fetch questions
fetch_questions()