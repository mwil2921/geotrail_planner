# -*- coding: utf-8 -*-
"""
Created on Tue June 19 2024
@author: Mark Williams
University of Tasmania
mark.williams@utas.edu.au
AHP priority calculated for geotrail criteria weights
Example: calculates weights of trail criteria for a geotrail based on trail preferences for Wilderness Adventurer's personas
Credit: https://github.com/PhilipGriffith/AHPy
Alternatively use AHP Priority Calculator https://bpmsg.com/ahp/ahp-calc.php

Williams, M.A., Rolls, S., McHenry, M.T.(2024).Optimising Geotrail Planning by Leveraging Least-Cost Path for Sustainable Geotourism Development: A Case Study on a Tasmanian West Coast Post-Mining Landscape.
"""

import ahpy

def ahp_trail_criteria():
    # Use a breakpoint in the code line below to debug your script.
    trail_criteria = {('Slope', 'Landforms'): 1 / 5, ('Slope', 'Distance to Roads'): 1 / 6,
                         ('Slope', 'Distance to Geosites'): 1 / 3,
                         ('Slope', 'Distance to Powerline Easements'): 1 / 7, ('Slope', 'Distance to Rivers'): 1 / 3,
                         ('Slope', 'Soil Drainage'): 1 / 3, ('Slope', 'Vegetation Communities'): 1 / 6,

                         ('Landforms', 'Slope'): 5, ('Landforms', 'Distance to Roads'): 4,
                         ('Landforms', 'Distance to Geosites'): 3,
                         ('Landforms', 'Distance to Powerline Easements'): 3, ('Landforms', 'Distance to Rivers'): 7,
                         ('Landforms', 'Soil Drainage'): 5, ('Landforms', 'Vegetation Communities'): 2,

                         ('Distance to Roads', 'Slope'): 6, ('Distance to Roads', 'Landforms'): 1 / 4,
                         ('Distance to Roads', 'Distance to Geosites'): 1 / 3,
                         ('Distance to Roads', 'Distance to Powerline Easements'): 1 / 2, ('Distance to Roads', 'Distance to Rivers'): 3,
                         ('Distance to Roads', 'Soil Drainage'): 5, ('Distance to Roads', 'Vegetation Communities'): 3,

                         ('Distance to Geosites', 'Slope'): 3, ('Distance to Geosites', 'Landforms'): 1 / 3,
                         ('Distance to Geosites', 'Distance to Roads'): 3,
                         ('Distance to Geosites', 'Distance to Powerline Easements'): 1 / 3, ('Distance to Geosites', 'Distance to Rivers'): 3,
                         ('Distance to Geosites', 'Soil Drainage'): 4, ('Distance to Geosites', 'Vegetation Communities'): 1,

                         ('Distance to Powerline Easements', 'Slope'): 7, ('Distance to Powerline Easements', 'Landforms'): 1 / 3,
                         ('Distance to Powerline Easements', 'Distance to Roads'): 2,
                         ('Distance to Powerline Easements', 'Distance to Geosites'): 3, ('Distance to Powerline Easements', 'Distance to Rivers'): 3,
                         ('Distance to Powerline Easements', 'Soil Drainage'): 2, ('Distance to Powerline Easements', 'Vegetation Communities'): 2,

                         ('Distance to Rivers', 'Slope'): 3,('Distance to Rivers', 'Landforms'): 1 / 7,
                         ('Distance to Rivers', 'Distance to Roads'): 1 / 3,
                         ('Distance to Rivers', 'Distance to Geosites'): 1 / 3,('Distance to Rivers', 'Distance to Powerline Easements'): 1 / 3,
                         ('Distance to Rivers', 'Soil Drainage'): 1 / 2,('Distance to Rivers', 'Vegetation Communities'): 1 / 3,

                         ('Soil Drainage', 'Slope'): 3, ('Soil Drainage', 'Landforms'): 1 / 5,
                         ('Soil Drainage', 'Distance to Roads'): 1 / 5,
                         ('Soil Drainage', 'Distance to Geosites'): 1 / 4, ('Soil Drainage', 'Distance to Powerline Easements'): 1 / 2,
                         ('Soil Drainage', 'Distance to Rivers'): 2, ('Soil Drainage', 'Vegetation Communities'): 1 / 3,

                         ('Vegetation Communities', 'Slope'): 6, ('Vegetation Communities', 'Landforms'): 1 / 2,
                         ('Vegetation Communities', 'Distance to Roads'): 1 / 3,
                         ('Vegetation Communities', 'Distance to Geosites'): 1, ('Vegetation Communities', 'Distance to Powerline Easements'): 1 / 2,
                         ('Vegetation Communities', 'Distance to Rivers'): 3, ('Vegetation Communities', 'Soil Drainage'): 3,

                         }
    trail = ahpy.Compare(name='Trail_criteria', comparisons=trail_criteria, precision=3, random_index='saaty')
    print(trail.target_weights)
    print(trail.consistency_ratio)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    ahp_trail_criteria()

