from psychopy import data, gui, core, event, visual
import time

# TEMPLATE: BASIC EXPERIMENT
# Demonstrates a basic experiment which incorporates counterbalancing, dynamic responses, response tracking, and
# output generation.

# Experiment name
expName = 'my_exp_name'

# Used for prompt pop-up
expInfo = {'participant': '', 'session': '001'}

# Display prompt that asks for participant/session numbers
dlg = gui.DlgFromDict(dictionary=expInfo, title=expName)

# Get the current date (Will get used for output file name)
expInfo['date'] = data.getDateStr()  # add a simple timestamp

# Exit if the user exists the prompt asking for participant/session numbers
if not dlg.OK:
    core.quit()  # user pressed cancel

# Get the filename based on participant number
participant_filename = "participant_files/participant_%s.csv" % expInfo['participant']

# Get the output file name based on participant number and current date/time
output_filename = 'output/participant_%s_%s' % (expInfo['participant'], expInfo['date'])

# Extra information for output file (Add date and participant number to output file)
info = {'date': expInfo['date'], 'participant': expInfo['participant']}

# Experiment Handler for generating a single data file from an experiment when given TrialHandler(s)
# In order to have more than 1 output file, more than 1 ExperimentHandler will need to be created.
# Anything Added to extraInfo variable will be included in output as a column.
thisExp = data.ExperimentHandler(name=expName, version='',
                                 extraInfo=info, runtimeInfo=None,
                                 savePickle=True, saveWideText=True,
                                 dataFileName=output_filename)

# Class to handle trial sequencing and data storage.
# Anything Added to extraInfo variable will be included in output as a column.
trial_handler = data.TrialHandler(nReps=1, method='sequential',
                                  extraInfo=None, trialList=data.importConditions(participant_filename),
                                  seed=None, name='')

# Add the trial handler to the ExperimentHandler
# Adding the trial handler will add all the columns from the read CSV into the output CSV
thisExp.addLoop(trial_handler)

# Screen window
win = visual.Window(size=(1920, 1080), fullscr=True, screen=0, allowGUI=False,
                    allowStencil=False, monitor='testMonitor', color=[0, 0, 0], colorSpace='rgb', blendMode='avg',
                    useFBO=True)

full_image = visual.ImageStim(win=win, size=2, pos=[0, 0])

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

keyboard_empty = visual.ImageStim(win=win, name='keyboard_empty', image='images/keyboard_empty.png', pos=[0, -0.7],
                                  size=0.3)

keyboard_a = visual.ImageStim(win=win, name='keyboard_a', image='images/keyboard_a.png', pos=[0, -0.7],
                              size=0.3)

keyboard_s = visual.ImageStim(win=win, name='keyboard_s', image='images/keyboard_s.png', pos=[0, -0.7],
                              size=0.3)

instructions_list = ['instr_1.png', 'instr_2.png', 'instr_3.png', 'instr_4.png']

for instruction in instructions_list:
    full_image.setImage('images/%s' % instruction)
    full_image.draw()
    win.flip()
    while True:
        time.sleep(1)  # Reduces amount of resources used
        if event.getKeys(keyList=['escape', 'esc']):
            core.quit()
        elif event.getKeys(keyList=['space']):
            break

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
    keyboard_empty.draw()
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
        elif event.getKeys(keyList=['A', 'a']):
            response_time = response_timer.getTime()
            keyboard_a.draw()
            response = 'a'
            break

        # Stim B is pressed
        elif event.getKeys(keyList=['s', 'S']):
            response_time = response_timer.getTime()
            keyboard_s.draw()
            response = 's'
            break

    # Redraw the two stim to display updated colours and pause for 1 seconds before removing text.
    stimA.draw()
    stimB.draw()
    win.flip()
    time.sleep(1)

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
