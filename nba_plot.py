#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
Plot NBA Data for 2014-2015
Age by position box plots
"""

import sys
import csv
import argparse

import plotly.plotly as py
from plotly.graph_objs import Data, Layout, YAxis, XAxis
from plotly.graph_objs import Figure, Box, Marker, Line


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


def get_ages_positions(nba_csv, yaxis_col, positions_col):
    """
    Get yaxis and nba positions in file

    :nba_csv: csv of nba data for 1 season
    :yaxis_col: column number for yaxis values
    :positions_col: column number for positions values
    :return: tuple of a list of yaxis and list of nba positions
    """
    yaxis = []
    positions = []
    with open(nba_csv, 'rb') as csv_handler:
        # remove headers
        csv_handler.readline()
        reader = csv.reader(csv_handler)
        for row in reader:
            position_value = row[positions_col]
            yaxis_value = row[yaxis_col]
            if position_value in POSITIONS:
                yaxis.append(yaxis_value)
                positions.append(POSITIONS[position_value])

    return yaxis, positions


def plot(yaxis_values, positions, yaxis_title,
         xaxis_title, plot_title, box_name):
    """
    Plot nba data

    :ages: list of the ages of players
    :positions: list of the positions
    :yaxis_title: title of the yaxis
    :xaxis_title: title of the xaxis
    :plot_title: title of the plot
    :box_name: name of the box

    :return:  None, data sent to plotly via API
    """
    data = Data([
        Box(
            y=yaxis_values,
            x=positions,
            name=box_name,
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
        title=plot_title,
        showlegend=False,
        autosize=True,
        width=792,
        height=469,
        xaxis=XAxis(
            title=xaxis_title,
            range=[-0.6799999999999999, 6.5],
            type='category',
            autorange=True,
            showexponent='all',
            side='bottom'
        ),
        yaxis=YAxis(
            title=yaxis_title,
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
    py.plot(fig)


def main():
    nba_csv = get_nba_csv()
    yaxis, positions = get_ages_positions(nba_csv, 3, 2)
    yaxis_title = 'Age'
    xaxis_title = 'Positions'
    plot_title = 'NBA Player Age by Position 2014-15 Season'
    box_title = 'Age'
    plot(yaxis, positions, yaxis_title, xaxis_title, plot_title, box_title)


if __name__ == '__main__':
    sys.exit(main())
