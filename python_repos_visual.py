import requests
import plotly.express as px

# Make an API call and check the response
url = "https://api.github.com/search/repositories"
url +="?q=language:python+sort:stars+stars:>10000"

headers = {"Accept": "application/vnd.github.v3+json"}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

# Convert the response object to a dictionary
response_dict = r.json()

# Process over all results
print(f"Complete results: {not response_dict['incomplete_results']}")

# Explore information about the repositories
repo_dicts = response_dict['items']
#repo_names, stars, hover_texts  = [], [], []
repo_links, stars, hover_texts = [], [], [] # Changing names out for repository links
for repo_dict in repo_dicts:
    # Code to turn repo names into active links
    repo_name = repo_dict['name']
    repo_url = repo_dict['html_url']
    repo_link = f"<a href='{repo_url}'>{repo_name}</a>"
    repo_links.append(repo_link)
    #repo_names.append(repo_dict['name'])
    stars.append(repo_dict['stargazers_count'])

    # Build hover_text
    owner = repo_dict['owner']['login']
    description = repo_dict['description']
    hover_text = f"{owner}<br />{description}"
    hover_texts.append(hover_text)

# make a visualization
title = "Most-starred Python Projects on Github"
labels = {'x': 'Repository', 'y': 'Stars'}
fig = px.bar(x=repo_links, y=stars, title=title, labels=labels, hover_name=hover_texts)

fig.update_layout(title_font_size=28, xaxis_title_font_size=20, yaxis_title_font_size=20) # Updating the size elements on the graph
fig.update_traces(marker_color='SteelBlue', marker_opacity=0.6) # Style change to alter bar color/opacity
fig.show()