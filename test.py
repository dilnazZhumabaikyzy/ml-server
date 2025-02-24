import requests 

data = {"input": "Given an array `nums` of n integers and an integer `target`, find three integers in `nums` such that the sum is closest to `target`. Return the sum of the three integers. You may assume that each input would have exactly one solution."}
headers = {"Content-Type": "application/json"}


res = requests.get("http://127.0.0.1:3000/", json=data, headers=headers)

print("Welcome get request", res.json())

res = requests.post("http://127.0.0.1:3000/classify", json=data, headers=headers)

print("Classification results:", res.json())

res_input = requests.post("http://127.0.0.1:3000/classify/input", json=data, headers=headers)
print("Input classification:", res_input.json())

res_output = requests.post("http://127.0.0.1:3000/classify/output", json=data, headers=headers)
print("Output classification:", res_output.json())


res_topic = requests.post("http://127.0.0.1:3000/classify/topic", json=data, headers=headers)
print("Topic classification:", res_topic.json())

res_difficulty = requests.post("http://127.0.0.1:3000/classify/difficulty", json=data, headers=headers)
print("Difficulty classification:", res_difficulty.json())

res_keywords = requests.post("http://127.0.0.1:3000/classify/keywords", json=data, headers=headers)
print("Keywords extraction:", res_keywords.json())

res_mapreduce = requests.post("http://127.0.0.1:3000/classify/mapreduce", json=data, headers=headers)

print("Mapreduce 5 classifications:")
print(res_mapreduce.json()) 


user_input = {
    "Topic": "dynamic programming",
    "Keywords": "array, search",
    "Input": "array of integers and target",
    "Output": "index of the integer number",
    "Difficulty": "Easy",
    "DataNotInteract": "1",
    "CountingRelated": "0",
    "FewKManyV": "1",
    "JoinData": "0",
    "ConditionProblem": "1"
}

res = requests.post("http://127.0.0.1:3000/find_similar_problems", json={"input": user_input})

response_data = res.json()
for problem_key, problem_data in response_data.items():
    print(f"Problem {problem_key}:")
    print(f"ID: {problem_data['id']}")
    print(f"Similarity Score: {problem_data['similarity_score']}")
    print()