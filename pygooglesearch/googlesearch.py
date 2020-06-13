import pandas as pd
import requests
from pathlib import Path
import os
import uuid
from itertools import chain
import warnings

class GoogleSearch:
    '''
    Creates wrapper class around Google Custom API
    that returns JSON response of search result items
    
    Params:
    api_key - String of API key acquired from Google API 
    search_engine - String of custom engine (cx) identifier from console
    '''
    def __init__(self, api_key, search_engine):
        self.api_key = api_key
        self.engine = search_engine
        self.api_url = 'https://www.googleapis.com/customsearch/v1?'
        self.has_next = True
        self.search_stats = None
        self.search_terms = None
        self.proxies = None
        self.results = []
    
    def _create_session(self):
        '''
        Creates a session object to API
        via requests pooling
        '''
        s = requests.Session()
        if self.proxies:
            s.proxies = self.proxies
        s.verify = False
        return s
    
    def get_results(self, **kwargs):
        '''
        Gets the JSON search results meeting
        search criteria
        
        Params:
        kwargs - Any valid key/vlaue combination from Google API
                 https://developers.google.com/custom-search/v1/reference/rest/v1/cse/list
        
        Returns:
        res - JSON response of Google Search Items if any along with additional metadata keys
        
        '''
        
        params = {'key': self.api_key,
                  'cx': self.engine,
                  'start': 1}
        
        for key, value in kwargs.items():
            params[key] = value
        
        session = self._create_session()
        
        while self.has_next == True:
            res = session.get(self.api_url, params=params)
        
            res = res.json()
            
            # Get results from search
            try:
                search_results = res['items']
                self.results.append(search_results)
            except:
                pass
            
            if params['start'] == 1:
                self.search_stats = res['searchInformation']
                self.search_terms = res['queries']['request'][0]
            try:
                params['start'] = res['queries']['nextPage'][0]['startIndex']
            except:
                self.has_next = False
        
        return list(chain(*self.results))