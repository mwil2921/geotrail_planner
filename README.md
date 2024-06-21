# Geotrail Planner

## Introduction
The Geotrail Planning Tool is a prototype designed for creating new geotrails in areas without existing infrastructure. This tool utilises a least cost path algorithm, incorporating weights determined by the Analytic Hierarchy Process (AHP), to generate optimal paths based on established trail best practices. The criteria used for planning are designed to ensure accessibility, safety, environmental preservation, and an enhanced visitor experience.

## Geotrail Trail Criteria
- **Slope**: Utilises gradual slopes with a maximum sustained grade of 15-20% and avoids construction on steeper slopes above 45 degrees to ensure lower maintenance costs and accessibility.
- **Contour Alignment**: Follows terrain contours to facilitate easy walking, ensuring smooth trail flow and proper water drainage.
- **Landforms**: Prefers ridgelines and higher, flatter landforms for lower construction costs and better scenic views, while avoiding valleys and pits.
- **Safety from Roads**: Maximises distance from roads to enhance safety and the overall walking experience.
- **Soil Type**: Prefers well-drained soils to mitigate erosion risks and reduce maintenance costs.
- **Geosites**: Prioritises proximity to geosites and points of interest to enhance educational and recreational value while avoiding direct access to prevent degradation.
- **Utility Infrastructure**: Maximises distance from powerlines and other infrastructure to avoid hazards and enhance the visitor experience.
- **Vegetation**: Selects aesthetically pleasing and ecologically valuable vegetation types, avoiding threatened vegetation.
- **Rivers and Waterbodies**: Minimises proximity to streams, rivers, and waterbodies to reduce crossings and construction costs while considering walker access to drinking water in remote areas.
- **Protected Areas**: Excludes special conservation zones and private freehold land by establishing strict no-travel buffers.
- **Threatened Species**: Establishes strict no-travel buffers around habitats of threatened species.

## Getting Started

### Prerequisites
- ArcGIS Pro
- Python environment compatible with ArcGIS Pro

### Usage
#### ArcGIS Pro Project
An ArcGIS Pro project has been provided, allowing you to explore and run the prototype with the included dataset based on a case study in Western Tasmania, Australia. Open the ArcGIS Pro project from the zip Geotrail_Planner.aprx and run the "Create Geotrail" geoprocessing tool in the Geotrail_Planner toolbox.

#### Python Script
A Python script that can be run as a Python toolbox is also available, and you will need to use the dataset in the zipped project as a sample. Use the Python scripts provided (AHP_criteria_weights.py and Geotrail_Tool_25M.pyt) to run the "Create Geotrail" geoprocessing tool.

If you would like to use your own dataset, you will need to prepare a standardised (1-9) dataset (recommended values in Williams et al., 2024) for each criterion. 

### Steps
1. **Set Parameters**: Define the parameters based on the criteria mentioned above, with weights determined by AHP.
2. **Choose trailheads**: Define the parameters for the origin and destination trailhead
3. **Ouput Geotrail**: Define the parameter for the output geotrail
4. **Run Tool**: Execute the least cost path algorithm to generate the optimal geotrail path.
5. **Review Output**: Analyse the generated path to ensure it meets all specified criteria and adjust parameters if necessary. Field validation is recommended to ensure it meets the needs of the targeted users.
6. **Finalise Path**: Save and export the finalised geotrail path for implementation.

## Additional Information

Note: the project will work without change if the project is extracted to C:\Geotrail_Tool\, otherwise modify INPATH variable in python script.

Created on Tue June 19, 2024

**Author**: Mark Williams  
**Affiliation**: University of Tasmania  
**Email**: [mark.williams@utas.edu.au](mailto:mark.williams@utas.edu.au)

Geotrail Least Cost Path Tool  
Python toolbox created using ArcGIS Pro 3.2.2  
Supplementary code associated with publication:

Williams, M.A., Rolls, S., McHenry, M.T. (2024). *Optimising Geotrail Planning by Leveraging Least-Cost Path for Sustainable Geotourism Development: A Case Study on a Tasmanian West Coast Post-Mining Landscape (under review).*
