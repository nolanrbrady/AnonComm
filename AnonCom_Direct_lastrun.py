#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Fri Sep 23 11:37:52 2022
If you publish work using this script the most relevant publication is:

    Peirce J, Gray JR, Simpson S, MacAskill M, Höchenberger R, Sogo H, Kastman E, Lindeløv JK. (2019) 
        PsychoPy2: Experiments in behavior made easy Behav Res 51: 195. 
        https://doi.org/10.3758/s13428-018-01193-y

"""

from psychopy import locale_setup
from psychopy import prefs
from psychopy import sound, gui, visual, core, data, event, logging, clock, colors, layout
from psychopy.constants import (NOT_STARTED, STARTED, PLAYING, PAUSED,
                                STOPPED, FINISHED, PRESSED, RELEASED, FOREVER)

import numpy as np  # whole numpy lib is available, prepend 'np.'
from numpy import (sin, cos, tan, log, log10, pi, average,
                   sqrt, std, deg2rad, rad2deg, linspace, asarray)
from numpy.random import random, randint, normal, shuffle, choice as randchoice
import os  # handy system and path functions
import sys  # to get file system encoding

import psychopy.iohub as io
from psychopy.hardware import keyboard

from pylsl import StreamInfo, StreamOutlet
info = StreamInfo(name="Trigger", type="Markers", channel_count=1, channel_format='int32', source_id="Aurora")
outlet = StreamOutlet(info)



# Ensure that relative paths start from the same directory as this script
_thisDir = os.path.dirname(os.path.abspath(__file__))
os.chdir(_thisDir)
# Store info about the experiment session
psychopyVersion = '2022.1.4'
expName = 'Anon_communication'  # from the Builder filename that created this script
expInfo = {
    'participant': '',
    'session': '001',
}
dlg = gui.DlgFromDict(dictionary=expInfo, sortKeys=False, title=expName)
if dlg.OK == False:
    core.quit()  # user pressed cancel
expInfo['date'] = data.getDateStr()  # add a simple timestamp
expInfo['expName'] = expName
expInfo['psychopyVersion'] = psychopyVersion

# Data file name stem = absolute path + name; later add .psyexp, .csv, .log, etc
filename = _thisDir + os.sep + u'data/%s_%s_%s' % (expInfo['participant'], expName, expInfo['date'])

# An ExperimentHandler isn't essential but helps with data saving
thisExp = data.ExperimentHandler(name=expName, version='',
    extraInfo=expInfo, runtimeInfo=None,
    originPath='/Users/nolanbrady/Desktop/LabResearch/IndependentStudy/AnonComm/AnonCom_Direct_lastrun.py',
    savePickle=True, saveWideText=True,
    dataFileName=filename)
# save a log file for detail verbose info
logFile = logging.LogFile(filename+'.log', level=logging.EXP)
logging.console.setLevel(logging.WARNING)  # this outputs to the screen, not a file

endExpNow = False  # flag for 'escape' or other condition => quit the exp
frameTolerance = 0.001  # how close to onset before 'same' frame

# Start Code - component code to be run after the window creation

# Setup the Window
win = visual.Window(
    size=[1720, 1000], fullscr=False, screen=0, 
    winType='pyglet', allowGUI=True, allowStencil=False,
    monitor='testMonitor', color=[0,0,0], colorSpace='rgb',
    blendMode='avg', useFBO=True, 
    units='height')
# store frame rate of monitor if we can measure it
expInfo['frameRate'] = win.getActualFrameRate()
if expInfo['frameRate'] != None:
    frameDur = 1.0 / round(expInfo['frameRate'])
else:
    frameDur = 1.0 / 60.0  # could not measure, so guess
# Setup ioHub
ioConfig = {}

# Setup iohub keyboard
ioConfig['Keyboard'] = dict(use_keymap='psychopy')

ioSession = '1'
if 'session' in expInfo:
    ioSession = str(expInfo['session'])
ioServer = io.launchHubServer(window=win, **ioConfig)
eyetracker = None

# create a default keyboard (e.g. to check for escape)
defaultKeyboard = keyboard.Keyboard(backend='iohub')

# Initialize components for Routine "load_triggers"
load_triggersClock = core.Clock()

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank you for taking part in our study.\n\nOur goal with this study is to understand the ways in which people communicate a little better. For this experiment you will be talking with another student about the prompts we will give you. Each prompt will last 20 seconds or until you press the space bar. Afterwards you will be given 60 seconds to talk.\nIf you have any questions you are always welcome to ask your proctor.\n\nTo move on please press the "spacebar"',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "survey"
surveyClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Before we start, please fill out the survey by scanning the QR code below.\n\nOnce you have finished please press the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()
image = visual.ImageStim(
    win=win,
    name='image', 
    image='surveyQRcode.png', mask=None, anchor='center',
    ori=0.0, pos=(0, -0.3), size=(0.25, 0.25),
    color=[1,1,1], colorSpace='rgb', opacity=None,
    flipHoriz=False, flipVert=False,
    texRes=128.0, interpolate=True, depth=-2.0)

# Initialize components for Routine "control_intro"
control_introClock = core.Clock()
text_20 = visual.TextStim(win=win, name='text_20',
    text="Before we start the experiment we are going to ask you describe a couple of things. You will have 60 seconds to tell us about prompted item.\n\nIf you finish before the 60 seconds are up early please press spacebar.\n\nOnce you're ready to start please press spacebar.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_7 = keyboard.Keyboard()

# Initialize components for Routine "control_prompt"
control_promptClock = core.Clock()
text_14 = visual.TextStim(win=win, name='text_14',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
sound_6 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_6')
sound_6.setVolume(1.0)
sound_9 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_9')
sound_9.setVolume(1.0)
finish_sound_control_prompt = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='finish_sound_control_prompt')
finish_sound_control_prompt.setVolume(1.0)
key_resp_11 = keyboard.Keyboard()
text_23 = visual.TextStim(win=win, name='text_23',
    text='You can press the spacebar whenever you are ready to start.',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-5.0);

# Initialize components for Routine "discuss_control"
discuss_controlClock = core.Clock()
text_21 = visual.TextStim(win=win, name='text_21',
    text='You have one minute to describe the prompt given.\n\nIf you finish early please press the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
sound_2 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_2')
sound_2.setVolume(1.0)
sound_3 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_3')
sound_3.setVolume(1.0)
finish_sound_control_resp = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='finish_sound_control_resp')
finish_sound_control_resp.setVolume(1.0)
key_resp_12 = keyboard.Keyboard()

# Initialize components for Routine "rest"
restClock = core.Clock()
rest_text = visual.TextStim(win=win, name='rest_text',
    text='Please take a 30 second break before moving to the next question.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
sound_11 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)
sound_12 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_12')
sound_12.setVolume(1.0)
sound_13 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_13')
sound_13.setVolume(1.0)

# Initialize components for Routine "practice_intro"
practice_introClock = core.Clock()
text_19 = visual.TextStim(win=win, name='text_19',
    text="Great! Now that we've done that lets get ready to start the experiment. We are going to start with a practice round so you can get the hang of it. \n\nIf you have any questions please ask them now or after the practice round.\n\nOnce you're ready press spacebar to continue.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_10 = keyboard.Keyboard()

# Initialize components for Routine "practice_prompt"
practice_promptClock = core.Clock()
text_3 = visual.TextStim(win=win, name='text_3',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_6 = visual.TextStim(win=win, name='text_6',
    text="Once you're ready to discuss your answer please press the spacebar.",
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
start_practice_discuss = keyboard.Keyboard()
sound_15 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_15')
sound_15.setVolume(1.0)
sound_16 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_16')
sound_16.setVolume(1.0)
finish_sound_practice_prompt = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='finish_sound_practice_prompt')
finish_sound_practice_prompt.setVolume(1.0)

# Initialize components for Routine "discuss_practice"
discuss_practiceClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='You have one minute to tell each other about your answers.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text="If you've finished speaking with one another you can press spacebar to continue.",
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_3 = keyboard.Keyboard()
sound_4 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_4')
sound_4.setVolume(1.0)
sound_5 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_5')
sound_5.setVolume(1.0)
finish_sound_practice_resp = sound.Sound('A', secs=1, stereo=True, hamming=True,
    name='finish_sound_practice_resp')
finish_sound_practice_resp.setVolume(1.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
rest_text = visual.TextStim(win=win, name='rest_text',
    text='Please take a 30 second break before moving to the next question.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
sound_11 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)
sound_12 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_12')
sound_12.setVolume(1.0)
sound_13 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_13')
sound_13.setVolume(1.0)

# Initialize components for Routine "main_intro"
main_introClock = core.Clock()
main_question = visual.TextStim(win=win, name='main_question',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
end_main_intro = keyboard.Keyboard()

# Initialize components for Routine "main_prompt"
main_promptClock = core.Clock()
text_4 = visual.TextStim(win=win, name='text_4',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_10 = visual.TextStim(win=win, name='text_10',
    text="Once you're ready to discuss your answer please press the spacebar.",
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
start_main_discuss = keyboard.Keyboard()
sound_19 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_19')
sound_19.setVolume(1.0)
sound_20 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_20')
sound_20.setVolume(1.0)
finish_sound_main_prompt = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='finish_sound_main_prompt')
finish_sound_main_prompt.setVolume(1.0)

# Initialize components for Routine "discuss_main"
discuss_mainClock = core.Clock()
text_15 = visual.TextStim(win=win, name='text_15',
    text='You have one minute to tell each other about your answers.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_16 = visual.TextStim(win=win, name='text_16',
    text="If you've finished speaking with one another you can press spacebar to continue.",
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_8 = keyboard.Keyboard()
sound_7 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_7')
sound_7.setVolume(1.0)
sound_8 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_8')
sound_8.setVolume(1.0)
finish_sound_main_resp = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='finish_sound_main_resp')
finish_sound_main_resp.setVolume(1.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
rest_text = visual.TextStim(win=win, name='rest_text',
    text='Please take a 30 second break before moving to the next question.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
sound_11 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)
sound_12 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_12')
sound_12.setVolume(1.0)
sound_13 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_13')
sound_13.setVolume(1.0)

# Initialize components for Routine "inflam_intro"
inflam_introClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text="You're about to start the inflamatory portion of the questions. Please rest for 30 seconds before beginning.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
skip = keyboard.Keyboard()
text_22 = visual.TextStim(win=win, name='text_22',
    text='Press the Spacebar to continue',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);

# Initialize components for Routine "inflam_prompt"
inflam_promptClock = core.Clock()
text_11 = visual.TextStim(win=win, name='text_11',
    text='',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_12 = visual.TextStim(win=win, name='text_12',
    text="Once you're ready to discuss your answer please press the spacebar.",
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()
sound_17 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_17')
sound_17.setVolume(1.0)
sound_18 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_18')
sound_18.setVolume(1.0)
finish_sound_inflam_prompt = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='finish_sound_inflam_prompt')
finish_sound_inflam_prompt.setVolume(1.0)

# Initialize components for Routine "discuss_inflam"
discuss_inflamClock = core.Clock()
text_17 = visual.TextStim(win=win, name='text_17',
    text='You have one minute to tell each other about your answers.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_18 = visual.TextStim(win=win, name='text_18',
    text="If you've finished speaking with one another you can press spacebar to continue.\n",
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_9 = keyboard.Keyboard()
sound_14 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_14')
sound_14.setVolume(1.0)
sound_21 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_21')
sound_21.setVolume(1.0)
finish_sound_inflam_resp = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='finish_sound_inflam_resp')
finish_sound_inflam_resp.setVolume(1.0)

# Initialize components for Routine "rest"
restClock = core.Clock()
rest_text = visual.TextStim(win=win, name='rest_text',
    text='Please take a 30 second break before moving to the next question.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_4 = keyboard.Keyboard()
sound_11 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_11')
sound_11.setVolume(1.0)
sound_12 = sound.Sound('A', secs=0.25, stereo=True, hamming=True,
    name='sound_12')
sound_12.setVolume(1.0)
sound_13 = sound.Sound('A', secs=1.0, stereo=True, hamming=True,
    name='sound_13')
sound_13.setVolume(1.0)

# Initialize components for Routine "fin"
finClock = core.Clock()
text_9 = visual.TextStim(win=win, name='text_9',
    text="You're all done. Thank you for your time!",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);

# Create some handy timers
globalClock = core.Clock()  # to track the time since experiment started
routineTimer = core.CountdownTimer()  # to track time remaining of each (non-slip) routine 

# ------Prepare to start Routine "load_triggers"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
load_triggersComponents = []
for thisComponent in load_triggersComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
load_triggersClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "load_triggers"-------
while continueRoutine:
    # get current time
    t = load_triggersClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=load_triggersClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in load_triggersComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "load_triggers"-------
for thisComponent in load_triggersComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "load_triggers" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "welcome"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_2.keys = []
key_resp_2.rt = []
_key_resp_2_allKeys = []
# keep track of which components have finished
welcomeComponents = [text_2, key_resp_2]
for thisComponent in welcomeComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
welcomeClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "welcome"-------
while continueRoutine:
    # get current time
    t = welcomeClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=welcomeClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_2* updates
    if text_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_2.frameNStart = frameN  # exact frame index
        text_2.tStart = t  # local t and not account for scr refresh
        text_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_2, 'tStartRefresh')  # time at next scr refresh
        text_2.setAutoDraw(True)
    
    # *key_resp_2* updates
    waitOnFlip = False
    if key_resp_2.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_2.frameNStart = frameN  # exact frame index
        key_resp_2.tStart = t  # local t and not account for scr refresh
        key_resp_2.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_2, 'tStartRefresh')  # time at next scr refresh
        key_resp_2.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_2.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_2.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_2.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_2.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_2_allKeys.extend(theseKeys)
        if len(_key_resp_2_allKeys):
            key_resp_2.keys = _key_resp_2_allKeys[-1].name  # just the last key pressed
            key_resp_2.rt = _key_resp_2_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in welcomeComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "welcome"-------
for thisComponent in welcomeComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_2.started', text_2.tStartRefresh)
thisExp.addData('text_2.stopped', text_2.tStopRefresh)
# check responses
if key_resp_2.keys in ['', [], None]:  # No response was made
    key_resp_2.keys = None
thisExp.addData('key_resp_2.keys',key_resp_2.keys)
if key_resp_2.keys != None:  # we had a response
    thisExp.addData('key_resp_2.rt', key_resp_2.rt)
thisExp.addData('key_resp_2.started', key_resp_2.tStartRefresh)
thisExp.addData('key_resp_2.stopped', key_resp_2.tStopRefresh)
thisExp.nextEntry()
# the Routine "welcome" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "survey"-------
continueRoutine = True
# update component parameters for each repeat
key_resp.keys = []
key_resp.rt = []
_key_resp_allKeys = []
# keep track of which components have finished
surveyComponents = [text, key_resp, image]
for thisComponent in surveyComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
surveyClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "survey"-------
while continueRoutine:
    # get current time
    t = surveyClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=surveyClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text* updates
    if text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text.frameNStart = frameN  # exact frame index
        text.tStart = t  # local t and not account for scr refresh
        text.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text, 'tStartRefresh')  # time at next scr refresh
        text.setAutoDraw(True)
    
    # *key_resp* updates
    waitOnFlip = False
    if key_resp.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp.frameNStart = frameN  # exact frame index
        key_resp.tStart = t  # local t and not account for scr refresh
        key_resp.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp, 'tStartRefresh')  # time at next scr refresh
        key_resp.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp.status == STARTED and not waitOnFlip:
        theseKeys = key_resp.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_allKeys.extend(theseKeys)
        if len(_key_resp_allKeys):
            key_resp.keys = _key_resp_allKeys[-1].name  # just the last key pressed
            key_resp.rt = _key_resp_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *image* updates
    if image.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        image.frameNStart = frameN  # exact frame index
        image.tStart = t  # local t and not account for scr refresh
        image.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(image, 'tStartRefresh')  # time at next scr refresh
        image.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in surveyComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "survey"-------
for thisComponent in surveyComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text.started', text.tStartRefresh)
thisExp.addData('text.stopped', text.tStopRefresh)
# check responses
if key_resp.keys in ['', [], None]:  # No response was made
    key_resp.keys = None
thisExp.addData('key_resp.keys',key_resp.keys)
if key_resp.keys != None:  # we had a response
    thisExp.addData('key_resp.rt', key_resp.rt)
thisExp.addData('key_resp.started', key_resp.tStartRefresh)
thisExp.addData('key_resp.stopped', key_resp.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('image.started', image.tStartRefresh)
thisExp.addData('image.stopped', image.tStopRefresh)
# the Routine "survey" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# ------Prepare to start Routine "control_intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
# keep track of which components have finished
control_introComponents = [text_20, key_resp_7]
for thisComponent in control_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
control_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "control_intro"-------
while continueRoutine:
    # get current time
    t = control_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=control_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_20* updates
    if text_20.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_20.frameNStart = frameN  # exact frame index
        text_20.tStart = t  # local t and not account for scr refresh
        text_20.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_20, 'tStartRefresh')  # time at next scr refresh
        text_20.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_7.frameNStart = frameN  # exact frame index
        key_resp_7.tStart = t  # local t and not account for scr refresh
        key_resp_7.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_7, 'tStartRefresh')  # time at next scr refresh
        key_resp_7.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_7.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_7.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_7.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_7.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_7_allKeys.extend(theseKeys)
        if len(_key_resp_7_allKeys):
            key_resp_7.keys = _key_resp_7_allKeys[-1].name  # just the last key pressed
            key_resp_7.rt = _key_resp_7_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in control_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "control_intro"-------
for thisComponent in control_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_20.started', text_20.tStartRefresh)
thisExp.addData('text_20.stopped', text_20.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# the Routine "control_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
trials = data.TrialHandler(nReps=0.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('control_questions.xlsx'),
    seed=None, name='trials')
thisExp.addLoop(trials)  # add the loop to the experiment
thisTrial = trials.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
if thisTrial != None:
    for paramName in thisTrial:
        exec('{} = thisTrial[paramName]'.format(paramName))

for thisTrial in trials:
    currentLoop = trials
    # abbreviate parameter names if possible (e.g. rgb = thisTrial.rgb)
    if thisTrial != None:
        for paramName in thisTrial:
            exec('{} = thisTrial[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "control_prompt"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    text_14.setText(prompt)
    sound_6.setSound('A', secs=0.25, hamming=True)
    sound_6.setVolume(1.0, log=False)
    sound_9.setSound('A', secs=0.25, hamming=True)
    sound_9.setVolume(1.0, log=False)
    finish_sound_control_prompt.setSound('A', secs=1.0, hamming=True)
    finish_sound_control_prompt.setVolume(1.0, log=False)
    key_resp_11.keys = []
    key_resp_11.rt = []
    _key_resp_11_allKeys = []
    # keep track of which components have finished
    control_promptComponents = [text_14, sound_6, sound_9, finish_sound_control_prompt, key_resp_11, text_23]
    for thisComponent in control_promptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    control_promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "control_prompt"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = control_promptClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=control_promptClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_14* updates
        if text_14.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_14.frameNStart = frameN  # exact frame index
            text_14.tStart = t  # local t and not account for scr refresh
            text_14.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
            text_14.setAutoDraw(True)
        if text_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_14.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_14.tStop = t  # not accounting for scr refresh
                text_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_14, 'tStopRefresh')  # time at next scr refresh
                text_14.setAutoDraw(False)
        # start/stop sound_6
        if sound_6.status == NOT_STARTED and tThisFlip >= 17-frameTolerance:
            # keep track of start time/frame for later
            sound_6.frameNStart = frameN  # exact frame index
            sound_6.tStart = t  # local t and not account for scr refresh
            sound_6.tStartRefresh = tThisFlipGlobal  # on global time
            sound_6.play(when=win)  # sync with win flip
        if sound_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_6.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_6.tStop = t  # not accounting for scr refresh
                sound_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_6, 'tStopRefresh')  # time at next scr refresh
                sound_6.stop()
        # start/stop sound_9
        if sound_9.status == NOT_STARTED and tThisFlip >= 18-frameTolerance:
            # keep track of start time/frame for later
            sound_9.frameNStart = frameN  # exact frame index
            sound_9.tStart = t  # local t and not account for scr refresh
            sound_9.tStartRefresh = tThisFlipGlobal  # on global time
            sound_9.play(when=win)  # sync with win flip
        if sound_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_9.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_9.tStop = t  # not accounting for scr refresh
                sound_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_9, 'tStopRefresh')  # time at next scr refresh
                sound_9.stop()
        # start/stop finish_sound_control_prompt
        if finish_sound_control_prompt.status == NOT_STARTED and tThisFlip >= 19-frameTolerance:
            # keep track of start time/frame for later
            finish_sound_control_prompt.frameNStart = frameN  # exact frame index
            finish_sound_control_prompt.tStart = t  # local t and not account for scr refresh
            finish_sound_control_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            finish_sound_control_prompt.play(when=win)  # sync with win flip
        if finish_sound_control_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_sound_control_prompt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                finish_sound_control_prompt.tStop = t  # not accounting for scr refresh
                finish_sound_control_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_sound_control_prompt, 'tStopRefresh')  # time at next scr refresh
                finish_sound_control_prompt.stop()
        
        # *key_resp_11* updates
        waitOnFlip = False
        if key_resp_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_11.frameNStart = frameN  # exact frame index
            key_resp_11.tStart = t  # local t and not account for scr refresh
            key_resp_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_11, 'tStartRefresh')  # time at next scr refresh
            key_resp_11.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_11.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_11.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_11.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_11.tStop = t  # not accounting for scr refresh
                key_resp_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_11, 'tStopRefresh')  # time at next scr refresh
                key_resp_11.status = FINISHED
        if key_resp_11.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_11.getKeys(keyList=['q', 'space'], waitRelease=False)
            _key_resp_11_allKeys.extend(theseKeys)
            if len(_key_resp_11_allKeys):
                key_resp_11.keys = _key_resp_11_allKeys[-1].name  # just the last key pressed
                key_resp_11.rt = _key_resp_11_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # *text_23* updates
        if text_23.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_23.frameNStart = frameN  # exact frame index
            text_23.tStart = t  # local t and not account for scr refresh
            text_23.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_23, 'tStartRefresh')  # time at next scr refresh
            text_23.setAutoDraw(True)
        if text_23.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_23.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_23.tStop = t  # not accounting for scr refresh
                text_23.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_23, 'tStopRefresh')  # time at next scr refresh
                text_23.setAutoDraw(False)
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in control_promptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "control_prompt"-------
    for thisComponent in control_promptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('text_14.started', text_14.tStartRefresh)
    trials.addData('text_14.stopped', text_14.tStopRefresh)
    sound_6.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_6.started', sound_6.tStartRefresh)
    trials.addData('sound_6.stopped', sound_6.tStopRefresh)
    sound_9.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_9.started', sound_9.tStartRefresh)
    trials.addData('sound_9.stopped', sound_9.tStopRefresh)
    finish_sound_control_prompt.stop()  # ensure sound has stopped at end of routine
    trials.addData('finish_sound_control_prompt.started', finish_sound_control_prompt.tStartRefresh)
    trials.addData('finish_sound_control_prompt.stopped', finish_sound_control_prompt.tStopRefresh)
    # check responses
    if key_resp_11.keys in ['', [], None]:  # No response was made
        key_resp_11.keys = None
    trials.addData('key_resp_11.keys',key_resp_11.keys)
    if key_resp_11.keys != None:  # we had a response
        trials.addData('key_resp_11.rt', key_resp_11.rt)
    trials.addData('key_resp_11.started', key_resp_11.tStartRefresh)
    trials.addData('key_resp_11.stopped', key_resp_11.tStopRefresh)
    trials.addData('text_23.started', text_23.tStartRefresh)
    trials.addData('text_23.stopped', text_23.tStopRefresh)
    
    # ------Prepare to start Routine "discuss_control"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    outlet.push_sample(x=[4])
    sound_2.setSound('A', secs=0.25, hamming=True)
    sound_2.setVolume(1.0, log=False)
    sound_3.setSound('A', secs=0.25, hamming=True)
    sound_3.setVolume(1.0, log=False)
    finish_sound_control_resp.setSound('A', secs=1.0, hamming=True)
    finish_sound_control_resp.setVolume(1.0, log=False)
    key_resp_12.keys = []
    key_resp_12.rt = []
    _key_resp_12_allKeys = []
    # keep track of which components have finished
    discuss_controlComponents = [text_21, sound_2, sound_3, finish_sound_control_resp, key_resp_12]
    for thisComponent in discuss_controlComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    discuss_controlClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "discuss_control"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = discuss_controlClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=discuss_controlClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_21* updates
        if text_21.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_21.frameNStart = frameN  # exact frame index
            text_21.tStart = t  # local t and not account for scr refresh
            text_21.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_21, 'tStartRefresh')  # time at next scr refresh
            text_21.setAutoDraw(True)
        if text_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_21.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_21.tStop = t  # not accounting for scr refresh
                text_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_21, 'tStopRefresh')  # time at next scr refresh
                text_21.setAutoDraw(False)
        # start/stop sound_2
        if sound_2.status == NOT_STARTED and tThisFlip >= 57-frameTolerance:
            # keep track of start time/frame for later
            sound_2.frameNStart = frameN  # exact frame index
            sound_2.tStart = t  # local t and not account for scr refresh
            sound_2.tStartRefresh = tThisFlipGlobal  # on global time
            sound_2.play(when=win)  # sync with win flip
        if sound_2.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_2.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_2.tStop = t  # not accounting for scr refresh
                sound_2.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_2, 'tStopRefresh')  # time at next scr refresh
                sound_2.stop()
        # start/stop sound_3
        if sound_3.status == NOT_STARTED and tThisFlip >= 58-frameTolerance:
            # keep track of start time/frame for later
            sound_3.frameNStart = frameN  # exact frame index
            sound_3.tStart = t  # local t and not account for scr refresh
            sound_3.tStartRefresh = tThisFlipGlobal  # on global time
            sound_3.play(when=win)  # sync with win flip
        if sound_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_3.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_3.tStop = t  # not accounting for scr refresh
                sound_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_3, 'tStopRefresh')  # time at next scr refresh
                sound_3.stop()
        # start/stop finish_sound_control_resp
        if finish_sound_control_resp.status == NOT_STARTED and tThisFlip >= 59-frameTolerance:
            # keep track of start time/frame for later
            finish_sound_control_resp.frameNStart = frameN  # exact frame index
            finish_sound_control_resp.tStart = t  # local t and not account for scr refresh
            finish_sound_control_resp.tStartRefresh = tThisFlipGlobal  # on global time
            finish_sound_control_resp.play(when=win)  # sync with win flip
        if finish_sound_control_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_sound_control_resp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                finish_sound_control_resp.tStop = t  # not accounting for scr refresh
                finish_sound_control_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_sound_control_resp, 'tStopRefresh')  # time at next scr refresh
                finish_sound_control_resp.stop()
        
        # *key_resp_12* updates
        waitOnFlip = False
        if key_resp_12.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_12.frameNStart = frameN  # exact frame index
            key_resp_12.tStart = t  # local t and not account for scr refresh
            key_resp_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_12, 'tStartRefresh')  # time at next scr refresh
            key_resp_12.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_12.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_12.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_12.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_12.tStop = t  # not accounting for scr refresh
                key_resp_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_12, 'tStopRefresh')  # time at next scr refresh
                key_resp_12.status = FINISHED
        if key_resp_12.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_12.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_12_allKeys.extend(theseKeys)
            if len(_key_resp_12_allKeys):
                key_resp_12.keys = _key_resp_12_allKeys[-1].name  # just the last key pressed
                key_resp_12.rt = _key_resp_12_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discuss_controlComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discuss_control"-------
    for thisComponent in discuss_controlComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    outlet.push_sample(x=[4])
    trials.addData('text_21.started', text_21.tStartRefresh)
    trials.addData('text_21.stopped', text_21.tStopRefresh)
    sound_2.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_2.started', sound_2.tStartRefresh)
    trials.addData('sound_2.stopped', sound_2.tStopRefresh)
    sound_3.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_3.started', sound_3.tStartRefresh)
    trials.addData('sound_3.stopped', sound_3.tStopRefresh)
    finish_sound_control_resp.stop()  # ensure sound has stopped at end of routine
    trials.addData('finish_sound_control_resp.started', finish_sound_control_resp.tStartRefresh)
    trials.addData('finish_sound_control_resp.stopped', finish_sound_control_resp.tStopRefresh)
    # check responses
    if key_resp_12.keys in ['', [], None]:  # No response was made
        key_resp_12.keys = None
    trials.addData('key_resp_12.keys',key_resp_12.keys)
    if key_resp_12.keys != None:  # we had a response
        trials.addData('key_resp_12.rt', key_resp_12.rt)
    trials.addData('key_resp_12.started', key_resp_12.tStartRefresh)
    trials.addData('key_resp_12.stopped', key_resp_12.tStopRefresh)
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    sound_11.setSound('A', secs=0.25, hamming=True)
    sound_11.setVolume(1.0, log=False)
    sound_12.setSound('A', secs=0.25, hamming=True)
    sound_12.setVolume(1.0, log=False)
    sound_13.setSound('A', secs=1.0, hamming=True)
    sound_13.setVolume(1.0, log=False)
    # keep track of which components have finished
    restComponents = [rest_text, key_resp_4, sound_11, sound_12, sound_13]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_text* updates
        if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text.frameNStart = frameN  # exact frame index
            rest_text.tStart = t  # local t and not account for scr refresh
            rest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
            rest_text.setAutoDraw(True)
        if rest_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_text.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                rest_text.tStop = t  # not accounting for scr refresh
                rest_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
                rest_text.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_11
        if sound_11.status == NOT_STARTED and tThisFlip >= 27-frameTolerance:
            # keep track of start time/frame for later
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.tStart = t  # local t and not account for scr refresh
            sound_11.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11.play(when=win)  # sync with win flip
        if sound_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_11.tStop = t  # not accounting for scr refresh
                sound_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11, 'tStopRefresh')  # time at next scr refresh
                sound_11.stop()
        # start/stop sound_12
        if sound_12.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
            # keep track of start time/frame for later
            sound_12.frameNStart = frameN  # exact frame index
            sound_12.tStart = t  # local t and not account for scr refresh
            sound_12.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12.play(when=win)  # sync with win flip
        if sound_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_12.tStop = t  # not accounting for scr refresh
                sound_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12, 'tStopRefresh')  # time at next scr refresh
                sound_12.stop()
        # start/stop sound_13
        if sound_13.status == NOT_STARTED and tThisFlip >= 29-frameTolerance:
            # keep track of start time/frame for later
            sound_13.frameNStart = frameN  # exact frame index
            sound_13.tStart = t  # local t and not account for scr refresh
            sound_13.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13.play(when=win)  # sync with win flip
        if sound_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_13.tStop = t  # not accounting for scr refresh
                sound_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13, 'tStopRefresh')  # time at next scr refresh
                sound_13.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    trials.addData('rest_text.started', rest_text.tStartRefresh)
    trials.addData('rest_text.stopped', rest_text.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    trials.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        trials.addData('key_resp_4.rt', key_resp_4.rt)
    trials.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    trials.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    sound_11.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_11.started', sound_11.tStartRefresh)
    trials.addData('sound_11.stopped', sound_11.tStopRefresh)
    sound_12.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_12.started', sound_12.tStartRefresh)
    trials.addData('sound_12.stopped', sound_12.tStopRefresh)
    sound_13.stop()  # ensure sound has stopped at end of routine
    trials.addData('sound_13.started', sound_13.tStartRefresh)
    trials.addData('sound_13.stopped', sound_13.tStopRefresh)
    thisExp.nextEntry()
    
# completed 0.0 repeats of 'trials'


# ------Prepare to start Routine "practice_intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_10.keys = []
key_resp_10.rt = []
_key_resp_10_allKeys = []
# keep track of which components have finished
practice_introComponents = [text_19, key_resp_10]
for thisComponent in practice_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
practice_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "practice_intro"-------
while continueRoutine:
    # get current time
    t = practice_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=practice_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_19* updates
    if text_19.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_19.frameNStart = frameN  # exact frame index
        text_19.tStart = t  # local t and not account for scr refresh
        text_19.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_19, 'tStartRefresh')  # time at next scr refresh
        text_19.setAutoDraw(True)
    
    # *key_resp_10* updates
    waitOnFlip = False
    if key_resp_10.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        key_resp_10.frameNStart = frameN  # exact frame index
        key_resp_10.tStart = t  # local t and not account for scr refresh
        key_resp_10.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(key_resp_10, 'tStartRefresh')  # time at next scr refresh
        key_resp_10.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(key_resp_10.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(key_resp_10.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if key_resp_10.status == STARTED and not waitOnFlip:
        theseKeys = key_resp_10.getKeys(keyList=['space'], waitRelease=False)
        _key_resp_10_allKeys.extend(theseKeys)
        if len(_key_resp_10_allKeys):
            key_resp_10.keys = _key_resp_10_allKeys[-1].name  # just the last key pressed
            key_resp_10.rt = _key_resp_10_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in practice_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "practice_intro"-------
for thisComponent in practice_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_19.started', text_19.tStartRefresh)
thisExp.addData('text_19.stopped', text_19.tStopRefresh)
# check responses
if key_resp_10.keys in ['', [], None]:  # No response was made
    key_resp_10.keys = None
thisExp.addData('key_resp_10.keys',key_resp_10.keys)
if key_resp_10.keys != None:  # we had a response
    thisExp.addData('key_resp_10.rt', key_resp_10.rt)
thisExp.addData('key_resp_10.started', key_resp_10.tStartRefresh)
thisExp.addData('key_resp_10.stopped', key_resp_10.tStopRefresh)
thisExp.nextEntry()
# the Routine "practice_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('practice_prompt.xlsx'),
    seed=None, name='practice')
thisExp.addLoop(practice)  # add the loop to the experiment
thisPractice = practice.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
if thisPractice != None:
    for paramName in thisPractice:
        exec('{} = thisPractice[paramName]'.format(paramName))

for thisPractice in practice:
    currentLoop = practice
    # abbreviate parameter names if possible (e.g. rgb = thisPractice.rgb)
    if thisPractice != None:
        for paramName in thisPractice:
            exec('{} = thisPractice[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "practice_prompt"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    text_3.setText(practice_question)
    start_practice_discuss.keys = []
    start_practice_discuss.rt = []
    _start_practice_discuss_allKeys = []
    sound_15.setSound('A', secs=0.25, hamming=True)
    sound_15.setVolume(1.0, log=False)
    sound_16.setSound('A', secs=0.25, hamming=True)
    sound_16.setVolume(1.0, log=False)
    finish_sound_practice_prompt.setSound('A', secs=1.0, hamming=True)
    finish_sound_practice_prompt.setVolume(1.0, log=False)
    # keep track of which components have finished
    practice_promptComponents = [text_3, text_6, start_practice_discuss, sound_15, sound_16, finish_sound_practice_prompt]
    for thisComponent in practice_promptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    practice_promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "practice_prompt"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = practice_promptClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=practice_promptClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_3* updates
        if text_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_3.frameNStart = frameN  # exact frame index
            text_3.tStart = t  # local t and not account for scr refresh
            text_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_3, 'tStartRefresh')  # time at next scr refresh
            text_3.setAutoDraw(True)
        if text_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_3.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_3.tStop = t  # not accounting for scr refresh
                text_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_3, 'tStopRefresh')  # time at next scr refresh
                text_3.setAutoDraw(False)
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        if text_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_6.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_6.tStop = t  # not accounting for scr refresh
                text_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_6, 'tStopRefresh')  # time at next scr refresh
                text_6.setAutoDraw(False)
        
        # *start_practice_discuss* updates
        waitOnFlip = False
        if start_practice_discuss.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_practice_discuss.frameNStart = frameN  # exact frame index
            start_practice_discuss.tStart = t  # local t and not account for scr refresh
            start_practice_discuss.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_practice_discuss, 'tStartRefresh')  # time at next scr refresh
            start_practice_discuss.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(start_practice_discuss.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_practice_discuss.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if start_practice_discuss.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_practice_discuss.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                start_practice_discuss.tStop = t  # not accounting for scr refresh
                start_practice_discuss.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_practice_discuss, 'tStopRefresh')  # time at next scr refresh
                start_practice_discuss.status = FINISHED
        if start_practice_discuss.status == STARTED and not waitOnFlip:
            theseKeys = start_practice_discuss.getKeys(keyList=['q', 'space'], waitRelease=False)
            _start_practice_discuss_allKeys.extend(theseKeys)
            if len(_start_practice_discuss_allKeys):
                start_practice_discuss.keys = _start_practice_discuss_allKeys[-1].name  # just the last key pressed
                start_practice_discuss.rt = _start_practice_discuss_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_15
        if sound_15.status == NOT_STARTED and tThisFlip >= 17-frameTolerance:
            # keep track of start time/frame for later
            sound_15.frameNStart = frameN  # exact frame index
            sound_15.tStart = t  # local t and not account for scr refresh
            sound_15.tStartRefresh = tThisFlipGlobal  # on global time
            sound_15.play(when=win)  # sync with win flip
        if sound_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_15.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_15.tStop = t  # not accounting for scr refresh
                sound_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_15, 'tStopRefresh')  # time at next scr refresh
                sound_15.stop()
        # start/stop sound_16
        if sound_16.status == NOT_STARTED and tThisFlip >= 18-frameTolerance:
            # keep track of start time/frame for later
            sound_16.frameNStart = frameN  # exact frame index
            sound_16.tStart = t  # local t and not account for scr refresh
            sound_16.tStartRefresh = tThisFlipGlobal  # on global time
            sound_16.play(when=win)  # sync with win flip
        if sound_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_16.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_16.tStop = t  # not accounting for scr refresh
                sound_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_16, 'tStopRefresh')  # time at next scr refresh
                sound_16.stop()
        # start/stop finish_sound_practice_prompt
        if finish_sound_practice_prompt.status == NOT_STARTED and tThisFlip >= 19-frameTolerance:
            # keep track of start time/frame for later
            finish_sound_practice_prompt.frameNStart = frameN  # exact frame index
            finish_sound_practice_prompt.tStart = t  # local t and not account for scr refresh
            finish_sound_practice_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            finish_sound_practice_prompt.play(when=win)  # sync with win flip
        if finish_sound_practice_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_sound_practice_prompt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                finish_sound_practice_prompt.tStop = t  # not accounting for scr refresh
                finish_sound_practice_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_sound_practice_prompt, 'tStopRefresh')  # time at next scr refresh
                finish_sound_practice_prompt.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in practice_promptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "practice_prompt"-------
    for thisComponent in practice_promptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('text_3.started', text_3.tStartRefresh)
    practice.addData('text_3.stopped', text_3.tStopRefresh)
    practice.addData('text_6.started', text_6.tStartRefresh)
    practice.addData('text_6.stopped', text_6.tStopRefresh)
    # check responses
    if start_practice_discuss.keys in ['', [], None]:  # No response was made
        start_practice_discuss.keys = None
    practice.addData('start_practice_discuss.keys',start_practice_discuss.keys)
    if start_practice_discuss.keys != None:  # we had a response
        practice.addData('start_practice_discuss.rt', start_practice_discuss.rt)
    practice.addData('start_practice_discuss.started', start_practice_discuss.tStartRefresh)
    practice.addData('start_practice_discuss.stopped', start_practice_discuss.tStopRefresh)
    sound_15.stop()  # ensure sound has stopped at end of routine
    practice.addData('sound_15.started', sound_15.tStartRefresh)
    practice.addData('sound_15.stopped', sound_15.tStopRefresh)
    sound_16.stop()  # ensure sound has stopped at end of routine
    practice.addData('sound_16.started', sound_16.tStartRefresh)
    practice.addData('sound_16.stopped', sound_16.tStopRefresh)
    finish_sound_practice_prompt.stop()  # ensure sound has stopped at end of routine
    practice.addData('finish_sound_practice_prompt.started', finish_sound_practice_prompt.tStartRefresh)
    practice.addData('finish_sound_practice_prompt.stopped', finish_sound_practice_prompt.tStopRefresh)
    
    # ------Prepare to start Routine "discuss_practice"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    outlet.push_sample(x=[1])
    sound_4.setSound('A', secs=0.25, hamming=True)
    sound_4.setVolume(1.0, log=False)
    sound_5.setSound('A', secs=0.25, hamming=True)
    sound_5.setVolume(1.0, log=False)
    finish_sound_practice_resp.setSound('A', secs=1, hamming=True)
    finish_sound_practice_resp.setVolume(1.0, log=False)
    # keep track of which components have finished
    discuss_practiceComponents = [text_7, text_8, key_resp_3, sound_4, sound_5, finish_sound_practice_resp]
    for thisComponent in discuss_practiceComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    discuss_practiceClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "discuss_practice"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = discuss_practiceClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=discuss_practiceClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_7* updates
        if text_7.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_7.frameNStart = frameN  # exact frame index
            text_7.tStart = t  # local t and not account for scr refresh
            text_7.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_7, 'tStartRefresh')  # time at next scr refresh
            text_7.setAutoDraw(True)
        if text_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_7.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # *key_resp_3* updates
        waitOnFlip = False
        if key_resp_3.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_3.frameNStart = frameN  # exact frame index
            key_resp_3.tStart = t  # local t and not account for scr refresh
            key_resp_3.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_3, 'tStartRefresh')  # time at next scr refresh
            key_resp_3.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_3.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_3.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_3.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_3.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_3.tStop = t  # not accounting for scr refresh
                key_resp_3.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_3, 'tStopRefresh')  # time at next scr refresh
                key_resp_3.status = FINISHED
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q','space'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_4
        if sound_4.status == NOT_STARTED and tThisFlip >= 57-frameTolerance:
            # keep track of start time/frame for later
            sound_4.frameNStart = frameN  # exact frame index
            sound_4.tStart = t  # local t and not account for scr refresh
            sound_4.tStartRefresh = tThisFlipGlobal  # on global time
            sound_4.play(when=win)  # sync with win flip
        if sound_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_4.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_4.tStop = t  # not accounting for scr refresh
                sound_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_4, 'tStopRefresh')  # time at next scr refresh
                sound_4.stop()
        # start/stop sound_5
        if sound_5.status == NOT_STARTED and tThisFlip >= 58-frameTolerance:
            # keep track of start time/frame for later
            sound_5.frameNStart = frameN  # exact frame index
            sound_5.tStart = t  # local t and not account for scr refresh
            sound_5.tStartRefresh = tThisFlipGlobal  # on global time
            sound_5.play(when=win)  # sync with win flip
        if sound_5.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_5.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_5.tStop = t  # not accounting for scr refresh
                sound_5.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_5, 'tStopRefresh')  # time at next scr refresh
                sound_5.stop()
        # start/stop finish_sound_practice_resp
        if finish_sound_practice_resp.status == NOT_STARTED and tThisFlip >= 59-frameTolerance:
            # keep track of start time/frame for later
            finish_sound_practice_resp.frameNStart = frameN  # exact frame index
            finish_sound_practice_resp.tStart = t  # local t and not account for scr refresh
            finish_sound_practice_resp.tStartRefresh = tThisFlipGlobal  # on global time
            finish_sound_practice_resp.play(when=win)  # sync with win flip
        if finish_sound_practice_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_sound_practice_resp.tStartRefresh + 1-frameTolerance:
                # keep track of stop time/frame for later
                finish_sound_practice_resp.tStop = t  # not accounting for scr refresh
                finish_sound_practice_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_sound_practice_resp, 'tStopRefresh')  # time at next scr refresh
                finish_sound_practice_resp.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discuss_practiceComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discuss_practice"-------
    for thisComponent in discuss_practiceComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('text_7.started', text_7.tStartRefresh)
    practice.addData('text_7.stopped', text_7.tStopRefresh)
    practice.addData('text_8.started', text_8.tStartRefresh)
    practice.addData('text_8.stopped', text_8.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    practice.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        practice.addData('key_resp_3.rt', key_resp_3.rt)
    practice.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    practice.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    outlet.push_sample(x=[1])
    sound_4.stop()  # ensure sound has stopped at end of routine
    practice.addData('sound_4.started', sound_4.tStartRefresh)
    practice.addData('sound_4.stopped', sound_4.tStopRefresh)
    sound_5.stop()  # ensure sound has stopped at end of routine
    practice.addData('sound_5.started', sound_5.tStartRefresh)
    practice.addData('sound_5.stopped', sound_5.tStopRefresh)
    finish_sound_practice_resp.stop()  # ensure sound has stopped at end of routine
    practice.addData('finish_sound_practice_resp.started', finish_sound_practice_resp.tStartRefresh)
    practice.addData('finish_sound_practice_resp.stopped', finish_sound_practice_resp.tStopRefresh)
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    sound_11.setSound('A', secs=0.25, hamming=True)
    sound_11.setVolume(1.0, log=False)
    sound_12.setSound('A', secs=0.25, hamming=True)
    sound_12.setVolume(1.0, log=False)
    sound_13.setSound('A', secs=1.0, hamming=True)
    sound_13.setVolume(1.0, log=False)
    # keep track of which components have finished
    restComponents = [rest_text, key_resp_4, sound_11, sound_12, sound_13]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_text* updates
        if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text.frameNStart = frameN  # exact frame index
            rest_text.tStart = t  # local t and not account for scr refresh
            rest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
            rest_text.setAutoDraw(True)
        if rest_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_text.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                rest_text.tStop = t  # not accounting for scr refresh
                rest_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
                rest_text.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_11
        if sound_11.status == NOT_STARTED and tThisFlip >= 27-frameTolerance:
            # keep track of start time/frame for later
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.tStart = t  # local t and not account for scr refresh
            sound_11.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11.play(when=win)  # sync with win flip
        if sound_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_11.tStop = t  # not accounting for scr refresh
                sound_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11, 'tStopRefresh')  # time at next scr refresh
                sound_11.stop()
        # start/stop sound_12
        if sound_12.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
            # keep track of start time/frame for later
            sound_12.frameNStart = frameN  # exact frame index
            sound_12.tStart = t  # local t and not account for scr refresh
            sound_12.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12.play(when=win)  # sync with win flip
        if sound_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_12.tStop = t  # not accounting for scr refresh
                sound_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12, 'tStopRefresh')  # time at next scr refresh
                sound_12.stop()
        # start/stop sound_13
        if sound_13.status == NOT_STARTED and tThisFlip >= 29-frameTolerance:
            # keep track of start time/frame for later
            sound_13.frameNStart = frameN  # exact frame index
            sound_13.tStart = t  # local t and not account for scr refresh
            sound_13.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13.play(when=win)  # sync with win flip
        if sound_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_13.tStop = t  # not accounting for scr refresh
                sound_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13, 'tStopRefresh')  # time at next scr refresh
                sound_13.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('rest_text.started', rest_text.tStartRefresh)
    practice.addData('rest_text.stopped', rest_text.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    practice.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        practice.addData('key_resp_4.rt', key_resp_4.rt)
    practice.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    practice.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    sound_11.stop()  # ensure sound has stopped at end of routine
    practice.addData('sound_11.started', sound_11.tStartRefresh)
    practice.addData('sound_11.stopped', sound_11.tStopRefresh)
    sound_12.stop()  # ensure sound has stopped at end of routine
    practice.addData('sound_12.started', sound_12.tStartRefresh)
    practice.addData('sound_12.stopped', sound_12.tStopRefresh)
    sound_13.stop()  # ensure sound has stopped at end of routine
    practice.addData('sound_13.started', sound_13.tStartRefresh)
    practice.addData('sound_13.stopped', sound_13.tStopRefresh)
# completed 1.0 repeats of 'practice'


# ------Prepare to start Routine "main_intro"-------
continueRoutine = True
# update component parameters for each repeat
main_question.setText("Nice work on the practice!\n\nNow that you've had a chance to practice do you have any questions? You have one minute to rest and ask questions.\n")
end_main_intro.keys = []
end_main_intro.rt = []
_end_main_intro_allKeys = []
# keep track of which components have finished
main_introComponents = [main_question, end_main_intro]
for thisComponent in main_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
main_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "main_intro"-------
while continueRoutine:
    # get current time
    t = main_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=main_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *main_question* updates
    if main_question.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        main_question.frameNStart = frameN  # exact frame index
        main_question.tStart = t  # local t and not account for scr refresh
        main_question.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(main_question, 'tStartRefresh')  # time at next scr refresh
        main_question.setAutoDraw(True)
    if main_question.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > main_question.tStartRefresh + 60-frameTolerance:
            # keep track of stop time/frame for later
            main_question.tStop = t  # not accounting for scr refresh
            main_question.frameNStop = frameN  # exact frame index
            win.timeOnFlip(main_question, 'tStopRefresh')  # time at next scr refresh
            main_question.setAutoDraw(False)
    
    # *end_main_intro* updates
    waitOnFlip = False
    if end_main_intro.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        end_main_intro.frameNStart = frameN  # exact frame index
        end_main_intro.tStart = t  # local t and not account for scr refresh
        end_main_intro.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(end_main_intro, 'tStartRefresh')  # time at next scr refresh
        end_main_intro.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(end_main_intro.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(end_main_intro.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if end_main_intro.status == STARTED and not waitOnFlip:
        theseKeys = end_main_intro.getKeys(keyList=['q', 'space'], waitRelease=False)
        _end_main_intro_allKeys.extend(theseKeys)
        if len(_end_main_intro_allKeys):
            end_main_intro.keys = _end_main_intro_allKeys[-1].name  # just the last key pressed
            end_main_intro.rt = _end_main_intro_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in main_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "main_intro"-------
for thisComponent in main_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('main_question.started', main_question.tStartRefresh)
thisExp.addData('main_question.stopped', main_question.tStopRefresh)
# check responses
if end_main_intro.keys in ['', [], None]:  # No response was made
    end_main_intro.keys = None
thisExp.addData('end_main_intro.keys',end_main_intro.keys)
if end_main_intro.keys != None:  # we had a response
    thisExp.addData('end_main_intro.rt', end_main_intro.rt)
thisExp.addData('end_main_intro.started', end_main_intro.tStartRefresh)
thisExp.addData('end_main_intro.stopped', end_main_intro.tStopRefresh)
thisExp.nextEntry()
# the Routine "main_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
main = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_stims.xlsx'),
    seed=None, name='main')
thisExp.addLoop(main)  # add the loop to the experiment
thisMain = main.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisMain.rgb)
if thisMain != None:
    for paramName in thisMain:
        exec('{} = thisMain[paramName]'.format(paramName))

for thisMain in main:
    currentLoop = main
    # abbreviate parameter names if possible (e.g. rgb = thisMain.rgb)
    if thisMain != None:
        for paramName in thisMain:
            exec('{} = thisMain[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "main_prompt"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    text_4.setText(main_questions
)
    start_main_discuss.keys = []
    start_main_discuss.rt = []
    _start_main_discuss_allKeys = []
    sound_19.setSound('A', secs=0.25, hamming=True)
    sound_19.setVolume(1.0, log=False)
    sound_20.setSound('A', secs=0.25, hamming=True)
    sound_20.setVolume(1.0, log=False)
    finish_sound_main_prompt.setSound('A', secs=1.0, hamming=True)
    finish_sound_main_prompt.setVolume(1.0, log=False)
    # keep track of which components have finished
    main_promptComponents = [text_4, text_10, start_main_discuss, sound_19, sound_20, finish_sound_main_prompt]
    for thisComponent in main_promptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    main_promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "main_prompt"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = main_promptClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=main_promptClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_4* updates
        if text_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_4.frameNStart = frameN  # exact frame index
            text_4.tStart = t  # local t and not account for scr refresh
            text_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_4, 'tStartRefresh')  # time at next scr refresh
            text_4.setAutoDraw(True)
        if text_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_4.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_4.tStop = t  # not accounting for scr refresh
                text_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_4, 'tStopRefresh')  # time at next scr refresh
                text_4.setAutoDraw(False)
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        if text_10.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_10.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_10.tStop = t  # not accounting for scr refresh
                text_10.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_10, 'tStopRefresh')  # time at next scr refresh
                text_10.setAutoDraw(False)
        
        # *start_main_discuss* updates
        waitOnFlip = False
        if start_main_discuss.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            start_main_discuss.frameNStart = frameN  # exact frame index
            start_main_discuss.tStart = t  # local t and not account for scr refresh
            start_main_discuss.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(start_main_discuss, 'tStartRefresh')  # time at next scr refresh
            start_main_discuss.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(start_main_discuss.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(start_main_discuss.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if start_main_discuss.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > start_main_discuss.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                start_main_discuss.tStop = t  # not accounting for scr refresh
                start_main_discuss.frameNStop = frameN  # exact frame index
                win.timeOnFlip(start_main_discuss, 'tStopRefresh')  # time at next scr refresh
                start_main_discuss.status = FINISHED
        if start_main_discuss.status == STARTED and not waitOnFlip:
            theseKeys = start_main_discuss.getKeys(keyList=['space'], waitRelease=False)
            _start_main_discuss_allKeys.extend(theseKeys)
            if len(_start_main_discuss_allKeys):
                start_main_discuss.keys = _start_main_discuss_allKeys[-1].name  # just the last key pressed
                start_main_discuss.rt = _start_main_discuss_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_19
        if sound_19.status == NOT_STARTED and tThisFlip >= 17-frameTolerance:
            # keep track of start time/frame for later
            sound_19.frameNStart = frameN  # exact frame index
            sound_19.tStart = t  # local t and not account for scr refresh
            sound_19.tStartRefresh = tThisFlipGlobal  # on global time
            sound_19.play(when=win)  # sync with win flip
        if sound_19.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_19.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_19.tStop = t  # not accounting for scr refresh
                sound_19.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_19, 'tStopRefresh')  # time at next scr refresh
                sound_19.stop()
        # start/stop sound_20
        if sound_20.status == NOT_STARTED and tThisFlip >= 18-frameTolerance:
            # keep track of start time/frame for later
            sound_20.frameNStart = frameN  # exact frame index
            sound_20.tStart = t  # local t and not account for scr refresh
            sound_20.tStartRefresh = tThisFlipGlobal  # on global time
            sound_20.play(when=win)  # sync with win flip
        if sound_20.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_20.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_20.tStop = t  # not accounting for scr refresh
                sound_20.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_20, 'tStopRefresh')  # time at next scr refresh
                sound_20.stop()
        # start/stop finish_sound_main_prompt
        if finish_sound_main_prompt.status == NOT_STARTED and tThisFlip >= 19-frameTolerance:
            # keep track of start time/frame for later
            finish_sound_main_prompt.frameNStart = frameN  # exact frame index
            finish_sound_main_prompt.tStart = t  # local t and not account for scr refresh
            finish_sound_main_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            finish_sound_main_prompt.play(when=win)  # sync with win flip
        if finish_sound_main_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_sound_main_prompt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                finish_sound_main_prompt.tStop = t  # not accounting for scr refresh
                finish_sound_main_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_sound_main_prompt, 'tStopRefresh')  # time at next scr refresh
                finish_sound_main_prompt.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in main_promptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "main_prompt"-------
    for thisComponent in main_promptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main.addData('text_4.started', text_4.tStartRefresh)
    main.addData('text_4.stopped', text_4.tStopRefresh)
    main.addData('text_10.started', text_10.tStartRefresh)
    main.addData('text_10.stopped', text_10.tStopRefresh)
    # check responses
    if start_main_discuss.keys in ['', [], None]:  # No response was made
        start_main_discuss.keys = None
    main.addData('start_main_discuss.keys',start_main_discuss.keys)
    if start_main_discuss.keys != None:  # we had a response
        main.addData('start_main_discuss.rt', start_main_discuss.rt)
    main.addData('start_main_discuss.started', start_main_discuss.tStartRefresh)
    main.addData('start_main_discuss.stopped', start_main_discuss.tStopRefresh)
    sound_19.stop()  # ensure sound has stopped at end of routine
    main.addData('sound_19.started', sound_19.tStartRefresh)
    main.addData('sound_19.stopped', sound_19.tStopRefresh)
    sound_20.stop()  # ensure sound has stopped at end of routine
    main.addData('sound_20.started', sound_20.tStartRefresh)
    main.addData('sound_20.stopped', sound_20.tStopRefresh)
    finish_sound_main_prompt.stop()  # ensure sound has stopped at end of routine
    main.addData('finish_sound_main_prompt.started', finish_sound_main_prompt.tStartRefresh)
    main.addData('finish_sound_main_prompt.stopped', finish_sound_main_prompt.tStopRefresh)
    
    # ------Prepare to start Routine "discuss_main"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    key_resp_8.keys = []
    key_resp_8.rt = []
    _key_resp_8_allKeys = []
    outlet.push_sample(x=[2])
    sound_7.setSound('A', secs=0.25, hamming=True)
    sound_7.setVolume(1.0, log=False)
    sound_8.setSound('A', secs=0.25, hamming=True)
    sound_8.setVolume(1.0, log=False)
    finish_sound_main_resp.setSound('A', secs=1.0, hamming=True)
    finish_sound_main_resp.setVolume(1.0, log=False)
    # keep track of which components have finished
    discuss_mainComponents = [text_15, text_16, key_resp_8, sound_7, sound_8, finish_sound_main_resp]
    for thisComponent in discuss_mainComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    discuss_mainClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "discuss_main"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = discuss_mainClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=discuss_mainClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_15* updates
        if text_15.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_15.frameNStart = frameN  # exact frame index
            text_15.tStart = t  # local t and not account for scr refresh
            text_15.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_15, 'tStartRefresh')  # time at next scr refresh
            text_15.setAutoDraw(True)
        if text_15.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_15.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_15.tStop = t  # not accounting for scr refresh
                text_15.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_15, 'tStopRefresh')  # time at next scr refresh
                text_15.setAutoDraw(False)
        
        # *text_16* updates
        if text_16.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_16.frameNStart = frameN  # exact frame index
            text_16.tStart = t  # local t and not account for scr refresh
            text_16.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_16, 'tStartRefresh')  # time at next scr refresh
            text_16.setAutoDraw(True)
        if text_16.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_16.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_16.tStop = t  # not accounting for scr refresh
                text_16.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_16, 'tStopRefresh')  # time at next scr refresh
                text_16.setAutoDraw(False)
        
        # *key_resp_8* updates
        waitOnFlip = False
        if key_resp_8.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_8.frameNStart = frameN  # exact frame index
            key_resp_8.tStart = t  # local t and not account for scr refresh
            key_resp_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_8, 'tStartRefresh')  # time at next scr refresh
            key_resp_8.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_8.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_8.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_8.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_8.tStop = t  # not accounting for scr refresh
                key_resp_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_8, 'tStopRefresh')  # time at next scr refresh
                key_resp_8.status = FINISHED
        if key_resp_8.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_8.getKeys(keyList=['q', 'space'], waitRelease=False)
            _key_resp_8_allKeys.extend(theseKeys)
            if len(_key_resp_8_allKeys):
                key_resp_8.keys = _key_resp_8_allKeys[-1].name  # just the last key pressed
                key_resp_8.rt = _key_resp_8_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_7
        if sound_7.status == NOT_STARTED and tThisFlip >= 57-frameTolerance:
            # keep track of start time/frame for later
            sound_7.frameNStart = frameN  # exact frame index
            sound_7.tStart = t  # local t and not account for scr refresh
            sound_7.tStartRefresh = tThisFlipGlobal  # on global time
            sound_7.play(when=win)  # sync with win flip
        if sound_7.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_7.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_7.tStop = t  # not accounting for scr refresh
                sound_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_7, 'tStopRefresh')  # time at next scr refresh
                sound_7.stop()
        # start/stop sound_8
        if sound_8.status == NOT_STARTED and tThisFlip >= 58-frameTolerance:
            # keep track of start time/frame for later
            sound_8.frameNStart = frameN  # exact frame index
            sound_8.tStart = t  # local t and not account for scr refresh
            sound_8.tStartRefresh = tThisFlipGlobal  # on global time
            sound_8.play(when=win)  # sync with win flip
        if sound_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_8.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_8.tStop = t  # not accounting for scr refresh
                sound_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_8, 'tStopRefresh')  # time at next scr refresh
                sound_8.stop()
        # start/stop finish_sound_main_resp
        if finish_sound_main_resp.status == NOT_STARTED and tThisFlip >= 59-frameTolerance:
            # keep track of start time/frame for later
            finish_sound_main_resp.frameNStart = frameN  # exact frame index
            finish_sound_main_resp.tStart = t  # local t and not account for scr refresh
            finish_sound_main_resp.tStartRefresh = tThisFlipGlobal  # on global time
            finish_sound_main_resp.play(when=win)  # sync with win flip
        if finish_sound_main_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_sound_main_resp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                finish_sound_main_resp.tStop = t  # not accounting for scr refresh
                finish_sound_main_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_sound_main_resp, 'tStopRefresh')  # time at next scr refresh
                finish_sound_main_resp.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discuss_mainComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discuss_main"-------
    for thisComponent in discuss_mainComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main.addData('text_15.started', text_15.tStartRefresh)
    main.addData('text_15.stopped', text_15.tStopRefresh)
    main.addData('text_16.started', text_16.tStartRefresh)
    main.addData('text_16.stopped', text_16.tStopRefresh)
    # check responses
    if key_resp_8.keys in ['', [], None]:  # No response was made
        key_resp_8.keys = None
    main.addData('key_resp_8.keys',key_resp_8.keys)
    if key_resp_8.keys != None:  # we had a response
        main.addData('key_resp_8.rt', key_resp_8.rt)
    main.addData('key_resp_8.started', key_resp_8.tStartRefresh)
    main.addData('key_resp_8.stopped', key_resp_8.tStopRefresh)
    outlet.push_sample(x=[2])
    sound_7.stop()  # ensure sound has stopped at end of routine
    main.addData('sound_7.started', sound_7.tStartRefresh)
    main.addData('sound_7.stopped', sound_7.tStopRefresh)
    sound_8.stop()  # ensure sound has stopped at end of routine
    main.addData('sound_8.started', sound_8.tStartRefresh)
    main.addData('sound_8.stopped', sound_8.tStopRefresh)
    finish_sound_main_resp.stop()  # ensure sound has stopped at end of routine
    main.addData('finish_sound_main_resp.started', finish_sound_main_resp.tStartRefresh)
    main.addData('finish_sound_main_resp.stopped', finish_sound_main_resp.tStopRefresh)
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    sound_11.setSound('A', secs=0.25, hamming=True)
    sound_11.setVolume(1.0, log=False)
    sound_12.setSound('A', secs=0.25, hamming=True)
    sound_12.setVolume(1.0, log=False)
    sound_13.setSound('A', secs=1.0, hamming=True)
    sound_13.setVolume(1.0, log=False)
    # keep track of which components have finished
    restComponents = [rest_text, key_resp_4, sound_11, sound_12, sound_13]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_text* updates
        if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text.frameNStart = frameN  # exact frame index
            rest_text.tStart = t  # local t and not account for scr refresh
            rest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
            rest_text.setAutoDraw(True)
        if rest_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_text.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                rest_text.tStop = t  # not accounting for scr refresh
                rest_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
                rest_text.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_11
        if sound_11.status == NOT_STARTED and tThisFlip >= 27-frameTolerance:
            # keep track of start time/frame for later
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.tStart = t  # local t and not account for scr refresh
            sound_11.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11.play(when=win)  # sync with win flip
        if sound_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_11.tStop = t  # not accounting for scr refresh
                sound_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11, 'tStopRefresh')  # time at next scr refresh
                sound_11.stop()
        # start/stop sound_12
        if sound_12.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
            # keep track of start time/frame for later
            sound_12.frameNStart = frameN  # exact frame index
            sound_12.tStart = t  # local t and not account for scr refresh
            sound_12.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12.play(when=win)  # sync with win flip
        if sound_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_12.tStop = t  # not accounting for scr refresh
                sound_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12, 'tStopRefresh')  # time at next scr refresh
                sound_12.stop()
        # start/stop sound_13
        if sound_13.status == NOT_STARTED and tThisFlip >= 29-frameTolerance:
            # keep track of start time/frame for later
            sound_13.frameNStart = frameN  # exact frame index
            sound_13.tStart = t  # local t and not account for scr refresh
            sound_13.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13.play(when=win)  # sync with win flip
        if sound_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_13.tStop = t  # not accounting for scr refresh
                sound_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13, 'tStopRefresh')  # time at next scr refresh
                sound_13.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main.addData('rest_text.started', rest_text.tStartRefresh)
    main.addData('rest_text.stopped', rest_text.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    main.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        main.addData('key_resp_4.rt', key_resp_4.rt)
    main.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    main.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    sound_11.stop()  # ensure sound has stopped at end of routine
    main.addData('sound_11.started', sound_11.tStartRefresh)
    main.addData('sound_11.stopped', sound_11.tStopRefresh)
    sound_12.stop()  # ensure sound has stopped at end of routine
    main.addData('sound_12.started', sound_12.tStartRefresh)
    main.addData('sound_12.stopped', sound_12.tStopRefresh)
    sound_13.stop()  # ensure sound has stopped at end of routine
    main.addData('sound_13.started', sound_13.tStartRefresh)
    main.addData('sound_13.stopped', sound_13.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'main'


# ------Prepare to start Routine "inflam_intro"-------
continueRoutine = True
# update component parameters for each repeat
skip.keys = []
skip.rt = []
_skip_allKeys = []
# keep track of which components have finished
inflam_introComponents = [text_13, skip, text_22]
for thisComponent in inflam_introComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
inflam_introClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "inflam_intro"-------
while continueRoutine:
    # get current time
    t = inflam_introClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=inflam_introClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_13* updates
    if text_13.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_13.frameNStart = frameN  # exact frame index
        text_13.tStart = t  # local t and not account for scr refresh
        text_13.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_13, 'tStartRefresh')  # time at next scr refresh
        text_13.setAutoDraw(True)
    
    # *skip* updates
    waitOnFlip = False
    if skip.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
        # keep track of start time/frame for later
        skip.frameNStart = frameN  # exact frame index
        skip.tStart = t  # local t and not account for scr refresh
        skip.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(skip, 'tStartRefresh')  # time at next scr refresh
        skip.status = STARTED
        # keyboard checking is just starting
        waitOnFlip = True
        win.callOnFlip(skip.clock.reset)  # t=0 on next screen flip
        win.callOnFlip(skip.clearEvents, eventType='keyboard')  # clear events on next screen flip
    if skip.status == STARTED and not waitOnFlip:
        theseKeys = skip.getKeys(keyList=['q', 'space'], waitRelease=False)
        _skip_allKeys.extend(theseKeys)
        if len(_skip_allKeys):
            skip.keys = _skip_allKeys[-1].name  # just the last key pressed
            skip.rt = _skip_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
    # *text_22* updates
    if text_22.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
        # keep track of start time/frame for later
        text_22.frameNStart = frameN  # exact frame index
        text_22.tStart = t  # local t and not account for scr refresh
        text_22.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_22, 'tStartRefresh')  # time at next scr refresh
        text_22.setAutoDraw(True)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in inflam_introComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "inflam_intro"-------
for thisComponent in inflam_introComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_13.started', text_13.tStartRefresh)
thisExp.addData('text_13.stopped', text_13.tStopRefresh)
# check responses
if skip.keys in ['', [], None]:  # No response was made
    skip.keys = None
thisExp.addData('skip.keys',skip.keys)
if skip.keys != None:  # we had a response
    thisExp.addData('skip.rt', skip.rt)
thisExp.addData('skip.started', skip.tStartRefresh)
thisExp.addData('skip.stopped', skip.tStopRefresh)
thisExp.nextEntry()
thisExp.addData('text_22.started', text_22.tStartRefresh)
thisExp.addData('text_22.stopped', text_22.tStopRefresh)
# the Routine "inflam_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
inflam = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_stims.xlsx'),
    seed=None, name='inflam')
thisExp.addLoop(inflam)  # add the loop to the experiment
thisInflam = inflam.trialList[0]  # so we can initialise stimuli with some values
# abbreviate parameter names if possible (e.g. rgb = thisInflam.rgb)
if thisInflam != None:
    for paramName in thisInflam:
        exec('{} = thisInflam[paramName]'.format(paramName))

for thisInflam in inflam:
    currentLoop = inflam
    # abbreviate parameter names if possible (e.g. rgb = thisInflam.rgb)
    if thisInflam != None:
        for paramName in thisInflam:
            exec('{} = thisInflam[paramName]'.format(paramName))
    
    # ------Prepare to start Routine "inflam_prompt"-------
    continueRoutine = True
    routineTimer.add(20.000000)
    # update component parameters for each repeat
    text_11.setText(inflam_questions)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    sound_17.setSound('A', secs=0.25, hamming=True)
    sound_17.setVolume(1.0, log=False)
    sound_18.setSound('A', secs=0.25, hamming=True)
    sound_18.setVolume(1.0, log=False)
    finish_sound_inflam_prompt.setSound('A', secs=1.0, hamming=True)
    finish_sound_inflam_prompt.setVolume(1.0, log=False)
    # keep track of which components have finished
    inflam_promptComponents = [text_11, text_12, key_resp_6, sound_17, sound_18, finish_sound_inflam_prompt]
    for thisComponent in inflam_promptComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    inflam_promptClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "inflam_prompt"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = inflam_promptClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=inflam_promptClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_11* updates
        if text_11.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_11.frameNStart = frameN  # exact frame index
            text_11.tStart = t  # local t and not account for scr refresh
            text_11.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_11, 'tStartRefresh')  # time at next scr refresh
            text_11.setAutoDraw(True)
        if text_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_11.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_11.tStop = t  # not accounting for scr refresh
                text_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_11, 'tStopRefresh')  # time at next scr refresh
                text_11.setAutoDraw(False)
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        if text_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_12.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                text_12.tStop = t  # not accounting for scr refresh
                text_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_12, 'tStopRefresh')  # time at next scr refresh
                text_12.setAutoDraw(False)
        
        # *key_resp_6* updates
        waitOnFlip = False
        if key_resp_6.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_6.frameNStart = frameN  # exact frame index
            key_resp_6.tStart = t  # local t and not account for scr refresh
            key_resp_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_6, 'tStartRefresh')  # time at next scr refresh
            key_resp_6.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_6.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_6.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_6.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_6.tStartRefresh + 20-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_6.tStop = t  # not accounting for scr refresh
                key_resp_6.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_6, 'tStopRefresh')  # time at next scr refresh
                key_resp_6.status = FINISHED
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_17
        if sound_17.status == NOT_STARTED and tThisFlip >= 17-frameTolerance:
            # keep track of start time/frame for later
            sound_17.frameNStart = frameN  # exact frame index
            sound_17.tStart = t  # local t and not account for scr refresh
            sound_17.tStartRefresh = tThisFlipGlobal  # on global time
            sound_17.play(when=win)  # sync with win flip
        if sound_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_17.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_17.tStop = t  # not accounting for scr refresh
                sound_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_17, 'tStopRefresh')  # time at next scr refresh
                sound_17.stop()
        # start/stop sound_18
        if sound_18.status == NOT_STARTED and tThisFlip >= 18-frameTolerance:
            # keep track of start time/frame for later
            sound_18.frameNStart = frameN  # exact frame index
            sound_18.tStart = t  # local t and not account for scr refresh
            sound_18.tStartRefresh = tThisFlipGlobal  # on global time
            sound_18.play(when=win)  # sync with win flip
        if sound_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_18.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_18.tStop = t  # not accounting for scr refresh
                sound_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_18, 'tStopRefresh')  # time at next scr refresh
                sound_18.stop()
        # start/stop finish_sound_inflam_prompt
        if finish_sound_inflam_prompt.status == NOT_STARTED and tThisFlip >= 19-frameTolerance:
            # keep track of start time/frame for later
            finish_sound_inflam_prompt.frameNStart = frameN  # exact frame index
            finish_sound_inflam_prompt.tStart = t  # local t and not account for scr refresh
            finish_sound_inflam_prompt.tStartRefresh = tThisFlipGlobal  # on global time
            finish_sound_inflam_prompt.play(when=win)  # sync with win flip
        if finish_sound_inflam_prompt.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_sound_inflam_prompt.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                finish_sound_inflam_prompt.tStop = t  # not accounting for scr refresh
                finish_sound_inflam_prompt.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_sound_inflam_prompt, 'tStopRefresh')  # time at next scr refresh
                finish_sound_inflam_prompt.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in inflam_promptComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "inflam_prompt"-------
    for thisComponent in inflam_promptComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    inflam.addData('text_11.started', text_11.tStartRefresh)
    inflam.addData('text_11.stopped', text_11.tStopRefresh)
    inflam.addData('text_12.started', text_12.tStartRefresh)
    inflam.addData('text_12.stopped', text_12.tStopRefresh)
    # check responses
    if key_resp_6.keys in ['', [], None]:  # No response was made
        key_resp_6.keys = None
    inflam.addData('key_resp_6.keys',key_resp_6.keys)
    if key_resp_6.keys != None:  # we had a response
        inflam.addData('key_resp_6.rt', key_resp_6.rt)
    inflam.addData('key_resp_6.started', key_resp_6.tStartRefresh)
    inflam.addData('key_resp_6.stopped', key_resp_6.tStopRefresh)
    sound_17.stop()  # ensure sound has stopped at end of routine
    inflam.addData('sound_17.started', sound_17.tStartRefresh)
    inflam.addData('sound_17.stopped', sound_17.tStopRefresh)
    sound_18.stop()  # ensure sound has stopped at end of routine
    inflam.addData('sound_18.started', sound_18.tStartRefresh)
    inflam.addData('sound_18.stopped', sound_18.tStopRefresh)
    finish_sound_inflam_prompt.stop()  # ensure sound has stopped at end of routine
    inflam.addData('finish_sound_inflam_prompt.started', finish_sound_inflam_prompt.tStartRefresh)
    inflam.addData('finish_sound_inflam_prompt.stopped', finish_sound_inflam_prompt.tStopRefresh)
    
    # ------Prepare to start Routine "discuss_inflam"-------
    continueRoutine = True
    routineTimer.add(60.000000)
    # update component parameters for each repeat
    key_resp_9.keys = []
    key_resp_9.rt = []
    _key_resp_9_allKeys = []
    outlet.push_sample(x=[3])
    sound_14.setSound('A', secs=0.25, hamming=True)
    sound_14.setVolume(1.0, log=False)
    sound_21.setSound('A', secs=0.25, hamming=True)
    sound_21.setVolume(1.0, log=False)
    finish_sound_inflam_resp.setSound('A', secs=1.0, hamming=True)
    finish_sound_inflam_resp.setVolume(1.0, log=False)
    # keep track of which components have finished
    discuss_inflamComponents = [text_17, text_18, key_resp_9, sound_14, sound_21, finish_sound_inflam_resp]
    for thisComponent in discuss_inflamComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    discuss_inflamClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "discuss_inflam"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = discuss_inflamClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=discuss_inflamClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_17* updates
        if text_17.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_17.frameNStart = frameN  # exact frame index
            text_17.tStart = t  # local t and not account for scr refresh
            text_17.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_17, 'tStartRefresh')  # time at next scr refresh
            text_17.setAutoDraw(True)
        if text_17.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_17.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_17.tStop = t  # not accounting for scr refresh
                text_17.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_17, 'tStopRefresh')  # time at next scr refresh
                text_17.setAutoDraw(False)
        
        # *text_18* updates
        if text_18.status == NOT_STARTED and tThisFlip >= 0-frameTolerance:
            # keep track of start time/frame for later
            text_18.frameNStart = frameN  # exact frame index
            text_18.tStart = t  # local t and not account for scr refresh
            text_18.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_18, 'tStartRefresh')  # time at next scr refresh
            text_18.setAutoDraw(True)
        if text_18.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_18.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                text_18.tStop = t  # not accounting for scr refresh
                text_18.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_18, 'tStopRefresh')  # time at next scr refresh
                text_18.setAutoDraw(False)
        
        # *key_resp_9* updates
        waitOnFlip = False
        if key_resp_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_9.frameNStart = frameN  # exact frame index
            key_resp_9.tStart = t  # local t and not account for scr refresh
            key_resp_9.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_9, 'tStartRefresh')  # time at next scr refresh
            key_resp_9.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_9.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_9.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_9.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_9.tStartRefresh + 60-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_9.tStop = t  # not accounting for scr refresh
                key_resp_9.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_9, 'tStopRefresh')  # time at next scr refresh
                key_resp_9.status = FINISHED
        if key_resp_9.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_9.getKeys(keyList=['q', 'space'], waitRelease=False)
            _key_resp_9_allKeys.extend(theseKeys)
            if len(_key_resp_9_allKeys):
                key_resp_9.keys = _key_resp_9_allKeys[-1].name  # just the last key pressed
                key_resp_9.rt = _key_resp_9_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_14
        if sound_14.status == NOT_STARTED and tThisFlip >= 57-frameTolerance:
            # keep track of start time/frame for later
            sound_14.frameNStart = frameN  # exact frame index
            sound_14.tStart = t  # local t and not account for scr refresh
            sound_14.tStartRefresh = tThisFlipGlobal  # on global time
            sound_14.play(when=win)  # sync with win flip
        if sound_14.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_14.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_14.tStop = t  # not accounting for scr refresh
                sound_14.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_14, 'tStopRefresh')  # time at next scr refresh
                sound_14.stop()
        # start/stop sound_21
        if sound_21.status == NOT_STARTED and tThisFlip >= 58-frameTolerance:
            # keep track of start time/frame for later
            sound_21.frameNStart = frameN  # exact frame index
            sound_21.tStart = t  # local t and not account for scr refresh
            sound_21.tStartRefresh = tThisFlipGlobal  # on global time
            sound_21.play(when=win)  # sync with win flip
        if sound_21.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_21.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_21.tStop = t  # not accounting for scr refresh
                sound_21.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_21, 'tStopRefresh')  # time at next scr refresh
                sound_21.stop()
        # start/stop finish_sound_inflam_resp
        if finish_sound_inflam_resp.status == NOT_STARTED and tThisFlip >= 59-frameTolerance:
            # keep track of start time/frame for later
            finish_sound_inflam_resp.frameNStart = frameN  # exact frame index
            finish_sound_inflam_resp.tStart = t  # local t and not account for scr refresh
            finish_sound_inflam_resp.tStartRefresh = tThisFlipGlobal  # on global time
            finish_sound_inflam_resp.play(when=win)  # sync with win flip
        if finish_sound_inflam_resp.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > finish_sound_inflam_resp.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                finish_sound_inflam_resp.tStop = t  # not accounting for scr refresh
                finish_sound_inflam_resp.frameNStop = frameN  # exact frame index
                win.timeOnFlip(finish_sound_inflam_resp, 'tStopRefresh')  # time at next scr refresh
                finish_sound_inflam_resp.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discuss_inflamComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discuss_inflam"-------
    for thisComponent in discuss_inflamComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    inflam.addData('text_17.started', text_17.tStartRefresh)
    inflam.addData('text_17.stopped', text_17.tStopRefresh)
    inflam.addData('text_18.started', text_18.tStartRefresh)
    inflam.addData('text_18.stopped', text_18.tStopRefresh)
    # check responses
    if key_resp_9.keys in ['', [], None]:  # No response was made
        key_resp_9.keys = None
    inflam.addData('key_resp_9.keys',key_resp_9.keys)
    if key_resp_9.keys != None:  # we had a response
        inflam.addData('key_resp_9.rt', key_resp_9.rt)
    inflam.addData('key_resp_9.started', key_resp_9.tStartRefresh)
    inflam.addData('key_resp_9.stopped', key_resp_9.tStopRefresh)
    outlet.push_sample(x=[3])
    sound_14.stop()  # ensure sound has stopped at end of routine
    inflam.addData('sound_14.started', sound_14.tStartRefresh)
    inflam.addData('sound_14.stopped', sound_14.tStopRefresh)
    sound_21.stop()  # ensure sound has stopped at end of routine
    inflam.addData('sound_21.started', sound_21.tStartRefresh)
    inflam.addData('sound_21.stopped', sound_21.tStopRefresh)
    finish_sound_inflam_resp.stop()  # ensure sound has stopped at end of routine
    inflam.addData('finish_sound_inflam_resp.started', finish_sound_inflam_resp.tStartRefresh)
    inflam.addData('finish_sound_inflam_resp.stopped', finish_sound_inflam_resp.tStopRefresh)
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    routineTimer.add(30.000000)
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    sound_11.setSound('A', secs=0.25, hamming=True)
    sound_11.setVolume(1.0, log=False)
    sound_12.setSound('A', secs=0.25, hamming=True)
    sound_12.setVolume(1.0, log=False)
    sound_13.setSound('A', secs=1.0, hamming=True)
    sound_13.setVolume(1.0, log=False)
    # keep track of which components have finished
    restComponents = [rest_text, key_resp_4, sound_11, sound_12, sound_13]
    for thisComponent in restComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    restClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "rest"-------
    while continueRoutine and routineTimer.getTime() > 0:
        # get current time
        t = restClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=restClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *rest_text* updates
        if rest_text.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            rest_text.frameNStart = frameN  # exact frame index
            rest_text.tStart = t  # local t and not account for scr refresh
            rest_text.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(rest_text, 'tStartRefresh')  # time at next scr refresh
            rest_text.setAutoDraw(True)
        if rest_text.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > rest_text.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                rest_text.tStop = t  # not accounting for scr refresh
                rest_text.frameNStop = frameN  # exact frame index
                win.timeOnFlip(rest_text, 'tStopRefresh')  # time at next scr refresh
                rest_text.setAutoDraw(False)
        
        # *key_resp_4* updates
        waitOnFlip = False
        if key_resp_4.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_4.frameNStart = frameN  # exact frame index
            key_resp_4.tStart = t  # local t and not account for scr refresh
            key_resp_4.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_4, 'tStartRefresh')  # time at next scr refresh
            key_resp_4.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_4.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_4.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_4.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > key_resp_4.tStartRefresh + 30-frameTolerance:
                # keep track of stop time/frame for later
                key_resp_4.tStop = t  # not accounting for scr refresh
                key_resp_4.frameNStop = frameN  # exact frame index
                win.timeOnFlip(key_resp_4, 'tStopRefresh')  # time at next scr refresh
                key_resp_4.status = FINISHED
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        # start/stop sound_11
        if sound_11.status == NOT_STARTED and tThisFlip >= 27-frameTolerance:
            # keep track of start time/frame for later
            sound_11.frameNStart = frameN  # exact frame index
            sound_11.tStart = t  # local t and not account for scr refresh
            sound_11.tStartRefresh = tThisFlipGlobal  # on global time
            sound_11.play(when=win)  # sync with win flip
        if sound_11.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_11.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_11.tStop = t  # not accounting for scr refresh
                sound_11.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_11, 'tStopRefresh')  # time at next scr refresh
                sound_11.stop()
        # start/stop sound_12
        if sound_12.status == NOT_STARTED and tThisFlip >= 28-frameTolerance:
            # keep track of start time/frame for later
            sound_12.frameNStart = frameN  # exact frame index
            sound_12.tStart = t  # local t and not account for scr refresh
            sound_12.tStartRefresh = tThisFlipGlobal  # on global time
            sound_12.play(when=win)  # sync with win flip
        if sound_12.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_12.tStartRefresh + 0.25-frameTolerance:
                # keep track of stop time/frame for later
                sound_12.tStop = t  # not accounting for scr refresh
                sound_12.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_12, 'tStopRefresh')  # time at next scr refresh
                sound_12.stop()
        # start/stop sound_13
        if sound_13.status == NOT_STARTED and tThisFlip >= 29-frameTolerance:
            # keep track of start time/frame for later
            sound_13.frameNStart = frameN  # exact frame index
            sound_13.tStart = t  # local t and not account for scr refresh
            sound_13.tStartRefresh = tThisFlipGlobal  # on global time
            sound_13.play(when=win)  # sync with win flip
        if sound_13.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > sound_13.tStartRefresh + 1.0-frameTolerance:
                # keep track of stop time/frame for later
                sound_13.tStop = t  # not accounting for scr refresh
                sound_13.frameNStop = frameN  # exact frame index
                win.timeOnFlip(sound_13, 'tStopRefresh')  # time at next scr refresh
                sound_13.stop()
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in restComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "rest"-------
    for thisComponent in restComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    inflam.addData('rest_text.started', rest_text.tStartRefresh)
    inflam.addData('rest_text.stopped', rest_text.tStopRefresh)
    # check responses
    if key_resp_4.keys in ['', [], None]:  # No response was made
        key_resp_4.keys = None
    inflam.addData('key_resp_4.keys',key_resp_4.keys)
    if key_resp_4.keys != None:  # we had a response
        inflam.addData('key_resp_4.rt', key_resp_4.rt)
    inflam.addData('key_resp_4.started', key_resp_4.tStartRefresh)
    inflam.addData('key_resp_4.stopped', key_resp_4.tStopRefresh)
    sound_11.stop()  # ensure sound has stopped at end of routine
    inflam.addData('sound_11.started', sound_11.tStartRefresh)
    inflam.addData('sound_11.stopped', sound_11.tStopRefresh)
    sound_12.stop()  # ensure sound has stopped at end of routine
    inflam.addData('sound_12.started', sound_12.tStartRefresh)
    inflam.addData('sound_12.stopped', sound_12.tStopRefresh)
    sound_13.stop()  # ensure sound has stopped at end of routine
    inflam.addData('sound_13.started', sound_13.tStartRefresh)
    inflam.addData('sound_13.stopped', sound_13.tStopRefresh)
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'inflam'


# ------Prepare to start Routine "fin"-------
continueRoutine = True
routineTimer.add(15.000000)
# update component parameters for each repeat
# keep track of which components have finished
finComponents = [text_9]
for thisComponent in finComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
finClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "fin"-------
while continueRoutine and routineTimer.getTime() > 0:
    # get current time
    t = finClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=finClock)
    tThisFlipGlobal = win.getFutureFlipTime(clock=None)
    frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
    # update/draw components on each frame
    
    # *text_9* updates
    if text_9.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
        # keep track of start time/frame for later
        text_9.frameNStart = frameN  # exact frame index
        text_9.tStart = t  # local t and not account for scr refresh
        text_9.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_9, 'tStartRefresh')  # time at next scr refresh
        text_9.setAutoDraw(True)
    if text_9.status == STARTED:
        # is it time to stop? (based on global clock, using actual start)
        if tThisFlipGlobal > text_9.tStartRefresh + 15-frameTolerance:
            # keep track of stop time/frame for later
            text_9.tStop = t  # not accounting for scr refresh
            text_9.frameNStop = frameN  # exact frame index
            win.timeOnFlip(text_9, 'tStopRefresh')  # time at next scr refresh
            text_9.setAutoDraw(False)
    
    # check for quit (typically the Esc key)
    if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
        core.quit()
    
    # check if all components have finished
    if not continueRoutine:  # a component has requested a forced-end of Routine
        break
    continueRoutine = False  # will revert to True if at least one component still running
    for thisComponent in finComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "fin"-------
for thisComponent in finComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
thisExp.addData('text_9.started', text_9.tStartRefresh)
thisExp.addData('text_9.stopped', text_9.tStopRefresh)

# Flip one final time so any remaining win.callOnFlip() 
# and win.timeOnFlip() tasks get executed before quitting
win.flip()

# these shouldn't be strictly necessary (should auto-save)
thisExp.saveAsWideText(filename+'.csv', delim='auto')
thisExp.saveAsPickle(filename)
logging.flush()
# make sure everything is closed down
if eyetracker:
    eyetracker.setConnectionState(False)
thisExp.abort()  # or data files will save again on exit
win.close()
core.quit()
