import requests
import pprint
import pandas as pd
import csv
import re
from datetime import datetime
from dateutil.parser import parse
from datetime import datetime
import matplotlib.pyplot as plt

class ExtractData(object):
	pp = pprint
	total_projects = 0
	total_entities = 0
	total_devices = 0
	houses_with_no_devices = 0
	device_ids = []
	device_types = {}
	device_types_df = pd.DataFrame()
	device_types = ["absoluteHumidity","barometricPressure","co2","currentSignal","electricityAmps","electricityConsumption","electricityExport","electricityFrequency","electricityGeneration","electricityImport","electricityKiloVoltAmpHours","electricityKiloWatts","electricityVolts","electricityVoltAmps","electricityVoltAmpsReactive","flowRateAir","flowRateLiquid","gasConsumption","heatConsumption","heatExport","heatGeneration","heatImport","heatTransferCoefficient","liquidFlowRate","oilConsumption","powerFactor","pulseCount","relativeHumidity","relativeHumidity","solarRadiation","status","temperatureAir","temperatureAmbient","temperatureFluid","temperatureGround","temperatureRadiant","temperatureSurface","thermalEnergy","time","voltageSignal","waterConsumption","windDirection","windSpeed"]
	housesWithElectricityConsumptionIds =[]
	device_types_do_not_match = []
	total_device_types = []

	def deviceTypesLower(self):
		aux = []
		for d in self.device_types:
			aux.append(d.lower())

		self.device_types = aux

	def getProjects(self):
		r = requests.get('http://www.getembed.com/4/programmes/bfb6e716f87d4f1a333fd37d5c3679b2b4b6d87f/projects/')

		# with open('electric_filtered_data.csv', 'wb') as csvfile:
		# 	filtered_data_file = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)

		with open('bpe_out.csv', 'wb') as csvfile:
			spamwriter = csv.writer(csvfile, delimiter=',',quotechar='|', quoting=csv.QUOTE_MINIMAL)
			#spamwriter.writerow(['project_id', 'entity_id','device_id','sensor_id','reading_type','unit'])
			
			# Get entities that meet the requirements
			#entitiesWithAllRequirements = self.getEntitiesWithAllRequirements()
	
			if r.status_code == 200:
	
				projects = r.json()
				self.total_projects = len(projects)
	
				# Iterate over projects 
				for p in projects:
	
					total,entities = self.getEntities(p['project_id'])
					self.total_entities += total
	
					# Iterate over entities
					for e in entities:
						
						# Check that the entities is valid according requirements
						#if e['entity_id'] in entitiesWithAllRequirements:
							
						self.total_devices = self.total_devices + len(e['devices'])
						
						if len(e['devices']) == 0:
							self.houses_with_no_devices += 1
						
						#Iterate over devices
						for device in e['devices']:
							readings = device['readings']
		
							# Iterate over readings
							for reading in readings:
								
								# Get entities that match the type or device
								#print p['project_id']
								#self.getEntitiesMatchType(reading,device['entity_id'],filtered_data_file)
								device_type = reading['type'].lower()
								self.total_device_types.append(device_type)
								
								if device_type != None:
									device_type = device_type.encode('utf-8','replace')
	
								unit = reading['unit']
								if unit != None:
									unit = unit.encode('utf-8','replace')

								try:
									alias = reading['alias'].encode('utf-8','replace')
								except Exception, exc:
									alias = None
								try:
									type = reading['type'].encode('utf-8','replace')
								except Exception, exc:
									type = None

								spamwriter.writerow([e['entity_id'], reading['device_id'],device_type,unit,alias,reading['upper_ts'],reading['lower_ts']])
								#filtered_data_file.writerow([entity_id, reading['device_id'],type,reading['unit'],alias,reading['upper_ts'],reading['lower_ts']])
		
								# Count how many devices are used and store it in a Dataframe
								if device_type in self.device_types:
									try:
										self.device_types_df.loc[device_type,'count'] = self.device_types_df.loc[device_type,'count'] + 1
									except Exception, exc:
										self.device_types_df.loc[device_type,'count'] = 1
								else:
									self.device_types_do_not_match.append(device_type)


		print "Total Projects: {} Total Entities: {}  Total Devices: {} Entities With No Devices: {} Total Readings: {} Readings With No Standard Reading Types: {}".format(self.total_projects,self.total_entities,self.total_devices,self.houses_with_no_devices,len(self.total_device_types),len(self.device_types_do_not_match))
		print self.device_types_df.sort(['count'], ascending=False)
		#self.pp.pprint(set(self.housesWithElectricityConsumptionIds))
		#self.pp.pprint(set(self.housesWithElectricityConsumptionIds))
		# self.pp.pprint(self.housesWithElectricityConsumptionIds)

	def getEntities(self,project_id):

		r = requests.get('http://www.getembed.com/4/projects/'+str(project_id)+'/entities/')

		if r.status_code == 200:
			entities = r.json()
			#self.pp.pprint(entities['entities'])
			total = entities['total_hits']
			return total,entities['entities']

	def getEntitiesMatchType(self,reading,entity_id,filtered_data_file):
		
		#if re.search('.*electricityConsummption.*', reading['type'].lower()) != None:
		#if re.search('electricityconsumption', reading['type'].lower()) != None:
		if reading['type'].lower() == 'electricityconsumption':

			aux = {}
			aux['entity_id'] = entity_id
			aux['device_id'] = reading['device_id']
			aux['type'] = reading['type']
			aux['unit'] = reading['unit']
			aux['alias'] = reading['alias']
			aux['upper_ts'] = reading['upper_ts']
			aux['lower_ts'] = reading['lower_ts']

			try:
				alias = reading['alias'].encode('utf-8','replace')
			except Exception, e:
				alias = None
			try:
				type = reading['type'].encode('utf-8','replace')
			except Exception, e:
				type = None

			#filtered_data_file.writerow([entity_id, reading['device_id'],type,reading['unit'],alias,reading['upper_ts'],reading['lower_ts']])
	
			#self.housesWithElectricityConsumptionIds.append(entity_id)
			print "E: {} D:{}".format(entity_id,reading['device_id'])
			self.housesWithElectricityConsumptionIds.append(aux)
			#print aux

	# GEt all the entities that have Total Primary Energy Requirement and Space Heating Requirement
	def getEntitiesWithAllRequirements(self):
		entitiesWithAllRequirements = []
		with open('buildings.csv', 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			for row in spamreader:
				if 'getembed' not in row[3]:
					entitiesWithAllRequirements.append(row[3])

		return entitiesWithAllRequirements[1::]

	def getMeasurements(self):
		#with open('electric_filtered_data.csv', 'rb') as csvfile:
		with open('bpe_out.csv', 'rb') as csvfile:
			spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
			df = pd.DataFrame()
			for row in spamreader:
				#r = requests.get('http://www.getembed.com/4/entities/'+str(row[0])+'/devices/'+str(row[1])+'/measurements/'+str(row[2])+'?startDate='+str(row[5])+'&endDate='+str(row[6]))
				#print row[5]
				
				upper_ts = row[5].split("T")[0] + ' 00:00:00'
				lower_ts = row[6].split("T")[0] + ' 00:00:00'
				# print upper_ts
				# lower_ts = '2014-01-01 00:00:00'
				# upper_ts = '2014-02-01 00:00:00'				
				# upper_ts = parse(row[5])
				# lower_ts = parse(row[6])
	
				#print type(parse(row[5]))
				#datetime.datetime(2015, 2, 24, 13, 0, tzinfo=tzoffset(None, -28800))
				#datetime.datetime.strptime('24052010', "%d%m%Y").date()
				r = requests.get('http://www.getembed.com/4/entities/'+str(row[0])+'/devices/'+str(row[1])+'/measurements/'+str(row[2])+'?startDate='+str(lower_ts)+'&endDate='+str(upper_ts))
				#print r.status_code
				print r.text
				measurements = r.json()
				measurements = measurements['measurements']

				print "Total Number of measurements: {}".format(len(measurements))
				print "Project ID: {} Device Id: {} Total Number Of measurements: {}".format(row[0],row[1],len(measurements))

				# for m in measurements:
				# 	#print m
				# 	date = parse(m['timestamp'])
				# 	#print date
				# 	#print m['timestamp'][0:10]
				# 	try:
				# 		#df.loc[str(date),'sensor_id'] = m['value']
				# 		try:
				# 			#df.loc[str(date),row[0]] = df.loc[str(date),row[0]] + m['value']
				# 			df.loc[m['timestamp'][0:10],row[0]] = df.loc[m['timestamp'],row[0]] + m['value']
				# 		except Exception, e:
				# 			df.loc[m['timestamp'][0:10],row[0]] = m['value']
						
				# 	except Exception, e:
				# 		print "issue"
				# 		print e
				# 		print m

				print len(measurements)
				#break
				# df.plot()
		return df


ed = ExtractData()
# ed.getEntitiesWithAllRequirements()
ed.deviceTypesLower()
ed.getProjects()
df = ed.getMeasurements()
