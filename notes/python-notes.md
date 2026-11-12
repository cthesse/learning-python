11/5/2026
    Downloaded Python, GIT, VS Code
    Created a learning-python repository, linked to VS Code via Git:Clone. From there, set up folders and files
    Take Aways
        What did I do?
            Cloned a github repository using github URL
            Created a Virtual Environment (.venv) using "python -m venv .venv" by opening a new Terminal within the learning-python folder. Private, will not be uploaded to github.
            Instructed VS Code to use the Virtual Environment (Ctrl+Shift+P, Python:Select Interpreter). .venv is active when it is seen at the beginning of the Terminal line.
        Why did I do this?
            Virtual Environments exist to ensure that libraries do not conflict with one another. Without Virtual Environments, two projects sharing a set of Python libraries could conflict. It is good housekeeping to create a Virtual Environment for each project so that an update to one library to meet the needs of one porject does not break the other Project.
    write -> run -> commit -> sync loop
        Write code/add to notes
        Run/Save
        Source Control
        Enter commit msg, and save. Then Sync.

11/10/2026
    Signed up for free API key with EIA and downloaded requests and python=dotenv to talk to websites and APIs and load secrets from a file

max(rows, key=lambda row:rows['values'])
    Identify the row with the largest value in a given column, in this case 'values'. 

Compared Demand to Demand Forecast
    After assigning D, DF 'type' to their respective lists, had to come up with a way to compare the Demand to Forecasted Demand based on period (day, hour). Inital instinct was to start with each Demand row, find its period value, and then loop through every Forecast row until the matching period value was found. Because Forecast list is looped through every time for each Demand period value, this is an inefficienct process. Rather, the following solution is preferable: Create a dictionary based off of Demand Period that assigns a ["period", "value"].
    Findings: On average, Demand was greater than forecast by 285 MW Hours (underforecasting for this time period). In the industry, this is the opposite of conservative. Conservative forecasting would mean that the forecasting is on average GREATER than the demand because more backup generation is available -> the forecast slightly underestimated demand.
    Python Dictionary/List takeaways:
        [] is a list, accessed by position.
        {} is a dictionary, accessed by a key (matching name)
            my_dict[key] = value adds one entry
            my_dict = {} replaces the whole dictionary
        WHEN CONFUSED ABOUT SHAPE use print(len(my_dict))
        API data is usually a list of dictionaries. Each hour is a dictionary, and the hours are sotred as a list

11/11/2026
    Used pandas/Keith Galli video to answer the following:
    Which hour of the day had highest demand per week?
    Which hour had peak demand during the week?
    How does a weekday to the weekend?
    Some useful commands:
        pd.to_datetime()
        .groupby(df['key_to_index'])['which_column_looking_at'].mean()
        .idxmax() = returns cell in index column with highest value of another column (max tells you highest value, idxmax tells you where highest value)
