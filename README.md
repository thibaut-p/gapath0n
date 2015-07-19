# gapath0n
In this repository we are sharing our *python code* for accessing the Getembed Building Performance Evaluation dataset. This could should make it much easier for a data scientist to grab the data and begin analysing it in SCIpy / their favourite flavour of analysis tools.

# Getembed.com - Data API Tutorial

This quick tutorial is designed to give people a head start in analysing the Building Performance Evaluation dataset.

During the AEC hackathon we discovered (there is no documentation on endpoints at right now but one can observe the API endpoints using firefox network dev tools to monitor the GET requests and) there is the following information available:

  - programmes
  - projects
  - entities
  - sensors

###List of all Building Performance Evaluation projects 
for the Building Performance Evaluation program (id: bfb6e716f87d4f1a333fd37d5c3679b2b4b6d87f)
http://www.getembed.com/4/programmes/bfb6e716f87d4f1a333fd37d5c3679b2b4b6d87f/projects/ 
###List of all buildings and their specific metadata (devices list, name, … )
for the project 99ec20944c13709a9b7faebbba87fdcfa3f30e55
http://www.getembed.com/4/projects/99ec20944c13709a9b7faebbba87fdcfa3f30e55/entities/ 

for the Aberfawr Terrace. Caerphilly 66a1ade5a7fecd82507b5eeaf83e16c5a1cf02fd
http://www.getembed.com/4/projects/66a1ade5a7fecd82507b5eeaf83e16c5a1cf02fd/entities/
 
###Time serie data 
for the building 2fda5e554c56225bdb16882b234ae786c2bf83e1
for the device 10d1a4cee29fe29c6572966a93b5a7b616446b94
device that has the sensor_id 10d1a4cee29fe29c6572966a93b5a7b616446b94
http://www.getembed.com/4/entities/2fda5e554c56225bdb16882b234ae786c2bf83e1/devices/10d1a4cee29fe29c6572966a93b5a7b616446b94/measurements/heatOutput?startDate=2012-04-18%2014:15:00&endDate=2014-08-31%2023:55:00 
