import csv

def readFromCSV(file_name):
	with open(file_name, 'r') as file:
		reader = csv.reader(file)
		ID = []
		for row in reader:
			
			ID.append(row[0])	
		
		ID[0] = ID[0][3:]
		return ID

if __name__ == '__main__':
	IDs = readFromCSV('ID.csv')
	print(IDs)