#api_to_index.py is a simple example api client that gets a position profile from 
#the postajob api, copies the nested addresses into a simpler flat structure
#and creates an xml document for each address.
import copy
import requests

from lxml import etree


def flatten_address(profile):
    flat_positions=[]
    addresses = copy.deepcopy(root.find('address'))
    #flat_positions = [copy.deepcopy(root) for address in addresses]
    for single_address in addresses:
        single_address.tag='address'
        newposition=copy.deepcopy(root)
        newposition.replace(newposition.find('address'), single_address)
        flat_positions.append(newposition)
    return flat_positions

def write_profiles(flat_positions):
    i=0
    for position in flat_positions:
        f=open(str(i)+'.xml', 'w')
        f.write(etree.tostring(position))
        i+=1

r=requests.get('http://127.0.0.1:8000/api/flat/positionprofile/3/?format=xml')
p=requests.post('http://127.0.0.1:8000/api/flat/positionprofile/?format=xml', r.content)
