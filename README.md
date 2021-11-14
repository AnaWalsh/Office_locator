# W4-geospatial-data-project

# Objective

The objective of this project is to determine the perfect location for a new company in the gaming industry.

These are the employees preferences on where to place the new office:

Muy importante : 40/65 - 3 PUNTOS
- Designers/Accont Managers 
- Designers --> near to companies that do design. (20 people)
- Account managers*--> travel a lot.(20 people) 

Normal - 2 PUNTOS
- Developers--> to be near tech startups that have raised at least 1 Million dollars. (15 people)
- Average age between 25 and 40 -->some place to go party.
- Executives --> like Starbucks.(10 people)


Nos da igual - 1 PUNTO
- CEO --> vegan.
- Maintenance guy --> basketball court 
- Dog—"Dobby" --> hairdresser every month. 
- 30% of the company** --> have at least 1 child.


Based on all the information given by the employees, the first filters I applied to look for possible locations were:

 1. Spanish companies.
 2. In the web sector to be surrounded by companies that are in a similar sector to ours.
 3. With less than 50 employees, to be surrounded by small companies like us
 4. Created since 2007 to be surrounded by young companies.

 # Working plan 
​​
Before first filtering using MongoDB I obtained a set of XXX companies with coordinates located in **Madrid, Barcelona, Bilbao, Gijón**. 
​
The coordinates were used to realice the API Foursquare calls using Bars, Preschool, Court Basketball, vegan restaurants and train stations. 
​
Once all the information was downloaded in json format, I made a calculation of the distances between the coordinates of origin and the information obtained from Foursquare. 
​
For the final decision of the location I have made a normalisation and assigned weights to the distances obtained. In the end, a ranking was obtained on which the final decision was based. 
​
The following resources have been used to achieve the objective of this project: 
​
-  [Foursquare API](https://foursquare.com/): get access to global data and  content from thousands trusted sources. To access all the necessary information about the resources surrounding the possible locations of the enterprise. 
- [MongoDB](https://www.mongodb.com/): is a document database with the scalability and flexibility that we want using querying and indexing. 

### Structure of the project files
​
The structure of this project is composed of:
 1. A folder of notebooks: 
    
    a) **Explore_Companies.ipynb** -->with the preliminary analysis where I search for companies that meet the requirements established a priori to be able to pre-select locations. 
​
    b) **APIs.ipynb** --> the call is made to the Api of "Foursquare Developers", where we will get some preferred conditions where we want our company to be located. 
​
    c) **Geospatial queries.ipynb** --> we make the spatial queries to calculate the distance between each point obtained in the Foursquare API and the locations selected at the beginning.
​
    d) **Madrid vs Barcelona vs Sevilla.ipynb** --> the relationship between each selected parameter (train stations, bars, vegan restaurants, basketball courts, and children's schools) and the possible locations (Madrid, Barcelona, Gijon and Bilbao) is evaluated. For this purpose, a normalisation and categorisation has been used. 
​
 2. scr folder: folder where all the .py files are stored with all the explained functions used during the whole project. The .py files included are: 
    a) APIsFunctions used in the APIs.ipynb
    b) GeospatialFunctions used in the Gespatial queries.ipynb
    c) CleaningFunctions used in the Madrid vs Barcelona vs Bilbao vs Gijon.ipynb
​
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