# W4-geospatial-data-project

# Objective

The objective of this project is to determine the perfect location for a new company in the gaming industry.

These are the employees preferences on where to place the new office:

3 POINTS
- Designers/Accont Managers 
- Designers --> near to companies that do design. (20 people)
- Account managers*--> travel a lot.(20 people) 
- CEO --> vegan.

2 POINTS
- Developers--> to be near tech startups that have raised at least 1 Million dollars. (15 people)
- Average age between 25 and 40 -->some place to go party.
- Executives --> like Starbucks.(10 people)

1 POINT
- Maintenance guy --> basketball court 
- Dog—"Dobby" --> hairdresser every month. 
- 30% of the company** --> have at least 1 child.


Based on all the information given by the employees, the first filters I applied to look for the best location between the three options (Seville, Madrid and Barcelona) are: 

 1. Starbucks
 2. Train stations
 3. Vegan restaurants
 4. Pet hairdressers

 # Working plan 
​​
Before first filtering using MongoDB I obtained a data set of three companies with coordinates located in Madrid, Barcelona and Seville.**. 
​
The coordinates were used to realice the API Foursquare calls using Starbucks, Stations, Vegans and Pet Hairdressers.
​
Once all the information was downloaded in json format, I made Geo Queries to obtain the services available in a perimeter of 500 meters around each of the coordinates,
​
For the final decision of the location I have made a parameter setting and assigned weights to each type of service. In the end, a ranking was obtained on which the final decision was based. 
​
The following resources have been used to achieve the objective of this project: 
​
-  [Foursquare API](https://foursquare.com/): get access to global data and  content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
- [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing. 

### Structure of the project files
​
The structure of this project is composed of:
 1. Geospatial_data_project.ipynb -->with the preliminary analysis where I search for places in the cities that meet the requirements and spatial queries to to check which of the cities meets the requirements within a 500 meter perimeter.
​
 2. scr folder: folder where all the .py files are stored with all the explained functions used during the whole project. 

 3. Output: all the dataframes imported and saved in csv format. 
​
​
# Libraries
​
[sys](https://docs.python.org/3/library/sys.html)
​
[requests](https://pypi.org/project/requests/2.7.0/)
​
[pandas](https://pandas.pydata.org/)
​
[dotenv](https://pypi.org/project/python-dotenv/)
​
[pymongo](https://www.mongodb.com/2)
​
[json](https://docs.python.org/3/library/json.html)
​
[os](https://docs.python.org/3/library/os.html)
​
[geopandas](https://geopandas.org/)
​
[shapely](https://pypi.org/project/Shapely/)
​
[reduce](https://docs.python.org/3/library/functools.html)
​
[operator](https://docs.python.org/3/library/operator.html)
​
[import dumps](https://pymongo.readthedocs.io/en/stable/api/bson/json_util.html)
​
[re](https://docs.python.org/3/library/re.html)