# webscraper

1. Hello World

- initial step of this project would to be to select a website to base this webscraper on, for myself i have an interest withis the cryptocurrency space, so this is what i will be basing this project upon.

- One of/if not the largest tracking websites of cryptocurrencies is coinmarketcap.com, so for this project I will be scraping data off their website building a framework which can scalably store this data & run a virtual version of my scraper :)


2. prototyping the webscraper

- Before being able to access the website a cookies iframe had appeared, in the initiliser the webscraper was designed to immediateley click this so that the webpage could be manipulated

- The second hurdle in this project was creating a class which could navigate the website & swap inbetween webpages
two key methods had been tested: scrolling until next element visable and scrolling by a certian pixel amount at this point both were viable options.

- In order to swap pages the webscraper also had to be able to have the next page button visable before attempting to click it.


3. Retrieving details

- Now that the website could be successfully navigated i could begin the process of scraping data.
after trial & error the best way to structure this would be within a dictionary comprehension.

- For each element in this list of dictionaries we would need to have identifiable bits of information.
For this a UUID string was utilised to act as a global unique identifier

- For a more obvious identifier we also collected each coins name & symbol, which being cryptocurrency coins will always be unique
other key information about coins was collected such as their market cap & price.

- Some coins would have missing attributes such as a missing price, for these a NoSuchElementException was used to skip these results without crashing the webscraper

- These details were saved as a json file by creating a write method which used the json.dump() method, here it is important to note a funny setback, whilst attempting to test this json file json.dumps was used unnoticed so all testing methods was attempting to analyse a string object rather than the list of dictionaries in json format as intended

- Alongside this an additional mothod was used to save the image data for each coin, this was inserted inside the same loop which collected coin attributes, in this instance the image url was collected & appended to the coins dictionary


4. Documentation & testing

- As the code project had now reached a point whereas it was in a draft version with features working as intended docstrings are added to explain the use of each method, this would make it far easier to understand the logic & reproduce this webscraper,

- Now we have a output in the form of a json file with all of our results an aditional testing file could be created to ensure that for future runs any errors could be more easily traced back using the inbuilt unittest module

- For the testing of this project we would only initilise a few tests, as more would be created as the project progressed, at the moment these tests checked that all dictionary keys existed, that the json file was a list & that inside of that list dictionaries existed


5. Scalably Storing Data

- Images are stored with the cryptocurrencies Symbol as an identifier, originally a method was created that would save the images as a .png file LOCALLY which could be uploaded, however this would create problems in importing to SQL & taking a large amount of time to upload correctly to AWS S3. Instead image data is saved via the images & then appended to our main coins_data.json file. 

- A method was created which could then later seperate this data into a list of the image urls, from here we the urlib import to save the images .jpg associated with the image url. Insteasd of saving the images locally a temporary dictionary was used which was used to transform the image url's to .jpeg & immediateley send the images to the AWS S3 bucket without saving them locally

- All coin information data is uploaded to an AWS S3 bucket stored as json file. this data is then connected to an AWS RDS instance via a Boto3 method combined with turning the json file into a pandas dataframe, from here we can connect to a postgreSQL server to manipulate the data in an SQL format.


6. Getting more data

For this section of the project the main aim was to collect a substantial amount of results & ensure no duplicates:

- To collect more data a method was created which would click the next page button at the bottom of the page until the webscraper had reached page 11 then the same method responsible for swapping pages would terminate the webpage. 

- Each coin from coinmarketcap had a unique ID with the coin name attatched to the end, by extracting this as a string and splitting the string so just the coin name was used as a friendly ID i could store this & adapt my scraping method so that if this name appeared the scraper would not scrape this already known data

- As the image data was also attatched in this loop when the Friendly ID was found it would lso prevent the image data being scraped too


7. Making the scraping scalable

- Now in order to make the data scalable we would have to install our project on a docker image that could be run & an amazon EC2 instance that could also be run.

In order to begin this first preperations would be needed for the project:
- Chromedriver was moved to the same directory as our project
- a Dockerfile was created, this would give docker instructions to read & download requirements, the instructions to download & unzip a google chrome package, update any packages & then to run the correct files
- All results which were stored in local directories had to have filepaths changed from e.g. 'patrick/project/coin_data.json' to './coin_data.json' this in turn would enable docker to find a existing filepath (docker cannot view local filepaths as it is a disconnected system)
- In the initiliser of the webscraper an additional headless arguement is used, this allows our project to run without any GUI (scary)

Creating the Docker image:
- Dockerhub acount was created & docker was downloaded via the CLI, using sudo commands we are able to login to docker & view all current images, as of right now there are none

- Whilst inside the cd which contains the project, dockerfile & requirements we can now use the docker build command to build our image. Here it is good to note that docker will only build the files that are explicitly mentioned within the Dockerfile within the project, & will only install packages containes within the requirements.txt file.

- Another key feature to note is that when building the image the -t (tag) arguement is used to name the docker image, this is important as later on when we attempt to pull the Docker image, we will only be able to pull images that begin with our username i.e. myname/scraperproject.
- Now that the image is built we can log into to our docker account in the CLI & using 'sudo docker run -it myname/scraperproject' can run the webscraper within docker, arguements are places within the initiliser of the scraper to allow for running of the scraper in headless mode.

Running the scraper via EC2:

- Alike running our scraper via docker this involves not running the project locally, in this context we are now running the scraper using an AWS EC2 instance (using AWS virtual servers). 

- In order to do this first we setup a free tier EC2 instance, gain our keypair which must be chmod 400 encrypted. we can then using the CLI paste our instance via its public DNS, which will detect our encrypted keypair & allow access to the instance. from here we can just sudo login to our docker account and alike before, pull our docker image to be run on the ec2 instance 


8. Monitoring and Alerting

Setup Prometheus:
In order to monitor the webscraper via the EC2 instance a container must be created to connect to prometheus. For prometheus to function correctly on MacOSX three different adjustments must be created:

- Using the dockerhub desktop application within the settings/engine we must add an additional arguement which will allow for a metrics ip address to be connected to the image

- A prometheus.yml file must be created in the root directory, this will allow the docker image to connect to prometheus for monitoring

- A prometheus Daemon file is also created which will also allow access to the prometheus monitoring software

- Once created we can run the prometheus container within the docker image using the VERY longwinded command 
'sudo docker run --rm -d \
--network=host \
--name prometheus\
-v root/prometheus.yml:/etc/prometheus/prometheus.yml \
prom/prometheus \
--config.file=/etc/prometheus/prometheus.yml \
--web.enable-lifecycle'

- This will allow for prometheus connections, to finish this we restart the docker image & pasting the ip used to connect prometheus into the search bar can check to see if our EC2 is connected

This prometheus connection is now connected to Grafana (a open source analytics engine), from here a dashboard is created, for my project i had chose to create graphs to monitor:

- Query duration

- Website http response size

- Container action size

- Engine health

9. CI/CD


As learnt previously it takes quite a while to update docker images with code changes, time to streamline this using CI/CD!

- Firstly Github secrets are made, these credentials will mean that whenever we push new changes to github (and so the docker image) we won't have to enter credentials everytime, these secrets are inaccesible to anyone after creation & are stored on the projects repository

- A Github action is created, github provides templates for these actions, a basic one is used this will automate updates to the docker image everytime the repository is updated & push it to dockerhub for usage on the EC2 Instance

- The very final objective of this project is to have the scraper run automatically, for my scraper I used cronjobs within my EC2 instance to have the webscraper run daily at 10am without user input, from this my grafana dashboard can be checked to ensure that the webscraper ran correctly






