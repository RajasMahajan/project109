import statistics 
import pandas as pd
import csv

data = pd.read_csv('data.csv')

dataonemale = data['male'].tolist()
dataonefemale = data['female'].tolist()

maleonemean = statistics.mean(dataonemale)
femaleonemean = statistics.mean(dataonefemale)

maleonemedian= statistics.median(dataonemale)
femaleonemedian = statistics.median(dataonefemale)

maleonemode = statistics.mode(dataonemale)
femaleonemode = statistics.mode(dataonefemale)

malestdev = statistics.stdev(dataonemale)
femalestdev = statistics.stdev(dataonefemale)

malefirststart,malefirstend = maleonemean - malestdev, maleonemean + malestdev
malesecondstart,malesecondend = maleonemean - (2*malestdev), maleonemean + (2*malestdev)
malethirdstart,malethirdend = maleonemean - (3*malestdev), maleonemean + (3*malestdev)


femalefirststart,femalefirstend = femaleonemean - femalestdev,femaleonemean + femaleonemean
femalesecondstart,femalesecondend = femaleonemean - (2*femalestdev), femalestdev + (2*femalestdev)
femalethirdstart,femalethirdend = femaleonemean - (3*femalestdev), femalestdev + (3*femalestdev)

male_within_firstdev = [result for result in maleonemean if result > malefirststart and result < malefirstend]
male_within_seconddev = [result for result in maleonemean if result > malefirststart and result < malefirstend]
male_within_thirddev = [result for result in maleonemean if result > malefirststart and result < malefirstend]

female_within_firstdev = [result for result in femalestdev if result > femalefirststart and result < femalefirstend]
female_within_seconddev = [result for result in femalestdev if result > femalefirststart and result < femalefirstend]
female_within_thirddev = [result for result in femalestdev if result > femalefirststart and result < femalefirstend]


print(male_within_firstdev,male_within_seconddev,male_within_thirddev)
print(female_within_firstdev,female_within_seconddev,female_within_thirddev)
