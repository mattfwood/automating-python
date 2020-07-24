import requests
import urllib.parse
import webbrowser

import pprint

pp = pprint.PrettyPrinter(indent=2)

# @TODO: get this from user input
USER = 'mattfwood'
ENDPOINT = f"https://api.github.com/users/{USER}/repos?sort=pushed"

response = requests.get(ENDPOINT)
result = response.json()[0]

print(result['url'])
webbrowser.open(result['svn_url'])

# QUESTION_ENDPOINT = (
#     'https://api.stackexchange.com/2.2/search?order=desc&sort=votes&site=stackoverflow'
# )

# # @TODO: Get this from user
# query = 'python filter'


# def pretty_print(value):
#     return pp.pprint(value)


# def get_question(query):
#     question_response = requests.get(QUESTION_ENDPOINT, params={'intitle': query})
#     first_result = question_response.json()['items'][0]
#     return first_result


# def get_top_answer(question_id):
#     response = requests.get(
#         f"https://api.stackexchange.com/2.2/questions/{question_id}/answers?order=desc&sort=votes&site=stackoverflow&filter=!9_bDE(S6I"
#     )
#     result = response.json()['items'][0]['body_markdown']
#     return result


# result = get_question(query)
# top_answer = get_top_answer(result['question_id'])

# # pretty_print(result)
# pretty_print(top_answer)
# print(result)
