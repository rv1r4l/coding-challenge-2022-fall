# ACM Research coding challenge (Fall 2022)

Essentially, my idea was to create a graph that would display the ratings of all companies over time. For example: We would see a change in ratings for companies such as Mercedes and Ford and would be able to compare them. This would be helpful for consumers for help in decision making for purchasing a vehicle in regards to overall rating. This would also be helpful for sellers, because they would be able to sell the right vehicle and obtain insight into which vehicles consumers would rather own. 

The way I was working on designing this challenge is by taking data from the dataset (Year, Make, Consumer Rating) and plotting it into a line graph using matplotlib. More specifically, I would be able to display a line for each company and show their consumer rating over time using the three datapoints mentioned above. I started off by figuring out how to obtain data from a csv file, and a quick google search led me to importing csv. This is a library that makes it very easy to read these types of files. After that, I worked on accessing data and printing it (as a test). My focus then shifted to figuring out how to show all of this data on a graph. For that I used matplotlib. This was very new to me, but I managaed to get a successful line graph to show up. I was successfully able to print, store, and display data from the csv file, but organizing it was another challenge that I had yet to run into. My main issue came when using three data points. I wanted to take the average consumer ratings from each year from each company and display that on my graph. 

Taking the average turned out to be a complicated task. I attempted to solve this issue by using HashMaps, and different algorithms to sort my data into a clean way to display on the graph. I figured out how to isolate the data from each company, but getting to merge the years with the consumer rating averages was complex. I attempted for a decent amount of time, and I have submitted my last edited copy.  

All the sources that I have listed may not be what I used in my final attempt, but what I used to research and try to figure out how to display the data correctly. 


Sources:
https://www.analyticsvidhya.com/blog/2021/08/python-tutorial-working-with-csv-file-for-data-science/
https://towardsdatascience.com/5-quick-and-easy-data-visualizations-in-python-with-code-a2284bae952f
https://stackoverflow.com/questions/22276066/how-to-plot-multiple-functions-on-the-same-figure-in-matplotlib
https://www.geeksforgeeks.org/python-get-unique-values-list/
https://www.digitalocean.com/community/tutorials/average-of-list-in-python
https://www.w3schools.com/python/pandas/pandas_csv.asp
https://swcarpentry.github.io/python-novice-gapminder/09-plotting/

Thank you for reading.
