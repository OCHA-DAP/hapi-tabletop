import json
import csv

def compileHeaders(dbObj):
	headers = {}
	print(dbObj[0])
	longDefinition = dbObj[0].keys()

	idx = 0
	for field in longDefinition:
		if field != 'Key' and field !='Value':
			headers[field] = idx
			idx=idx+1

	return headers

def convertToListOfDicts(dbObj):
	headers = dbObj[0]
	output = []
	print(headers)

	templateRow = {}

	for row in dbObj[1:]:
		outputRow = {}
		for header in headers:
			outputRow[header] = None
		for idx,cell in enumerate(row):
			outputRow[headers[idx]] = cell
		output.append(outputRow)
	return output

def longToWideTransform(dbObj):
	headerLookup = compileHeaders(dbObj)
	currentRecord = -1
	currentISO = 'AAA'
	outputRow = []
	output = []
	for dbRow in dbObj:
		recordID = dbRow['Record_ID']
		if recordID != currentRecord:
			currentRecord = recordID
			output.append(outputRow)
			length = len(headerLookup)

			outputRow = [None] * length

			for field in dbRow:
				if field != 'Key' and field != 'Value':
					idx = headerLookup[field]

					outputRow[idx] = dbRow[field]
		
		value = dbRow['Value']
		key = dbRow['Key']

		if key not in headerLookup:
			headerLookup[key] = len(headerLookup)
			outputRow.append(None)

		idx = headerLookup[key]
		outputRow[idx] = value			

	output.append(outputRow)

	length = len(headerLookup)
	output[0] = [None] * length
	for header in headerLookup:
		place = headerLookup[header]
		output[0][place] = header

	output = convertToListOfDicts(output)

	return output

# results need to be sorted by recordID
def longToWide(dbObj):
	dbObj = longToWideTransform(dbObj)
	return dbObj

if __name__ == "__main__":
    longToWide()

