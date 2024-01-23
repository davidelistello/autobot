from urllib.request import urlopen, Request
import base64
import logging
import ssl
import json

GIT_API_URL='https://api.github.com'
ORG='tamedia-adtec'
USER='davidelistello'
API_TOKEN='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'

# based on https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-organization-repositories

def map_projects(data):
    """Extracts a dictionary using name as key node and clone_url as value key node, from a given data JSON dictionary"""
    pj_names = []
    pj_dict = {}
    for id in data:
        pj_names.append(id["name"])
        pj_dict[id["name"]] = id["clone_url"]
    return pj_names, pj_dict


def push_to_sonar(pj_tuples):
    """Create entry into SonarQube for each projects using Sonar APIs"""

def github_get_api(url):
    """List all projects accessible from the organization and create analysis records by calling sonarqube API"""
    try:
        context = ssl._create_unverified_context()
        request = Request(GIT_API_URL + url)
        base64string = base64.encodebytes(('%s' % (API_TOKEN)).encode('utf8')).decode('utf8').replace('\n', '')
        request.add_header("Accept", "application/vnd.github+json")
        request.add_header("X-GitHub-Api-Version","2022-11-28")
        request.add_header("Authorization", "Basic %s" % base64string)
        response = urlopen(request,context=context)
        payload = response.read().decode('utf-8')
        json_response = json.loads(payload)
        response.close()
        print(json_response)
        #push_to_sonar(map_projects(json_response))
        print(map_projects(json_response)[1])
    except BaseException as exception:
        logging.warning('Failed to get api request from %s' % url)
        logging.warning(f"Exception Name: {type(exception).__name__}")
        logging.warning(f"Exception Desc: {exception}")


def main():
    github_get_api("/orgs/"+ORG+"/repos")

if __name__ == "__main__":
    main()
