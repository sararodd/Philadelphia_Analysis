import os
import pandas as pd

#change current directory
path = "/Users/sararodriguez/Downloads/philadelphia_test 2/control_data"
os.chdir(path)
print(os.getcwd())

os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))

for filename in os.listdir(os.getcwd()):
    #load csv file using relative path
    if 'philly_gender_M089887.xlsx' in filename:
        print("made it here")
        dataA = pd.read_excel(filename, skiprows=3)
        mean1 = dataA['correct'].mean()
        std1 = dataA['correct'].std()

        print('Mean of correct answers: ' + str(mean1))
        print('Std of correct answers: ' + str(std1))

    elif not filename == '.DS_Store':

        print(filename)
        dataA = pd.read_csv(filename, skiprows = 3)


    #names the columns
    #column_names = ['rowNo', 'type', 'trialNo', 'stim1', 'key', 'ITI', 'presTime', 'stimFormat', 'trialText', 'keyboard',
     #           'random', 'ITI_real', 'presTime_real', 'timestamp', 'response', 'RT', 'correct']
    #names = column_names

    #calculating the mean, standard deviation, etc...
        mean1 = dataA['correct'].mean()
        std1 = dataA['correct'].std()

        print('Mean of correct answers: ' + str(mean1))
        print('Std of correct answers: ' + str(std1))