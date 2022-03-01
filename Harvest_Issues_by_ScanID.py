#!/usr/bin/env python

################################################################################################
#
# **IMPORTANT** - Requires Bright Organizational or Personal API Key
# Before use, export your Bright Organizational or Personal API Key from the command line
# > export BRIGHT_API=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# 
# Usage: ./Harvest_Issues_by_ScanID.py [BRIGHT SCAN ID]
#
# - jharris 28FEB2022
#
################################################################################################

import os
import sys
import requests
import json

try:  
    os.environ['BRIGHT_API']
except KeyError:
    print("-------") 
    print("Please set and export the environment variable 'BRIGHT_API' with the following command:")
    print("export BRIGHT_API=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX")
    print("-------")
    sys.exit()

thisAPI = "Api-Key " + os.environ['BRIGHT_API']
if (len(sys.argv) > 1):
    thisScanID = sys.argv[1]
else:
    print("Usage: ./Harvest_Issues_by_ScanID.py [BRIGHT SCAN ID]")
    sys.exit()
thisURL = "https://app.neuralegion.com/api/v1/scans/" + thisScanID + "/issues"

def getIssues (ScanID):
    try:
        r = requests.get(thisURL, headers = {"Content-Type": "application/json",'Authorization': thisAPI})
        myJson = r.json()
        print("Success.")
        return myJson
    except Exception as e: 
        print(e)
        sys.exit()  

print("-------")
print("Attempting to harvest issues from scan ID: " + thisScanID + " ...")
thisJSONReturn = getIssues(thisScanID)
print("Writing results to file: issues.json")

with open("issues.json", "w") as write_file:
    json.dump(thisJSONReturn, write_file, indent=4)

print("-------")
