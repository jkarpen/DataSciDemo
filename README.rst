=============
Interactive Data Visualization with Plotly/Python
=============

This repository is comprised of a script and data set used to present Plotly and Python at the Data Science FunConference, 
San Diego, CA on Sat, Feb 28, 2015.

Presenters:

* jkarpen
* jkrooskos

------------------
Data Visualization
------------------

The data visualization may be viewed `here. <https://plot.ly/~jkarpen/143/nba-player-age-by-position-2014-15-season/>`_

-----------
Description
-----------
The code is used to create a box plot of NBA data for age by position for 1 season.

The data we used contains info on individual NBA players in the 2014-15 season (ongoing). 
The variables we used for our visual are player position (PG, SF, PF, SG, C) on the x axis and with player age on the y axis.
However, any categorical variable can be used on the x axis to split the box plots, and any continuous variable can be on the y
axis to create the distribution. 

------------
Requirements
------------

* This script is intended to work with Python 2.7
* A Plotly account and API key 

Here is Plotly's Python API documentation:

* https://plot.ly/python/overview/

Here are two good starter tutorials:

* http://www.blog.pythonlibrary.org/2014/10/27/plotting-data-online-via-plotly-and-python/
* http://www.wired.com/2013/12/creating-plots-with-python-and-plotly/

------------
Sample Usage
------------

``python nba_ploy.py nba_14_15.csv``
