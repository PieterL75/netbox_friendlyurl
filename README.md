# netbox_friendlyurl
Create user-friendly url's for standard netbox/model/type/pk/ format

Install in the most common ways.

The links are build as 'search' parameters, relative to the model. The first parameter has to be the primary field of the model (name, vid, address, ...)
All values are searched for with case insensitive 'starts with'

format: 
* https://netbox/applabel/modelname/primairykey=value/
* https://netbox/applabel/modelname/primairykey=value|key=value/
* https://netbox/applabel/modelname/primairykey=value|key=value|key=value/ (as many as needed)

Use a | (pipe) as separator between the key=value pairs.
If you refer to related objects in the second keys, then you can either use the 'id' of the object, or you can use the 'name'. 
If an ID is expected, but a text is found, then an case insenitive exact lookup for the 'name' field is performed to find the correct ID. If that fails, then the pair is removed from the searchparameters

Examples:
* Link to VLAN with ID 3000: https://netbox/ipam/vlan/vid=3000/
* Link to a device starting with 'esx001' : https://netbox/dcim/devices/name=esx001/
* Link to VLAN with ID 1000 in VlanGroup Offices (ID 8) : https://netbox/ipam/vlan/vid=1000|group=8/
* Link to VLAN with ID 1000 in VlanGroup Offices (ID 8) : https://netbox/ipam/vlan/vid=1000|group=Offices/

If no unique object is found with those values, then you get redirected to the search enginge, with the primairykey value to be searched for and the object type set.
* https://netbox/dcim/devices/name=esx0/  -> gets redirected to https://netbox/search/?obj_types=dcim.device&q=esx0

