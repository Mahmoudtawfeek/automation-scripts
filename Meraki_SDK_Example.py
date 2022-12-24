#You can unhash the function that you only need.
#This is general code for show - update - add and delete some parameters to Meraki Dashboard using MerakiSdkClient
#Developed and organized and tested by Mahmoud Tawfeek
#Getting started with MerakiSdkClient platform to perform Meraki Automation
from meraki_sdk.meraki_sdk_client import MerakiSdkClient
import json
from pprint import pprint
#Entering Generated Token from API-Dashboard for your account in a hashing function
import maskpass
token = maskpass.askpass(prompt="Token: ", mask="#")
#Handling all of the authentication, storing a token for all of our requests
meraki = MerakiSdkClient(token)
#Getting a list of the organizations that are available
#I need to only manage an known organization that I am its admin
my_organizations = meraki.organizations.get_organizations()
#pprint(my_organizations)
my_certain_organization = input("The organization name that I need to manage name is: ")
#Now Lets dig deeper with MerakiSdkClient to get a list of Network IDs and other parameters
for certainorganization in my_organizations:
    if certainorganization["name"] == my_certain_organization:
        certainorganization_id = certainorganization["id"]
        #pprint("Organization ID is : " + str(certainorganization_id))
networkparams = {}
networkparams["organization_id"] = certainorganization_id
listofcertainorganizationnetworks = meraki.networks.get_organization_networks(networkparams)
#Now lets get some details from a specific network
#pprint(listofcertainorganizationnetworks)
my_specific_network = input("The specific network name that I need to manage name is: ")
for specificnetwork in listofcertainorganizationnetworks:
    if specificnetwork["name"] == my_specific_network:
        specificnetwork_id = specificnetwork["id"]
networkclients = {}
networkclients["network_id"] = specificnetwork_id
listofcertainorganizationnetworkclients = meraki.clients.get_network_clients(networkclients)
listofcertainorganizationnetworkstaticroutes = meraki.mx_static_routes.get_network_static_routes(specificnetwork_id)
pprint(listofcertainorganizationnetworkclients)
pprint(listofcertainorganizationnetworks)
pprint(listofcertainorganizationnetworkstaticroutes)

#Create .json file and convert it to excel sheet for simplicity
#import pandas as pd
#jsonfile_Clients = open("clients_in_GomlaMarketHQ.json","w")
#jsonfile_Clients.write (json.dumps(listofcertainorganizationnetworkclients))
#jsonfile_Clients.close()
#df_json_Clients = pd.read_json("clients_in_GomlaMarketHQ.json")
#df_json_Clients.to_excel("clients_in_GomlaMarketHQ.xlsx")
#jsonfile_Staticroutes = open("Staticroutes_in_GomlaMarketHQ.json","w")
#jsonfile_Staticroutes.write (json.dumps(listofcertainorganizationnetworkstaticroutes))
#jsonfile_Staticroutes.close()
#df_json_Staticroutes = pd.read_json("Staticroutes_in_GomlaMarketHQ.json")
#df_json_Staticroutes.to_excel("Staticroutes_in_GomlaMarketHQ.xlsx")

#Task1: Update static route for subnet 10.100.0.0/16 to be 10.100.0.0/24
#my_specific_route = input("The specific route name that I need to update is: ")
#for specificroute in listofcertainorganizationnetworkstaticroutes:
#    if specificroute["name"] == my_specific_route:
#        specificroute_id = specificroute["id"]
#routedict = {}
#routedict["network_id"] = specificnetwork_id
#routedict["sr_id"] = specificroute_id
#newroutes = meraki.mx_static_routes.get_network_static_route(routedict)
#pprint(newroutes)
#newroute = newroutes
#pprint(newroute)
#newroute['subnet'] = input("The required new subnet will be: ")
#updatedroute = {}
#updatedroute["network_id"] = specificnetwork_id
#updatedroute["sr_id"] = specificroute_id
#updatedroute["update_network_static_route"] = newroute
#result = meraki.mx_static_routes.update_network_static_route(updatedroute)
#result_update = meraki.mx_static_routes.get_network_static_route(routedict)
#pprint(result_update)

#Task2: Add new static route for subnet 10.100.1.0/24:
#newroute = {}
#routeparam = {}
#routeparam["gatewayIp"] = input("The gateway for the new route will be: ")
#routeparam["name"]=input("The name of the new route to be added will be: ")
#routeparam["subnet"]=input("The subnet that will be routed will be: ")
#newroute["network_id"] = specificnetwork_id
#newroute['create_network_static_route'] = routeparam 
#routing = meraki.mx_static_routes.create_network_static_route(newroute)
#pprint(routing)

#Task3: Delete unwanted routes (10.100.0.0/24 and 10.100.1.0/24)
#while True:
#    Questionnaire = input("Do you want to remove route? yes/no: ")
#    if Questionnaire.lower() == "yes" or Questionnaire.lower() == 'y':
#        my_specific_unwanted_route = input("The specific route name that I need to update is: ")
#        for unwantedspecificroute in listofcertainorganizationnetworkstaticroutes:
#            if unwantedspecificroute["name"] == my_specific_unwanted_route:
#                unwantedspecificroute_id = unwantedspecificroute["id"]
#        unwantedroutedict = {}
#        unwantedroutedict["network_id"] = specificnetwork_id
#        unwantedroutedict["sr_id"] = unwantedspecificroute_id
#        deleteroute = meraki.mx_static_routes.delete_network_static_route(unwantedroutedict)
        #pprint(listofcertainorganizationnetworkstaticroutes)
#    else:
#        input("Thanks for using our templates")
#        break