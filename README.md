# MMM-Hive #
A MagicMirror Module Compatible with H.I.V.E

## Step 1 Configuration and Setup: ##

First enter your MagicMirror Directory:  
- ``` cd ~/Desktop/MagicMirror ```  


First clone the repository with the following command:

- ``` git clone https://github.com/NateBrownProjects/MMM-Hive.git```\

Then enter the directory using the following command:
- ``` cd MMM-Hive```


If your MagicMirror folder is inside of your Documents folder, then change the following lines in ``` hive.sh``` from:
- ``` cd ~/Documents/MagicMirror/ ```


To:
- ``` cd ~/Desktop/MagicMirror/ ```

## Step 2: ##

Install all dependencies:
- ``` cd MMM-Hive```
- ``` sh setup.sh ```


## IMPORTANT!! ##
If you already have a ```.sh``` file for your MagicMirror that automates through crontab, then please just copy the lines of code from ```hive.sh``` to your MagicMirror ```.sh``` file.

### If you dont have one, please follow the steps below: ###
#### Step 1: ####
Type the following commands
``` crontab -e```
Then add in the following command:  

``` 0 9 * * * ~/Desktop/MMM-Hive/hive.sh ```
and:  

``` 0 21 * * * ~/Desktop/MMM-Hive/hiveoff.sh ```

These 2 commands will run H.I.V.E at 9:00AM every day and will turn on your display at 9:00AM and turn off your display and stop at 9:00PM. For more infomation about crontab, please click the link below.
https://help.dreamhost.com/hc/en-us/articles/215767047-Creating-a-custom-Cron-Job

