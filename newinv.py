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

if os.path.exists("disks.csv"):
    os.remove("disks.csv")
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
    #writer = csv.DictWriter(csvfile ,delimiter=',', fieldnames=['ip','name','zone','machinetype','project','created','license','status2'])
    fields = ['name','ip','zone','machinetype','project','created','license','status']
    writer = csv.DictWriter(csvfile,  fieldnames=fields)

# writing to disk csv file
with open('disks.csv', 'a',  newline='') as csvfile:
    # creating a csv dict writer object
    #writer = csv.DictWriter(csvfile ,delimiter=',', fieldnames=['ip','name','zone','machinetype','project','created','license','status2'])
    diskfields = ['name','ip','zone','project','disk','disksize(GB','type']
    writer = csv.DictWriter(csvfile,  fieldnames=diskfields)
 
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
        g = open('disks.csv', "a")
        try:
            ip = (line.strip())
            #print (ip)
            #print (",", end='')           
            for name in data['_meta']['hostvars'][line.strip()]['name']:            
                print("".join([name[0] for name in name.split()]), end='', file=i)
                instance = i.getvalue()
                instance2 = instance.strip()
            #print (instance2)
            i.truncate(0)          
                
                #z = str(name)
            #print (",", end='')                     
            for zone in data['_meta']['hostvars'][line.strip()]['zone']:
                print (zone, end='', file=i)
                zone = i.getvalue()
                zone2 = zone.strip()
            #print (zone)
            i.truncate(0)                
            #print (",", end='')            
            for machinetype in data['_meta']['hostvars'][line.strip()]['machineType']:
                print (machinetype, end='', file=i)
                machinetype = i.getvalue()
                machinetype2 = machinetype.strip()
            #print (machinetype)
            i.truncate(0)
            #print (",", end='')            
            for status in data['_meta']['hostvars'][line.strip()]['status']:
                print (status, end='', file=i)
                status = i.getvalue()
                status2 = status.strip()
            #print (status)
            i.truncate(0)
            #print (",", end='')            
            for project in data['_meta']['hostvars'][line.strip()]['project']:
                print (project, end='', file=i)
                project = i.getvalue()
            #print (project)
            i.truncate(0)
            #print (",", end='')            
            for creation in data['_meta']['hostvars'][line.strip()]['creationTimestamp']:
                print (creation, end='',file=i)
                creation = i.getvalue()
            #print (creation)
            i.truncate(0)
            #print (",", end='')            
            for license in data['_meta']['hostvars'][line.strip()]['disks'][0]['licenses']:
                    print (license, "\n", end='',file=i)
                    license1 = i.getvalue()
                    clean_license = license1.replace("\n", "  ")
                    #cleaner_license = clean_license + '\n'
            #print (clean_license)
            i.truncate(0)


        except KeyError as ke:
                #print(" None")
                clean_license = ("None" )
        #x = (instance2,",",ip, ",", zone2, ",", machinetype2, ",", project, ",", creation, ",", clean_license)
        print (instance2,",",ip, ",", zone2, ",", machinetype2, ",", project, ",", creation, ",", clean_license, ",", status2, "\n", file=f, end='')#, file=csv        
        try:
            jsonDisk = data['_meta']['hostvars'][line.strip()]['disks']
            for x in jsonDisk:
                diskname = x['deviceName']
                # keys = x.keys()
                #print(diskname)
                size = x['diskSizeGb'].strip()
                disktype = x['type'].strip()
                #print (size)
                # values = x.values()
                # print(values)
                print (instance2, ",", ip, ",", zone2, ",", project, ",", diskname, ",", size,",", disktype, "\n", file=g, end='')

        except KeyError as ke:
                #print(" None")
                diskname = ("None" )
with open (filename, "r") as file:
    filedata = file.read()





filedata = filedata.replace(remove, '')

with open(filename, "w") as file:
    file.write(filedata)
 




#with open(filename, 'rb+') as filehandle:
#    filehandle.seek(-1, os.SEEK_END)
#    filehandle.truncate()



#file = open('inventory.csv','r')
#lines = file.readlines()
#lines = lines[:-1]

##lines.append(lines[-1].strip())
#file.close()
#file = open('inventory.csv','w')
#file.writelines(lines)


#lines = open(filename, "r").readlines()
#lastline = (lines[-1].rstrip()- "\n"
#open(filename, 'w').writelines(lines)


with open(filename, "r")as r, open(
    'inventory2.csv', 'w') as o:
    data = r.read()
    data = data.replace('\000', '')
    o.write(data)



#with open( 
#    "inventory.csv", 'r') as r, open( 
#        'inventory2.csv', 'w') as o: 
      
#    for line in r: 
        #strip() function 
#        if line.strip(): 
#            o.write(line) 
  
#f = open("output.txt", "r") 
#print("New text file:\n",f.read())
