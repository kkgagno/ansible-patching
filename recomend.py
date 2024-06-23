# input text file
inputFile = "rec.txt"

# Enter the string
descrString = "description"
nanosString = "primaryImpact.costProjection.cost.nanos"
#print(descrString)
#print(nanosString)

# Opening the given file in read-only mode
with open(inputFile, 'r') as filedata:

   # Traverse in each line of the file
   
   for line in filedata:

      # Checking whether the given string is found in the line data
      
      if descrString in line:

         # Print the line, if the given string is found in the current line
         #print(line)
         descr = line.replace(" ", "").replace("description:","").replace("\n", " ")
         #descr = x.replace("\n", " ")
         print(descr)

      if nanosString in line:
         nanos = line.replace(" ", "").replace("\n", " ").replace("description:", "").replace("primaryImpact.costProjection.cost.nanos:", "")
         #nanos = x.replace("\n", " ")
         print(nanos)
# Closing the input file
filedata.close()
