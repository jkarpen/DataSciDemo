=============
Description
=============

NBA Box Plots for age by position for 1 season

This script is intended to work with python 2.7

A Plotly account and API key is required for this code to run properly. 

Here is Plotly's Python API documentation: 
https://plot.ly/python/overview/

Here are two good starter tutorials:
http://www.blog.pythonlibrary.org/2014/10/27/plotting-data-online-via-plotly-and-python/
http://www.wired.com/2013/12/creating-plots-with-python-and-plotly/

The data we used contains info on individual NBA players in the 2014-15 season (ongoing). 
The variables we used for our visual are player position (PG, SF, PF, SG, C) on the x axis and with player age on the y axis.
However, any categorical variable can be used on the x axis to split the box plots, and any continuous variable can be on the y
axis to create the distribution. 

=============
Sample Usage
=============

``python nba_ploy.py nba_14_15.csv``
