# <i>CSE-327-Software-Engineering-RE-SEARCH-Cluster-Based-Search-Engine
RE-SEARCH is a cluster based search engine that makes searching more easier and saves valuable time.

<p align="center">
   NORTH SOUTH UNIVERSITY<br>
   Department of Electrical and Computer Engineering
<p>
<p align="center">
  <img src="https://user-images.githubusercontent.com/63312173/169691760-a83acee4-4afd-424a-a34a-986a9d5e06c6.png">
</p>
<p align="center">
   CSE 327 | CSE 299 L<br>
   Software Engineering | Junior Design <br>
   Project Title: RE-SEARCH [Cluster Based Search Engine]<br>
 <p>
 
 # Introduction
In this data-driven technological era, there is an abundance of data readily accessible to all with the help of search engines. However, users, especially researchers and such may face hurdle to get specific results for their need with the overwhelming amount of data available. This is where RE-SEARCH, a cluster-based search application comes in to play as its main purpose is to let its users to search in their custom-made clusters of links with the type of files the users are looking for. Re-search is designed to make searching very specific for its users. Users will be able to set their own clusters of links and will be able to define search methods based on textual file types such as: pdf, txt, doc etc. Users then will be able to search for keywords within the clusters to get intended results. The software serves to make researching easier for its users as other conventional search engines can often provide overwhelming number of results or data that can make the research very cumbersome.

# Aims & Goals
1. User friendly interface on the frontend which would boost up RE-SEARCH and make searching easier and faster.<br>
2. The users are in charge here, and set their own parameters and search for their desired content. No redundant results which might waste the user’s time.<br>
3. One of the primary goals of our project is to provide a safe, secured search experience. We do not use or make profit by selling any of the user’s data secretively or deceptively, and only require just their e-mail IDs and a password to register or to login via their other social accounts.<br>
4. RE-SEARCH makes searching accurate and easy for its users with no strings attached. Users can find whatever they are looking for with ease and its even enjoyable to use.<br>
<br><i>The web application RE-SEARCH would also aim to fulfill other quality attributes such as:</i><br>
   <b>Availability:</b> This software will be available to use at all times for its users as the data would be indexed in a 3rd party service, Elasticsearch and would also provide search functionalities. Temporary unavailability may happen for scheduled maintenance.<br>
   <b>Correctness:</b> This software will provide accurate results based on the links the users provide in clusters and the keywords they will use when they need to search.<br>
   <b>Reusability:</b> The users will be able to reuse and search many times on the clusters that they create.<br>
    
# Tools needed
<b>Programming/Markup Languages:</b> Django (Python framework for the backend), HTML, CSS, and JavaScript (for the frontend)
Django was the framework that glued everything together in the project. Django was used to created models which are tables in the database. Django views were made used of to render http requests from the frontend. Django Rest Framework was used to build the APIs. HTML and CSS were the main two technologies that were used to build the frontend. Javascript was used to implement voice searching functionality.<br>

<b>Libraries (Python):</b> Textract (For extracting data), Django-allauth (For user authentication),
Beautifulsoup (for scraping and crawling) and Powerful Python libraries like Beautifulsoup, Textract will be used to build our crawler which will crawl the links based on the inputs and the input parameters the users set.<br>

<b>Database:</b> Sqlite3 Django’s default Sqlite3 database is used in the project to store relevant data/models.<br>
<b>Search Engine:</b> Elasticsearch. Elasticsearch is the core of the project. It was used to provide searching functionalities inside the clusters. Elasticsearch was also used to store the scraped content in Elasticsearch indexes.
    
<b>External APIs/Services:</b> Paypal API, Gmail API. Paypal API helped facilitating donation options to support the developers of this project. Gmail API
was used to enable easy social login feature for the users to use this app.<br>

<b>IDE/Text Editor:</b> Visual Studio Code VS Code was the only code editor that was used in the development of this project    

# Use Case Diagram
<p align="center">
  <img height=500 width=450 src="https://user-images.githubusercontent.com/63312173/169749428-d1a91fe6-e081-41ab-ade2-afa415094a18.png">
</p>

# Web Application View
All of the authentications: social login, login, sign-up, sign out, resetting passwords, adding secondary emails, verifying e-mail IDs were handled using Django Allauth. The corresponding html files were designed and implemented according with the help of relevant tools. The following is a snapshot of the UI of the login
page and registration.
<p align="center">
  <img height=450 width=1000 src="https://user-images.githubusercontent.com/63312173/169750128-4630c101-559d-4c50-8402-9e5a8f4ca2af.PNG">
</p>
After a user successfully has logged in to the system, whether by logging in or registering for the first time, the user is able to successfully create “search clusters” with a title and the description for a particular cluster initially. Then the user can create more clusters if they want to. 
<p align="center">
  <img height=450 width=1000 src="https://user-images.githubusercontent.com/63312173/169750441-ef46fd17-87af-4f87-abfe-159f0aee5886.PNG">
</p>
The cluster view page is successfully created with relevant views and html files. There are other options such as search, view, edit, delete are kept on the UI, and they both successfully render those requests with the help of the relevant views and corresponding html pages. The cluster view page has pagination support, and will have multiple pages of clusters if the total amount of clusters exceeds for a particular page. The saved clusters will be stored into the database for particular users in the form of Cluster table, which was a model as we have implemented.
<p align="center">
  <img height=450 width=1000 src="https://user-images.githubusercontent.com/63312173/169750776-8f7c8dec-3065-4878-a2e9-5d73a5b04562.PNG">
</p>
The user will be able to add a URL, define the depth of crawl, and the type of data they would like to scrape/crawl. This option is found on the view option for a particular cluster. The URLs and their relevant info are stored in the DB. The scraping triggers upon a set interval after an URL is added. The depth logic, crawling strategies are all defined in the scrape.py file.
<p align="center">
  <img height=450 width=1000 src="https://user-images.githubusercontent.com/63312173/169751127-abe9a03b-f041-4209-ad44-bf4b3e89391a.png">
</p>
Users can now add multiple URLs inside a cluster and set their parameters accordingly. All of the scraped content is saved in individual Elasticsearch indexes for individual clusters.
<p align="center">
  <img height=450 width=1000 src="https://user-images.githubusercontent.com/63312173/169751377-23b236d1-e83c-4439-81ba-883b3d9bc587.PNG">
</p>
After scraped content is successfully stored in an index, users can perform searching inside those indexes for the data they scraped. The search function works perfectly and returns accurate hit links for a search query and the desired content as well. The users will be able to export the obtained search results as a CSV
file. The CSV file will contain the links as of now, but can be easily implemented including or just the content itself by little adjustment. There is voice searching implemented as well inside the clusters, and users shall be able to conveniently just speak at their microphones and perform fast, accurate searching with voice
commands. This was implemented using a simple Javascript function. <br>
As evaluated, all of the main functionalities of the project are working seamlessly. Now, there is an option to donate has also been implemented powered by the Paypal API and the users may donate if they wish to support.
<p align="center">
  <img height=450 width=1000 src="https://user-images.githubusercontent.com/63312173/169751986-e2e4a70c-b70f-4f2b-9ac7-465496e17933.png">
</p>

# Future Work
   <b>Development of API</b>
The development of the necessary APIs is finished. The APIs that are successfully built so far are: RegisterAPI, ClusterAPI, UrlAPI, UserAPI. These APIs would provide for registering users, making clusters, adding URLs even outside of the web app. The APIs will work as a middle man between the default database and other platforms. These would be crucial in future to provide cross-platform support for other operating systems such as Android, and iOS.<br>
   <b>Plans for deployment</b>
The plan is to make this software open for all to use and in order to do that, deployment should be the next step. And as mentioned before, we will provide multi-platform support for Web, Android.
   
# Conclusion
The goal of the project is to build a more user friendly search engine that provides a safer, more secured, and smoother searching experience. That is why RE-SEARCH is designed to make searching very specific for its users. It saves the valuable time for its users. Features like easy to use and attractive user interface, voice searching, wildcard searching, less populated search result and exporting search results make RESEARCH different from other search engines available in web.
<i>
