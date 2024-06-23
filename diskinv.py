import json
import csv
import os
if os.path.exists("servers.txt"):
    os.remove ("servers.txt")
else:
    print("File does not exist.")
    
if os.path.exists("inventory.csv"):
    os.remove ("inventory.csv")
else:
    print("File does not exist.") 


if os.path.exists("diskinv.csv"):
    os.remove ("diskinv.csv")
else:
    print("File does not exist.")


import io
i=io.StringIO()   


remove = ("\000")
remove2 = ("^@")
# name of csv file
filename = "inventory.csv"
# writing to inventory csv file
with open('inventory.csv', 'a',  newline='') as csvfile:
    # creating a csv dict writer object
    fields = ['name','ip','zone','machinetype','project','created','license','status']
    writer = csv.DictWriter(csvfile,  fieldnames=fields)
 
    # writing headers (field names)
    writer.writeheader()
# Assuming 'data.json' contains your JSON data
with open('allinv.json', 'r') as f:
    data = json.load(f)
    



# writing to diskinv csv file
with open('diskinv.csv', 'a',  newline='') as csvfile:
    # creating a csv dict writer object
    fields = ['name','ip','zone','project','license']
    writer = csv.DictWriter(csvfile,  fieldnames=fields)
 
    # writing headers (field names)
    writer.writeheader()
# Assuming 'data.json' contains your JSON data
with open('allinv.json', 'r') as f:
    data = json.load(f)


# Accessing data from the loaded JSON
for item in data['_meta']['hostvars']:

    with open("servers.txt", "a") as f:
       print(item, file=f)

with open('servers.txt') as topo_file:
    for line in topo_file:
        f = open('inventory.csv', "a")
        g = open('diskinv.csv', "a")
        try:
            jsonDisk = data['_meta']['hostvars'][line.strip()]['disks']
            for x in jsonDisk:
                diskname = x['deviceName']
                # keys = x.keys()
                #print(diskname)
                size = x['diskSizeGb'].strip()
                #print (size)
                # values = x.values()
                # print(values)
                print (diskname, ",", size, "\n", file=g, end='')

        except KeyError as ke:
                #print(" None")
                diskname = ("None" )



