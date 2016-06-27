from psychopy import data, core, visual, event
import time

# TEMPLATE: DYNAMIC RESPONSE
# Demonstrates changes to stimuli when a response is given during each trial.

# Name of CSV file that will get read.
FILE_NAME = 'sample_csv.csv'

# Class to handle trial sequencing and data storage.
# Anything Added to extraInfo variable will be included in output as a column.
trial_handler = data.TrialHandler(nReps=1, method='sequential',
                                  extraInfo=None, trialList=data.importConditions(FILE_NAME),
                                  seed=None, name='')

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

keyboard_empty = visual.ImageStim(win=win, name='keyboard_empty', image='images/keyboard_empty.png', pos=[0, -0.7],
                                  size=0.3)

keyboard_a = visual.ImageStim(win=win, name='keyboard_a', image='images/keyboard_a.png', pos=[0, -0.7],
                              size=0.3)

keyboard_s = visual.ImageStim(win=win, name='keyboard_s', image='images/keyboard_s.png', pos=[0, -0.7],
                              size=0.3)

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

    # Clear all pressed keys before starting next trial
    # This is used just in case user pressed a key in between trials
    event.clearEvents()

    # Keep displaying text until response (escape, 1 or 0)
    while True:
        time.sleep(0.1)

        # Exit if Escape is pressed
        if event.getKeys(keyList=['esc', 'escape']):
            core.quit()

        # Stim A is pressed
        elif event.getKeys(keyList=['a', 'A']):
            # If stim A is selected, change colour of text to red
            keyboard_a.draw()
            break

        # Stim B is pressed
        elif event.getKeys(keyList=['s', 'S']):
            # If stim B is selected, change colour of text to red
            keyboard_s.draw()
            break

    stimA.draw()
    stimB.draw()
    win.flip()
    time.sleep(1)

    # Remove text and pause for 0.5 seconds before moving to next trial
    win.flip()
    time.sleep(0.5)
