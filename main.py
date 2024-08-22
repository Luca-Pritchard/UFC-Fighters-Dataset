
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----setting up original dataframe and updated dataframe with an additional column (win rate) to be used later in my data analysis in things such as stance, weight and height win rates.----#
original_df = pd.read_csv('ufc-fighters-statistics.csv')

ufcstats_df = pd.read_csv('ufc-fighters-statistics.csv')
ufcstats_df['win rate'] = ufcstats_df['wins'] / (ufcstats_df['wins'] + ufcstats_df['losses'] + ufcstats_df['draws']) * 100

#----All my functions getting defined----#
#-Shows the original dataset to the user-#
def showOriginalData():
    print(original_df)
#-Shows the updated dataset to the user with the additional column-#
def showUpdatedData():
    print(ufcstats_df)
#-Matches each fighters weight to one of the UFC's standardised weight classes which they fight under so I can find the average winrates for different weights-#
def assign_weight_class(weight_in_kg):
    if weight_in_kg <= 56.7:
        return "Flyweight"
    elif weight_in_kg <= 61.2:
        return "Bantamweight"
    elif weight_in_kg <= 65.8:
        return "Featherweight"
    elif weight_in_kg <= 70.3:
        return "Lightweight"
    elif weight_in_kg <= 77.1:
        return "Welterweight"
    elif weight_in_kg <= 83.9:
        return "Middleweight"
    elif weight_in_kg <= 93.0:
        return "Light Heavyweight"
    else:
        return "Heavyweight"

#-creates the variable: weight class so it can be projected onto the matplotlib graph which is also made in the form of a bar graph for users to see which weight performs the best-#
def WeightWinrates():
    
    ufcstats_df['weight_class'] = ufcstats_df['weight_in_kg'].apply(assign_weight_class)
    W_avg_winrates = ufcstats_df.groupby('weight_class')['win rate'].mean()
    
    # Plot the average win rates
    W_avg_winrates.plot(
                    kind='bar',
                    color='red',
                    alpha=0.3,
                    title='Average Win Rates by Weight Class')
    plt.ylabel('Average Win Rate')
    plt.show()

#-Matches each fighters Height to a height range of 10cm so I can find the average winrates for each of these different height classes-#
def assign_height_class(height_cm):
    if height_cm <= 160:
        return "160cm or less"
    elif height_cm <= 170:
        return "170-179cm"
    elif height_cm <= 180:
        return "180-189cm"
    elif height_cm <= 190:
        return "190-199cm"
    elif height_cm <= 200:
        return "200-209cm"
    elif height_cm <= 210:
        return "210-219cm"
    elif height_cm >= 220:
        return "220cm or over"

#-adds the "height_class" variable and then graphs it and the fighters winrate onto a matplotlib chart.-#
def HeightWinrates():
    ufcstats_df['height_class'] = ufcstats_df['height_cm'].apply(assign_height_class)

    # Calculate average win rates by height class
    H_avg_winrates = ufcstats_df.groupby('height_class')['win rate'].mean()

    H_avg_winrates.plot(
                    kind ='bar',
                    color='red',
                    alpha=0.3,
                    title='Average Win Rates by Height')
    plt.ylabel('Average Win Rate')
    plt.show()

#-finds the mean win rate of each stance and contains a note detailing how there is less data on fighters stances compared to height & weight-#
def StanceWinrates():
    print('Please note that the data on stances is far more limited than the data on weight, height, win rate, etc.')
    S_avg_winrates = ufcstats_df.groupby('stance')['win rate'].mean()

    S_avg_winrates.plot(
                    kind ='bar',
                    color='red',
                    alpha=0.3,
                    title='Average Win Rates For each stance')
    plt.ylabel('Average Win Rate')
    plt.show()

#-assigns the reach of each figher into a range of 10cm-#
def assign_reach_class(reach_in_cm):
    if reach_in_cm <= 159:
        return "159cm or less"
    elif reach_in_cm <= 160:
        return "160-169cm"
    elif reach_in_cm <= 170:
        return "170-179cm"
    elif reach_in_cm <= 180:
        return "180-189cm"
    elif reach_in_cm <= 190:
        return "190-199cm"
    elif reach_in_cm <= 200:
        return "200-209cm"
    elif reach_in_cm <= 210:
        return "210-219cm"
#-prints a note describing the smaller sample size of each fighters reach in contrast to each fighters weight and win rate. Then it creates the "reach_class" variable and plots it onto the matplotlib chart with the fighters winrates-#
def ReachWinrates():
    print('Please note that the data on reach is far more limited than the data on weight, height, win rate, etc.')

    ufcstats_df['reach_class'] = ufcstats_df['reach_in_cm'].apply(assign_reach_class)

    R_avg_winrates = ufcstats_df.groupby('reach_class')['win rate'].mean()

    R_avg_winrates.plot(
                    kind ='bar',
                    color='red',
                    alpha=0.3,
                    title='Average Win Rates For different reaches')
    plt.ylabel('Average Win Rate')
    plt.show()
#-Basic text based UI showing the user how to access each dataset and the updated information then allows the user to input a number 1-7 to make their choice. It then runs the corresponding function from the users choice or states if the user inputted something wrong and needs to try again-#
def userOptions():
    global quit

    print("""Welcome to the UFC Fighter Metrics. You can visualise how different attributes affect fighters winrates by choosing one of the options below. 
          
    Please select one of these:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the average winrate of each weight class
    4 - Visualise the average winrate of different heights
    5 - Visualise the average winrate for different stances
    6 - Visualise the average winrate for differnt reaches
    7 - Quit 
        """)
    
    try:
        choice = int(input('Enter Selection: '))

        if choice == 1:
            showOriginalData()
        elif choice == 2:
            showUpdatedData()
        elif choice == 3:
            WeightWinrates()
        elif choice == 4:
            HeightWinrates()
        elif choice == 5:
            StanceWinrates()
        elif choice == 6:
            ReachWinrates()
        elif choice == 7:
            quit = True
        else:
            print('Pick a number, ya gronk.')

    except:
        print('Please enter a number from the options')

   

#----Main program, just says to run the user options function until the user chooses the 7th function, quit----#
while not quit:
    userOptions()