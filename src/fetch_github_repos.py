from urllib.request import urlopen, Request
import base64
import logging
import ssl
import json

GIT_API_URL='https://api.github.com'
ORG='tamedia-adtec'
USER='davidelistello'
API_TOKEN='#please_provide_your_token#'

# based on https://docs.github.com/en/rest/repos/repos?apiVersion=2022-11-28#list-organization-repositories

def map_projects(data):
    """Extracts a dictionary using name as key node and clone_url as value key node, from a given data JSON dictionary"""
    result = []
    dict = {}
    for id in data:
        result.append(id["name"])
        dict[id["name"]] = id["clone_url"]
    return dict



def github_get_api(url):
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
        print(map_projects(json_response))
    except BaseException as exception:
        logging.warning('Failed to get api request from %s' % url)
        logging.warning(f"Exception Name: {type(exception).__name__}")
        logging.warning(f"Exception Desc: {exception}")


def main():
    github_get_api("/orgs/"+ORG+"/repos")

if __name__ == "__main__":
    main()
