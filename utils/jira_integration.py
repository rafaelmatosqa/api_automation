import requests
import json
import os

class JiraIntegration:
    def __init__(self, jira_config):
        self.project_key = jira_config['projectKey']
        self.jira_url = jira_config['jiraUrl']
        self.username = jira_config['username']
        self.password = jira_config['password']
        self.jira_send = jira_config['jirasend']

    def send_results_to_jira(self, filename="tm4j_result.json"):
        if self.jira_send == "CI":
            # Fetch credentials from environment variables or a vault
            self.jira_url = os.getenv('JIRA_URL')
            self.username = os.getenv('JIRA_USERNAME')
            self.password = os.getenv('JIRA_API_TOKEN')

        with open(filename, 'r') as file:
            results = json.load(file)
        
        payload = {
            "projectKey": self.project_key,
            "name": "Automated Test Run",
            "items": results
        }

        url = f"{self.jira_url}/rest/atm/1.0/testrun"
        headers = {
            'Content-Type': 'application/json',
            'Accept': 'application/json'
        }

        response = requests.post(url, auth=(self.username, self.password), headers=headers, data=json.dumps(payload))
        if response.status_code not in [200, 201]:
            print(f"Failed to log test result to JIRA: {response.status_code}, {response.text}")
