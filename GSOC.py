import requests
import os

Severities = ["MINOR", "MAJOR", "CRITICAL", "BLOCKER"]
Types = ["CODE_SMELL", "BUG", "VULNERABILITY"]
IssueStatus = ["OPEN", "CONFIRMED", "FALSE_POSITIVE", "ACCEPTED", "FIXED"]


def get_sonarqube_issues():
    sonarqubeIssues = []
    token = os.getenv("SONAR_TOKEN")
    url = os.getenv("SONAR_HOST_URL") + "/api/issues/search"
    params = {
        "components": "gsoc2025",
        "severities": ",".join(Severities),
        "types": ",".join(Types),
        "issueStatuses": ",".join(IssueStatus)
    }
    response = requests.get(url, params=params, auth=(token, ""))
    if response.status_code == 200:
        sonarqubeAnalysis = response.json()
        for i in sonarqubeAnalysis["issues"]:
            if i.get("severity") in Severities and i.get("type") in Types and i.get("status") in IssueStatus:
                filePath = i.get("component").split(":")[-1]
                severity = i.get("severity")
                issueType = i.get("type")
                message = i.get("message")
                startLine = i.get("startLine")
                endLine = i.get("endLine")
                issue = {
                    "title": f"{severity} Issue in {filePath}: {message}",
                    "body": "**Description**:\n"
                            f"**Severity:** {severity}\n"
                            f"**Type:** {issueType}\n"
                            f"**File:** {filePath}\n"
                            f"**Lines:** {startLine} - {endLine}\n"
                            f"**Message:** {message}\n\n"
                            "Generated by SonarQube.",
                    "labels": ["sonarqube-automated", issueType, severity]
                }
                sonarqubeIssues.append(issue)
        return sonarqubeIssues
    else:
        print(f"Error while running sonarqube analysis: {response.status_code}, {response.text}")

    
def get_github_exsitsingIssues():
    githubIssues = []
    url = "https://api.github.com/repos/ajeyprasand/gsoc2025/issues"
    token = os.getenv("AUTH_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    params = {
        "state": "open", 
        "labels": "sonarqube-automated"
    }
    response = requests.get(url, headers=headers, params=params)
    if response.status_code == 200:
        existingIssues = response.json()        
        for i in existingIssues:
            issue = {}
            issue["title"] = i["title"]
            issue["body"] = i["body"]
            githubIssues.append(issue)
        return existingIssues
    else:
        print(f"Error while running fetching issues from github: {response.status_code}, {response.text}")
        

def create_github_issues(issues):
    url = "https://api.github.com/repos/ajeyprasand/gsoc2025/issues"
    token = os.getenv("AUTH_TOKEN")
    headers = {
        "Accept": "application/vnd.github+json",
        "Authorization": f"Bearer {token}",
        "X-GitHub-Api-Version": "2022-11-28"
    }
    for issue in issues[:2]:
        response = requests.post(url, headers=headers, json=issue)
        if response.status_code == 201:
            print(f"Successfully created issue: {issue['title']}")
        else:
            print(f"Error while creating issues in github: {response.status_code}, {response.text}")


if __name__ == "__main__":
    sonarqubeIssues = get_sonarqube_issues()
    githubIssues = get_github_exsitsingIssues()
    githubIssueTitles = []
    issuesToBeCreated = []
    if(githubIssues!= None):
        githubIssueTitles = [issue["title"] for issue in githubIssues]
    for i in sonarqubeIssues:
        if i["title"] not in githubIssueTitles:
            issuesToBeCreated.append(i)
    create_github_issues(issuesToBeCreated)
