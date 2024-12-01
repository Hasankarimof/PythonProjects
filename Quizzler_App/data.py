import requests

parameters = {
    "amount":"10",
    "type":"boolean",
}



response = requests.get("https://opentdb.com/api.php",params=parameters)
response.raise_for_status()
data = response.json()
question_data = []
for item in data["results"]:
    question_data.append({
        "question": item["question"],
        "correct_answer": item["correct_answer"]
})
