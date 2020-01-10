import os
import pandas as pd

#idiot code test for 0% mean and 0% standard deviation for correct answers

# change current directory
path = "/Users/sararodriguez/Desktop"
os.chdir(path)
print(os.getcwd())

os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))

for filename in os.listdir(os.getcwd()):
    # load excel files
    if 'IdiotTest00.xlsx' in filename:

        print(filename)
        data = pd.read_excel(filename, skiprows=3)

        # calculating the mean and standard deviation
        mean1 = data['correct'].mean()
        std1 = data['correct'].std()

        print('Mean of correct answers: ' + str(mean1))
        print('Std of correct answers: ' + str(std1))



#idiot code test for 100% mean and 0% standard deviation for correct answers

# change current directory
path = "/Users/sararodriguez/Desktop"
os.chdir(path)
print(os.getcwd())

os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))

for filename in os.listdir(os.getcwd()):
    # load excel files
    if 'IdiotTest01.xlsx' in filename:

        print(filename)
        data = pd.read_excel(filename, skiprows=3)

        # calculating the mean and standard deviation
        mean1 = data['correct'].mean()
        std1 = data['correct'].std()

        print('Mean of correct answers: ' + str(mean1))
        print('Std of correct answers: ' + str(std1))


#code for 'philadelphia tests results' files

# change current directory
path = "/Users/sararodriguez/Downloads/philadelphia_test 2/control_data"
os.chdir(path)
print(os.getcwd())

os.listdir(os.getcwd())
print(os.listdir(os.getcwd()))

# create loop for all files in subfolder 'control data' from 'philadelphia_test 2' folder
for filename in os.listdir(os.getcwd()):
    # load excel files
    if 'philly_gender_M089887.xlsx' in filename:

        print(filename)
        data = pd.read_excel(filename, skiprows=3)

        # calculating the mean and standard deviation
        mean1 = data['correct'].mean()
        std1 = data['correct'].std()

        print('Mean of correct answers: ' + str(mean1))
        print('Std of correct answers: ' + str(std1))

    # exclude random files when loading csv files
    elif not filename == '.DS_Store':

        print(filename)
        data = pd.read_csv(filename, skiprows=3)

        # calculating the mean and standard deviation
        mean1 = data['correct'].mean()
        std1 = data['correct'].std()

        print('Mean of correct answers: ' + str(mean1))
        print('Std of correct answers: ' + str(std1))