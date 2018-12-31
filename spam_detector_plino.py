# -*- coding: utf-8 -*-
"""
Created on Mon Dec 31 15:57:23 2018

@author: sujeeth.kumaravel
@reference: Plino API documentation
"""

import urllib.request
import json

def spam_detector_plino(text):
        
    # API's url
    url = "https://plino.herokuapp.com/api/v1/classify/"
    req = urllib.request.Request(url)
    
    # Add content-type header to the api call (The content that is going to be posted is encoded using utf-8 charset)
    req.add_header('Content-Type', 'application/json; charset=utf-8')
    
    # The content to be posted
    body={'email_text': text}
    
    # Convert the content into JSON encoded as utf-8
    json_data = json.dumps(body).encode('utf-8')
    
    # Add content-length header to the api call
    req.add_header('Content-Length', len(json_data)) 
    
    # Perform the call. Decode what comes back from the API.
    with urllib.request.urlopen(req, json_data) as f:
        responseJSON = f.read().decode('utf-8')

    return responseJSON