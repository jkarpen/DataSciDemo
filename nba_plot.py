#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Plot NBA Data for 2014-2015 
Age by position box plots
"""

import os
import sys
import csv
import argparse

import plotly.plotly as py
from plotly.graph_objs import *


POSITIONS = {
	'PF': 'Power Forward',
	'SG': 'Shooting Guard',
	'C': 'Center',
	'SF': 'Small Forward',
	'PG': 'Point Guard',
}


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
			if position in POSITIONS:
				ages.append(age)
				positions.append(POSITIONS[position])

	return ages, positions


def plot(ages, positions):
	"""
	Plot nba data

	:ages: list of the ages of players
	:positions: list of the positions

	:return:  None, data sent to plotly via API  
	"""
	data = Data([
	    Box(
	        y=ages,
	        x=positions,
	        name='AGE',
	        boxmean=True,
	        boxpoints='all',
	        jitter=0.5,
	        whiskerwidth=0.5,
	        fillcolor='rgb(106, 168, 79)',
	        marker=Marker(
	            color='rgba(7, 55, 99, 0.5)',
	            size=4,
	            symbol='circle',
	            opacity=0.7
	        ),
	        line=Line(
	            color='rgba(7, 55, 99, 0.5)',
	            width=2
	        ),
	        opacity=1,
	        showlegend=False
	    )
	])
	layout = Layout(
	    title='NBA Player Age by Position 2014-15 Season',
	    showlegend=False,
	    autosize=True,
	    width=792,
	    height=469,
	    xaxis=XAxis(
	        title='Position',
	        range=[-0.6799999999999999, 6.5],
	        type='category',
	        autorange=True,
	        showexponent='all',
	        side='bottom'
	    ),
	    yaxis=YAxis(
	        title='Age',
	        range=[17.944444444444443, 39.05555555555556],
	        type='linear',
	        autorange=True,
	        showexponent='all'
	    ),
	    paper_bgcolor='rgb(255, 255, 255)',
	    plot_bgcolor='rgb(217, 217, 217)',
	    hovermode='closest',
	    boxmode='overlay',
	    boxgap=0.4,
	    boxgroupgap=0.4
	)
	fig = Figure(data=data, layout=layout)
	plot_url = py.plot(fig)


def main():
	nba_csv = get_nba_csv()
	ages, positions = get_ages_positions(nba_csv)
	plot(ages, positions)


if __name__ == '__main__':
	sys.exit(main())