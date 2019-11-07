----------------------------------------------
## Mission to Mars!
----------------------------------------------
#### Description:

In this project we utilized various frameworks to achieve a customized homepage front that populates with most recent data that's pulled from various sources.

* #### FrameWorks Utilized:
     * Python
     * Flask
     * Mongo DB
     * Beauitful Soup
     * Selenium
     * HTML

First, we went developed our Web Scraper scripts through the utilization of Beautiful Soup to target and store specfic data into lists/dictionaries.

After this step, we then transposed the specific data into a python file, which would run when initiated by user input from the homepage.  This was named "scrape_mars.py".

We then developed our flask server and utilized the render templates framework to have a an interactive webpage front that the user can initate our webscraper script.  Each time the user would initiate the "scrape new data" it would capture all specfied data and load the variables into our mars database in MongoDB.

After the data extraction, flask would then render the information from MongoDB onto our index.html providing the user with an updated Mars Fact Page.

Posted Below are some of the screenshots of the final project:

![Screenshot1](/images/image1.png)
---------------------------------------------------------

![Screenshot2](/images/image2.png)


