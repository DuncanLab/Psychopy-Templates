from psychopy import data

# TEMPLATE: READING CSV FILES
# Demonstrates how to read CSV files that has multiple columns.

# CSV file that gets read
FILE_NAME = 'sample_csv.csv'

# Class to handle trial sequencing and data storage.
# Gets passed in the CSV file name
trial_handler = data.TrialHandler(nReps=1, method='sequential',
                                  extraInfo=None, trialList=data.importConditions(FILE_NAME),
                                  seed=None, name='')

# Used to show which row is currently being processed
row = 0

# Go through every trial/row in the CSV file
for trial in trial_handler:
    # Print the Row and the 2 Stims (columns 'StimA' and 'StimB')
    print 'Row: %d' % row
    print 'StimA: %s' % trial['StimA']
    print 'StimB: %s' % trial['StimB']

    # Increment the row number
    row += 1
