#Minecraft-Scrape

Such an ugly name for the python script, but didnt have anything else in mind at the time of writing it. Maybe one day I'll come up with something better.

##About

The purpose of this script is to grab the amount of users that had purchased minecraft off of the website and then using this number create other data that can be used. The script is hosted on a virtual private server and ran once a day whenever the clock strikes midnight. The reason for running the task at midnight is to collect accurate data about the people purchasing Minecraft per 24 hours.

##Dependencies
- lxml (pip install lxml <- in command line)
  - Used to parse Minecrafts html file

- requests (pip install requests <- in command line)
  - Used to pull the website and stores it as a string

##Future implementations
- Optimised code (So far very sloppy and crowded with comments)

##Known issues
- Large Growth rate upon first log entry