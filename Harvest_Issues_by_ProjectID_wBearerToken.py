#!/usr/bin/env python

################################################################################################
#
# **IMPORTANT** - Requires Bright Organiztional or Personal API Key
# Before use, export your Bright Organiztional or Personal API Key from the command line
# > export BRIGHT_API=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
# 
# Usage: ./Harvest_Issues_by_ProjectID_wBearerToken.py [BRIGHT PROJECT ID]
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

myAPI = "Api-Key " + os.environ['BRIGHT_API']
myUsername = os.environ['BRIGHT_USERNAME']
myPassword = os.environ['BRIGHT_PASSWORD']
if (len(sys.argv) > 1):
    myProjectID = sys.argv[1]
else:
    print("Usage: ./Harvest_Issues_by_ScanID.py [BRIGHT SCAN ID]")
    sys.exit()
myURL = "https://app.neuralegion.com/api/v1/projects/" + myProjectID + "/issues"

def getBearerToken(inUsername, inEmailPass):
    try:
        thisPayload = {"email":inUsername,"password":inEmailPass}
        thisURL = "https://app.neuralegion.com/api/v1/auth/login"
        r = requests.post(thisURL, data = thisPayload)
        thisTokenJson = json.loads(r.text)
        for (thisKey, thisVal) in thisTokenJson.items():
            if (thisKey == "accessToken"):
                thisReturn = thisVal
                break
        return thisReturn
    except Exception as e: 
        print(e)
        sys.exit()

def getIssues (inBearer):
    inBearer = "Bearer " + str(inBearer)
    try:
        r = requests.get(myURL, headers = {"Content-Type": "application/json",'Authorization': inBearer})
        myJson = r.json()
        print("Success.")
        return myJson
    except Exception as e: 
        print(e)
        sys.exit()  

print("-------")
myBearerToken = getBearerToken(myUsername, myPassword)
print(myBearerToken)
print("Attempting to harvest issues from scan ID: " + myProjectID + " ...")
thisJSONReturn = getIssues(myBearerToken)
print("Writing results to file: issues.json")

with open("issues.json", "w") as write_file:
    json.dump(thisJSONReturn, write_file, indent=4)

print("-------")
