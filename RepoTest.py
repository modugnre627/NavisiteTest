#! python
import sys
import json
from urllib.request import Request, urlopen
from urllib.error import URLError, HTTPError

import urllib.parse
import urllib.request

def depo_list(num_of_repos, search_string):

    print('The number of repositories to find is', num_of_repos, 'and the search string is:', search_string)

    url = 'https://api.github.com/search/repositories'
    values = {'q' : search_string ,
              'sort' : 'forks',
              'order' : 'desc' }


    url_values = urllib.parse.urlencode(values)

    full_url = url + '?' + url_values
    #data = data.encode('utf-8') # data should be bytes
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
        the_page = response.read()
        print(the_page)
    
    


    
    # r = requests.get('https://api.github.com/search/repositories?&sort=fork&order=desc')

    # response = urllib.request.urlopen('http://python.org/')
    # html = response.read()
    # sys.stdout.write("html= %s\n" % (html,))


