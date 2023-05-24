import json
import csv, urllib.request

#loads the resource from HDX. Only works with CSV currently
def loadResource(url):
	response = urllib.request.urlopen(url)
	lines = [l.decode('utf-8') for l in response.readlines()]
	csv_reader = csv.reader(lines)
	list_of_csv = list(csv_reader)
	return list_of_csv


#takes in the header mapping, list of list data, and header rows and replaces headers
def replaceHeaders(headerRow,mappings,data):
	headerRow = headerRow - 1
	for idx, header in enumerate(data[headerRow]):
		for mapping in mappings:
			if mapping[0] == header:
				data[headerRow][idx] = mapping[1]
	return data


#removes rows between header and data
def removeRows(headerRow,dataRow,data):
	return [data[headerRow-1]] + data[dataRow-1:]


#add new columns as defined in fixed cols part of transformation file
def addFixedValues(fixedCols,data):
	for fixedCol in fixedCols:
		for idx, row in enumerate(data):
			if idx==0:
				data[idx].append(fixedCol['key'])
			else:
				data[idx].append(fixedCol['value'])

	return data


def transformToObject(longDefinition,coreDefinition,countryDefinition,data):
	longLookup = {}
	for definition in longDefinition:
		key = definition['header']
		longLookup[key] = None
		for idx,header in enumerate(data[0]):
			if header == key:
				longLookup[key] = idx

	indicatorLookup = {}
	for definition in coreDefinition:
		key = definition['header']
		indicatorLookup[key] = None
		for idx,header in enumerate(data[0]):
			if header == key:
				indicatorLookup[key] = idx

	for definition in countryDefinition:
		key = definition['header']
		indicatorLookup[key] = None
		for idx,header in enumerate(data[0]):
			if header == key:
				indicatorLookup[key] = idx

	dbObj = []

	for idx, row in enumerate(data[1:]):
		
		for indicator in indicatorLookup:
			dbRow = {}
			if indicatorLookup[indicator] is not None:
				place = indicatorLookup[indicator]
				value = row[place]
				dbRow['Key'] = indicator
				dbRow['Value'] = value
			else:
				dbRow['Key'] = indicator
				dbRow['Value'] = None
			

			for key in longLookup:
				if longLookup[key] is not None:
					place = longLookup[key]
					value = row[place]
					dbRow[key] = value
				else:
					dbRow[key] = None

			dbRow['Record_ID'] = idx

			dbObj.append(dbRow)

	return dbObj


def transform(indicator):
	#schema for db
	longDefinitionFile = 'definition_files/long_definition.json'

	with open(longDefinitionFile) as f:
	    longDefinition = json.load(f)

	#schema for individual indicator segments
	indicatorDefinitionFile = 'definition_files/'+indicator+'_definition.json'

	with open(indicatorDefinitionFile) as f:
	    indicatorDefinition = json.load(f)

	dbObj = []

	#loop for each country in the indicator
	for country in indicatorDefinition['fields']['country-specific']:

		#load the transformation config to go from resource to DB schema
		for transformation in country['transformations']:

			#get the resource and format
			data = loadResource(transformation['resource'])

			#replace the headers to standardised headers
			data = replaceHeaders(transformation['headerRow'],transformation['mappings'],data)

			#remove rows between and header and start of data
			data = removeRows(transformation['headerRow'],transformation['dataRow'],data)

			#add columns for fixed values
			data = addFixedValues(transformation['fixedCols'],data)

			#transform to defined DB object from definition files
			newObj = transformToObject(longDefinition['fields'],indicatorDefinition['fields']['core'], country['include'],data)
			dbObj = dbObj + newObj

	print(dbObj)

	return dbObj

if __name__ == "__main__":
    transform()

