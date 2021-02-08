# Predicting Potential Yellow Jackets

### Project for Hacklytics 2021

#### Authors: Saurabh Joshi, Natasha Suska, Richard Sharrott, Sam Lim.

Download the following packages
```
1. pip install streamlit
2. pip install altair
3. pip install numpy, pandas, seaborn, matplotlib
4. pip install plotly
```
## ***Inspiration:***
The shift in the focus of student athlete recruitment from a performance-basis to a character-basis for a cultural fit led to a question of leveraging social network services feeds in student athlete recruitment. We formulated our problem statement by probability prediction of a prospective student athlete based on athletic performance and Twitter sentiment analysis. 

## ***What it does:***
1. Scrapes the student athlete information from US high school football ranking websites. 

2. Scrapes the student athlete information from GT RamblinWreck Football websites based on website handles. 

3. Stores the data into CSV file, data cleaning / pre-processing for string matching on names

4. Student athlete twitter handles are fed into python library for sentiment analysis

5. Saves all the cleaned data of student athlete performance and sentiment from Twitter account into a CSV file

6. Data visualization of student athletes using Streamlit web app

## ***How we built it:***

Data, specifically for the Georgia Tech Football team, was not available online or provided by the sponsor, and thus we made our own web scraper to collect data of student athletes who are in Georgia Tech and and their corresponding Twitter accounts. Rivals and MaxPreps sites are used to scrape the student athlete data for each year and match with the Georgia Tech football roster. 

We scraped Twitter handles from the roster available in GT RamblinWreck website to process sentiment analysis on current football players before their contract signing dates. This is done by obtaining Twitter developer account, using Tweepy library, and feeding the Twitter statuses onto VADER sentiment NLP library. 

We also cross-matched the roster to Rivals data to gain athletic performance of the current athletes. 

The front-end part is built using Streamlit Web app. For data visualization we have used libraries like Plotly, Altair, seaborn which are python Visualization library. 
<br>
<br>

## ***Challenges we ran into:***

**Challenge #1: Availability of data**

In order to properly estimate an incoming student-athlete to be a good fit for the Georgia Tech football team, we needed a database of student athletes. Because no student athlete data were provided by the sponsor, we created a web-scraper and manually collected athlete data from “Rivals.com” or “MaxPreps.com” per year. Though these two websites provided a good amount of student athlete data, we were only able to find 8 students out of a few thousand students who had the name match, possessed all athletic performance, ratings, and social media accounts. This sparseness of the data leads to class imbalance, which is one of the biggest hurdles in building a predictive model. 

**Challenge #2: Tracking of confirmed SNS accounts**

Out of 82 current student athletes in the football department, only half of them had Twitter accounts. Tracking 41 Twitter accounts and confirming the identity of the student athlete was somewhat simple. However, there was no confirmed social network handles database available for potential student athletes. Simply searching their names on the Twitter developer API was not an option as we might be collecting different people who have the same name. Each player, if they had an account, was checked manually by searching, analyzing the posts, and confirming the basic information. This was more than sentiment analysis if it could be automated for the entire potential student athlete. 
 

## ***Accomplishments that we're proud of:***

• A specific problem statement formulation in a general recruitment recommendation challenge

• Web scraping to collect thousands of student athletes
  a. string matching on name combinations (Charlie = Charles, Jeffrey → Jeff, R.J. = Rj, De’Quaz → De quaz)
  b. Finding twitter handles both manually and automatically through scaping

• Putting together data visualization web app using Streamlit

• Data manipulations on the handles and data collection from Twitter Developer API 

• NLP sentiment analysis on past twitter feeds before the contract signing days

**Aside from technical aspects of the project**

• Not losing ourselves while communicating among the team members that are at most 10 hours apart (aye, do you see our future?)
• Though couldn’t build an innovative / robust model but definitely provided a good foundation leading to futures steps of projects within few hours 
<br>
<br>

## ***What we learned:***
• **As a developer:**

  1. Data scraping from a particular website by finding a desired handle

  2. Making visualization web-app through Streamlit
  
  3. Collecting status data from social media accounts and performing sentiment analysis using NLP

• **As an audience:**

  1. Statistically significant distribution of offense performance statistics

      a. Due to COVID-19 leading to less exercises and less number of games

  2. More usage and activity of Twitter account observed  from the student athletes for its advertisement and branding of themselves
  
      a. A worthy factor that can be taken into account when evaluating for a potential candidate but cannot be the sole predictor in character assessment
  
      b. Other types of accounts such as Instagram, Facebook also need to be considered for more confident results
      <br>
      <br>

## ***What's next for Predicting Potential Yellow Jackets:***
1. Data collection from various sources
Per student athlete, we need following pieces of information to build features of a sample

    a. Basic information (height, weight, location, high school)

    b. Past athletic performance before the recruitment based on the athlete position (QB: passing yards, passing completion rate, number of games played)

    c. Uniform score metric based on the performances due to various positions

    d. Academic performance and evaluation metric from high school 

    e. Confirmed social network services account

    **We would collect the mentioned student athlete samples from the following places:**

    • From Georgia Tech Football department:

    1. Current student athletes (training data with a positive response variable)

    • From web / other student athlete database:
  
    1. Current student athletes (training data with a negative response variable)
  
    2. Prospective student athletes (test data with no response variable) 
   

1. Model training using Extreme gradient boosting (random forest based algorithm)
Using the features collected for each of the student athletes, we can estimate the driving factor in determining Georgia Tech admittance and predict the probability in the admission of prospective student athletes. 

3. Activity tracking based on their likes or retweets and the category of those contents

4. More advanced sentiment analysis by breaking down into more specific emotions other than positive, neutral, and negative
5. Visualization of of a player performance and its position in the distribution of the performance statistics
<br>

## ***Built with:***

• Python

• Visualization Library: Seaborn, Plotly express, Altair
Streamlit for Web UI Dashboard

• Twitter Developer API and VADER sentiment analysis

• Web Scraping using Beautiful-Soup
