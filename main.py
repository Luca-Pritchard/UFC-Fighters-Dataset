
#----Modules----#
import pandas as pd
import matplotlib.pyplot as plt

#----Global Variables----#
quit = False

#----Setup dataframe and query it here prior to creating visualisation and UI functions----#
original_df = pd.read_csv('ufc-fighters-statistics.csv')


ufcstats_df = pd.read_csv('ufc-fighters-statistics.csv')
ufcstats_df['win rate'] = ufcstats_df['wins'] / (ufcstats_df['wins'] + ufcstats_df['losses'] + ufcstats_df['draws'])


#----Define Functions Below----#
def showOriginalData():
    print(original_df)

def showUpdatedData():
    print(ufcstats_df)

def WeightWinrates():
    ufcstats_df.plot(
                    kind='bar',
                    x='name',
                    y='win rate',
                    color='red',
                    alpha=0.3,
                    title='Weight winrates')
    plt.show()

def userOptions():
    global quit

    print("""Welcome to the Goofy UFC dataset. What attributes do you want to take a look at?
          
    Please select an option:
    1 - Show the original dataset
    2 - Show the updated Data Frame
    3 - Visualise the average winrate of each weight class
    4 - Quit Program
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
            quit = True
        else:
            print('Pick a number, ya gronk.')

    except:
        print('Because you didnt enter a number from the options, Heres an essay about orangutans: Orangutans: Guardians of the Rainforest Orangutans, also known as “persons of the forest,” are remarkable Asian great apes found in the lush rainforests of Southeast Asia. Lets delve into their fascinating world and explore their unique characteristics, habitat, and conservation challenges.1. Species and Habitat Bornean Orangutan (Pongo pygmaeus) Inhabits large portions of Borneo. Known for their distinctive cheek pads in older males. Typically twice the size of females, with a height of up to 1.3 meters (4.3 feet) and a weight of 130 kg (285 pounds).Coarse red hair covers their dark tan or brownish skin.Sumatran Orangutan (Pongo abelii)Limited to northern Sumatra. Shares cognitive abilities with gorillas and chimpanzees.Largest arboreal animals, spending over 90% of their waking hours in trees.Ripe-fruit eaters but consume a variety of foods, including invertebrates and occasional meat. Tapanuli Orangutan (Pongo tapanuliensis)Also found in northern Sumatra.Recently discovered and critically endangered.Distinctive features include a unique call and genetic differences.2. Threats and Conservation Habitat DestructionDeforestation due to logging, agriculture, and palm oil plantations threatens their rainforest homes.As trees disappear, orangutans lose both shelter and food sources.Illegal Wildlife TradeOrangutans are hunted and captured for the exotic pet trade. Their young are often separated from their mothers, causing immense distress. Climate ChangeAltered weather patterns affect fruit availability, impacting their diet.Rising temperatures and changing ecosystems pose additional challenges.3. The Guardians of BiodiversitySeed Dispersers Orangutans play a crucial role in rainforest ecology.They disperse seeds as they move through the canopy, aiding plant growth.Conservation EffortsOrganizations like the Orangutan Foundation International work tirelessly to protect orangutans.Reforestation, anti-poaching efforts, and education are vital components of conservation. In conclusion, orangutans are not just charismatic creatures; they are essential guardians of the rainforest. By understanding their plight and supporting conservation initiatives, we can ensure their survival and preserve the rich biodiversity of our planet. Remember, our actions today impact their future. Lets stand together as stewards of the forest and protect these remarkable beings!')

   

#----Main program----#
while not quit:
    userOptions()