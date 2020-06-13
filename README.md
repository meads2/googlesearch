![image](docs/google-header.png)

# **Google Search**

This project aims to provide easy to use interface for working with Google Search results from the google API.

## **Getting Started**

#### **1.Get API Keys**
First check out the following site to get your own Google [API key](https://developers.google.com/custom-search/v1/overview) to enable making requests to the search engine service.

#### **2. Create a Search Engine**
After you have an API key you will need to create a [custom search engine](https://developers.google.com/custom-search/docs/tutorial/creatingcse). Make sure **"Search the entire web"** is enabled in the control panel. If this is not set your search engine will not return any results.

**Search Engine ID** Copy this value from the control panel you will need this value.

#### **3.Set Env Variables**
```bash
export GOOGLE_API_KEY=YOUR_API_KEY
export GOOGLE_SEARCH_ENGINE=SEARCH_ENGINE_ID
export
```

#### **4.Search Google**
```python
# Create Google Client
from pygooglesearch import GoogleSearch
gc = GoogleSearch(api_key=GOOGLE_API_KEY, search_engine=GOOGLE_SEARCH_ENGINE)

# Get Results
results = gc.get_results(q='coffee near me')
print(results)
```