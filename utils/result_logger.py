import json

class ResultLogger:
    def __init__(self):
        self.results = []

    def log_result(self, name, status, environment):
        self.results.append({
            "scenario": name,
            "status": status,
            "environment": environment
        })

    def save_results(self, filename="tm4j_result.json"):
        with open(filename, 'w') as file:
            json.dump(self.results, file, indent=4)
