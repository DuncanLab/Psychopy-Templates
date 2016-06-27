from psychopy import data, core, gui

# TEMPLATE: COUNTERBALANCING
# Demonstrates Picks trial sequence based on participant number passed in. Participant number must be between 0-9.
#   Sequence will be fetched from one of the text files in the participant_files folder.

# Experiment name
expName = 'counterbalancing_example'

# Used for prompt pop-up
expInfo = {'participant': '', 'session': '001'}

# Display prompt that asks for participant/session numbers
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

# Get the current date (Will get used for output file name)
expInfo['date'] = data.getDateStr()  # add a simple timestamp

# Exit if the user exists the prompt asking for participant/session numbers
if not dlg.OK:
    core.quit()  # user pressed cancel

# Participant filename can be found inside the 'participant_files' folder.
# All CSV files start with 'sample_csv_' followed by a number. That number will be the participant number
# Using the inputted participant number, get the appropriate participant file.
participant_filename = 'participant_files/sample_csv_%s.csv' % expInfo['participant']

# Class to handle trial sequencing and data storage.
trial_handler = data.TrialHandler(nReps=1, method='sequential',
                                  extraInfo=None, trialList=data.importConditions(participant_filename),
                                  seed=None, name='')

# Used to show which row is currently being processed
row = 0

# Go through every trial/row in the CSV file for the inputted participant number
for trial in trial_handler:
    # Print the Row and the 2 Stims (columns 'StimA' and 'StimB')
    print 'Row: %d' % row
    print 'StimA: %s' % trial['StimA']
    print 'StimB: %s' % trial['StimB']

    # Increment the row number
    row += 1
