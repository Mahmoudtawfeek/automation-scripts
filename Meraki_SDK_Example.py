#Getting started with MerakiSdkClient platform to perform Meraki Automation
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint

#Entering Generated Token from API-Dashboard for your account in a hashing function
import maskpass
token = maskpass.askpass(prompt="Token: ", mask="#")

#Handling all of the authentication, storing a token for all of our requests
meraki = MerakiSdkClient(token)

#Getting a list of the organizations that are available.
my_organizations = meraki.organizations.get_organizations()
pprint(my_organizations)

