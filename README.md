# webscraper

Project with AiCore involved creating a Webscraper for coinmarketcap.com
this Webscraper would scrape the various attributes of cryptocurrencies from the popular tracking website coinmarketcap.com

Selenium was utilised for automating the webscraper

1. prototyping the webscraper:

before being able to access the website a cookies iframe had appeared, in the initiliser the webscraper was designed to immediateley click this so that the webpage could be manipulated

The second hurdle in this project was creating a class which could navigate the website & swap inbetween webpages
two key methods had been tested: scrolling until next element visable and scrolling by a certian pixel amount at this point both were viable options.

In order to swap pages the webscraper also had to be able to have the next page button visable before attempting to click it.

2. Retrieving details

Now that the website could be successfully navigated i could begin the process of scraping data.
after trial & error the best way to structure this would be within a dictionary comprehension.
for each element in this list of dictionaries we would need to have identifiable bits of information.
For this a UUID string was utilised to act as a global unique identifier, for a more obvious identifier 
we also collected each coins name & symbol, which being cryptocurrency coins will always be unique
other key information about coins was collected such as their market cap & price.

Some coins would have missing attributes such as a missing price, for these a NoSuchElementException was used to skip these results without crashing the webscraper

These details were saved as a json file by creating a write method which used the json.dump() method, here it is important to note a funny setback, whilst attempting to test this json file json.dumps was used unnoticed so all testing methods was attempting to analyse a string object rather than the list of dictionaries in json format as intended

Alongside this an additional mothod was used to save the image date for each coin, in this case the urlib import was used & using a combination of the images srs element with a '.png' string each image could be saved as a png within a seperate Coin_Images file.

3. Documentation & testing

As the code project had now reached a point whereas it was in a draft version with features working as intended docstrings are added to explain the use of each method, this would make it far easier to understand the logic & reproduce this webscraper,

Now we have a output in the form of a json file with all of our results an aditional testing file could be created to ensure that for future runs any errors could be more easily traced back using the inbuilt unittest module, for the testing of this project we would only initilise a few tests, as more would be created as the project progressed, at the moment these tests checked that all dictionary keys existed, that the json file was a list & that inside of that list dictionaries existed

4. Scalably Storing Data

Images are stored with the cryptocurrencies Symbol as an identifier, originally a method was created that would save the images as a .png file which could be uploaded, however this would create problems in importing to SQL & taking a large amount of time to upload correctly to AWS S3. Instead image data is saved via the images url in a json file.

All data is uploaded to an AWS S3 bucket stored as json files. this data is then connected to an AWS RDS instance via a Boto3 method, from here we can connect to a postgreSQL server to manipulate the data in an SQL format, as for right now the only this to do is to create an inner join which would use the symbol from both data sets to assign the coins image url to its dataset
