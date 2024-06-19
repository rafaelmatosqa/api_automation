import json
from utils.jira_integration import JiraIntegration

class ResultLogger:
    def __init__(self, jira_config):
        self.results = []
        self.jira_integration = JiraIntegration(jira_config)

    def log_result(self, name, status, environment, test_case_key=None):
        if test_case_key:
            self.results.append({
                "testCaseKey": test_case_key,
                "status": status,
                "environment": environment
            })

    def save_results(self, filename="tm4j_result.json"):
        with open(filename, 'w') as file:
            json.dump(self.results, file, indent=4)
        self.jira_integration.send_results_to_jira(filename)
