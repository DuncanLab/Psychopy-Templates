from psychopy import data, core, visual, event
import time

# TEMPLATE: RESPONSE TRACKING AND OUTPUT GENERATION
# Demonstrates how to track user response and response time and create an output file with the data.

# Name of CSV file that will get read.
FILE_NAME = 'sample_csv.csv'

OUTPUT_FILE_NAME = 'output_csv'

# Experiment Handler for generating a single data file from an experiment when given TrialHandler(s)
# In order to have more than 1 output file, more than 1 ExperimentHandler will need to be created.
# Anything Added to extraInfo variable will be included in output as a column.
thisExp = data.ExperimentHandler(name="ExpName", version='',
                                 extraInfo=None, runtimeInfo=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=OUTPUT_FILE_NAME)

# Class to handle trial sequencing and data storage.
# Anything Added to extraInfo variable will be included in output as a column.
trial_handler = data.TrialHandler(nReps=1, method='sequential',
                                  extraInfo=None, trialList=data.importConditions(FILE_NAME),
                                  seed=None, name='')

# Add the trial handler to the ExperimentHandler
# Adding the trial handler will add all the columns from the read CSV into the output CSV
thisExp.addLoop(trial_handler)

# Screen window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False,
                    allowStencil=False, monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb', blendMode='avg',
                    useFBO=True)

stimA = visual.TextStim(win=win, ori=0, name='StimA',
                        text='A',
                        font='Arial',
                        pos=[-0.5, 0], height=0.5, wrapWidth=None,
                        color='white', colorSpace='rgb', opacity=1,
                        depth=0.0)

stimB = visual.TextStim(win=win, ori=0, name='StimB',
                        text='B',
                        font='Arial',
                        pos=[0.5, 0], height=0.5, wrapWidth=None,
                        color='white', colorSpace='rgb', opacity=1,
                        depth=0.0)

# Tracks the time for each trial
response_timer = core.Clock()

# Used to keep track of response time for a trial
response_time = 0

# Used to keep track of response for a trial
response = None

# Go through every trial/row in the CSV file
for trial in trial_handler:

    # Set the visual text based on CSV file row values
    stimA.setText(trial['StimA'])
    stimB.setText(trial['StimB'])

    # Draw text on screen
    stimA.draw()
    stimB.draw()
    win.flip()

    # Reset response timer to start counting from 0
    response_timer.reset()

    # Clear all pressed keys before starting next trial
    # This is used just in case user pressed a key in between trials
    event.clearEvents()

    # Keep displaying text until response (escape, 1 or 0)
    while True:

        # Sleep for 100 ms during each iteration to reduce amount of CPU usage
        time.sleep(0.1)

        # Exit if escape is pressed
        if event.getKeys(keyList=['esc', 'escape']):
            core.quit()

        # Stim A is pressed
        elif event.getKeys(keyList=['1']):
            response_time = response_timer.getTime()
            response = '1'
            break

        # Stim B is pressed
        elif event.getKeys(keyList=['0']):
            response_time = response_timer.getTime()
            response = '0'
            break

    # Remove text and pause for 0.5 seconds before moving to next trial
    win.flip()
    time.sleep(0.5)

    # Add the response and response time to the ExperimentHandler which will add it to the output file for the
    # given trial.
    thisExp.addData('my_response', response)
    thisExp.addData('my_response_time', response_time)

    # Inform the ExperimentHandler that you are moving on to the next trial
    # This is required for the output file generation
    thisExp.nextEntry()
