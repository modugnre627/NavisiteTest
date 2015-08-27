#! python

import sys
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError
import urllib.parse
import urllib.request

# name: Robert Modugno
# description:  Basic python script to query against
#               GitHub repository.  Accept number of
#               repositories to display and a search
#               string and store results in a json
#               dictionary and write to terminal
#
# Once the module has been run at the command line
# simply type in repository_search(n, 's') where
# n is the maximum number of repositories to display
# and 's' is the search string to evaluate.  As this is
# quick and dirty and my first attempt at Python there
# is very little error checking other then evaluating
# the HTTP GET request

def repository_search(num_of_repos, search_string):

    # args: num_of_repos = number of repositories to display
    #       search_string = string to use for search
    
    url = 'https://api.github.com/search/repositories'
    values = {'q' : search_string ,
              'sort' : 'forks',
              'order' : 'desc' }
    
    url_values = urllib.parse.urlencode(values)
    full_url = url + '?' + url_values
    req = urllib.request.Request(full_url)
    
    

    try:
        response = urlopen(req)    
    except HTTPError as e:
        print('The server couldn\'t fulfill the request.')
        print('Error code: ', e.code)
        print(e)
    except URLError as e:
        print('We failed to reach a server.')
        print('Reason: ', e.reason)
    else:
        repo_data = json.loads(response.readall().decode('utf-8'))

    print(type(repo_data['items']))

    my_list = repo_data['items']

      
    d = {}
    d2 = {}
    
    my_new_list = []
    owner_list = []

    d['keyword'] = search_string
    d['desired_num_of_repositories'] = num_of_repos
    d['number_repositories_returned'] = repo_data['total_count']

    if d['number_repositories_returned'] < num_of_repos : num_of_repos = d['number_repositories_returned']

    for i in range(num_of_repos):
        d2.clear()
        d_owner = my_list[i]['owner'].copy()
        d2['id'] = my_list[i]['id']
        d2['name'] = my_list[i]['name']
        d2['description'] = my_list[i]['description']
        d2['language'] = my_list[i]['language']
        d2['created_at'] = my_list[i]['created_at']
        d2['html_url'] = my_list[i]['html_url']
        d2['watchers_count'] = my_list[i]['watchers_count']
        d2['forks_count'] = my_list[i]['forks_count']
        d2['owner_login'] = d_owner['login']
        d2['owner_id'] = d_owner['id']
        d2['owner_url'] = d_owner['url']
        my_new_list.append(d2.copy())
        


    d['items'] = my_new_list


    my_json_list = json.dumps(d,sort_keys=True,indent=4, separators=(',', ': '))
    
    print('My List Is',my_json_list)
    
    


