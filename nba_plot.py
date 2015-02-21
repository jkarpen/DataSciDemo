"""
Plot NBA Data for 2014-2015 
Age by position box plots
"""

import os
import sys
import csv
import argparse

import plotly.plotly as py


def get_nba_csv():
	"""
	Get path to nba csv file

	:return: path to nba csv
	"""
	parser = argparse.ArgumentParser()
	parser.add_argument('nba_csv')
	args = parser.parse_args()

	return args.nba_csv


def get_ages_positions(nba_csv):
	"""
	Get ages and positions in file

	:nba_csv: csv of nba data for 1 season
	:return: tuple of a list of ages and list of positions 
	"""
	ages = []
	positions = []
	with open(nba_csv, 'rb') as csv_handler:
		headers = csv_handler.readline()
		reader = csv.reader(csv_handler)
		for row in reader:
			position = row[2]
			age = row[3]
			ages.append(age)
			positions.append(position)

	return ages, positions



def main():
	nba_csv = get_nba_csv()
	ages, positions = get_ages_positions(nba_csv)


	print min(positions)
	print max(positions)
	print len(positions)

if __name__ == '__main__':
	sys.exit(main())