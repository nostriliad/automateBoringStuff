#! python3

import os
import glob
import csv
from xlsxwriter.workbook import Workbook

subfolders = [f.path[2:] for f in os.scandir('.') if f.is_dir()]
rownames = [logfile[:-4] for logfile in sorted(os.listdir('./Z+50'))]

def extractDipoleMoment(logfile):
	with open(logfile) as fp:
		while 1:
			line = fp.readline()
			if 'Dipole moment' in line:
				line = fp.readline()
				data = line.split()[1:8:2]
				return data

with open('chem_logs.csv', 'w', newline='') as csvfile:
	logwriter = csv.writer(csvfile, delimiter=',',
							quotechar='|', quoting=csv.QUOTE_MINIMAL)
	for subfolder in subfolders:
		logwriter.writerow([subfolder, 'x', 'y', 'z', 'total'])
		chemlogs = sorted(os.listdir(subfolder))
		for chemlog in chemlogs:
			data = extractDipoleMoment(os.path.join('.', subfolder, chemlog))
			logwriter.writerow([chemlog[:-4], data[0], data[1], data[2], data[3]])
		logwriter.writerow([])
			

for csvfile in glob.glob(os.path.join('.', '*.csv')):
	workbook = Workbook(csvfile[:-4] + '.xlsx')
	worksheet = workbook.add_worksheet()
	with open(csvfile, 'rt', encoding='utf8') as f:
		reader = csv.reader(f)
		for r, row in enumerate(reader):
			for c, col in enumerate(row):
				worksheet.write(r, c, col)
	workbook.close()
	os.remove(csvfile)


