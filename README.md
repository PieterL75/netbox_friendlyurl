# netbox_friendlyurl
Create user-friendly url's for standard netbox/model/type/pk/ format

Install in the most common ways.

The links are build as 'search' parameters, relative to the model. The first parameter has to be the primariy field of the model (name, vid, address, ...)
format: 
* https://netbox/applabel/modelname/primairykey=value/
* https://netbox/applabel/modelname/primairykey=value/key=value/
* https://netbox/applabel/modelname/primairykey=value/key=value/key=value/ (as many as needed)

If no unique object is found with those values, then you get redirected to the search enginge, with the primairykey value to be searched for.
If you refer to related objects in the second keys, then you need to used the 'id' and not the name of the object.

Examples:
* Link to VLAN with ID 3000: https://netbox/ipam/vlan/vid=3000/
* Link to a device starting with 'esx001' : https://netbox/dcim/devices/name=esx001/
* Link to VLAN with ID 1000 in VlanGroup Offices (ID 8) : https://netbox/ipam/vlan/vid=1000/group=8/
