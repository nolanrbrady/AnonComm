#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
This experiment was created using PsychoPy3 Experiment Builder (v2022.1.4),
    on Fri Jun 24 13:37:19 2022
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
    originPath='/Users/nolanbrady/Desktop/LabResearch/EEG_Protocols/AnonComm/Anon_communication_lastrun.py',
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
    size=(1024, 768), fullscr=True, screen=0, 
    winType='pyglet', allowGUI=False, allowStencil=False,
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

# Initialize components for Routine "welcome"
welcomeClock = core.Clock()
text_2 = visual.TextStim(win=win, name='text_2',
    text='Thank you for taking part in our study.\n\nOur goal with this study is to understand the ways in which people communicate a little better. For this experiment you will either be talking with someone directly or with them through an anonymous chat room. We will provide a series of questions for you to discuss together, once you have read it and agree to start discussing please press the "spacebar". You will be given one minute to share with the other person your answer to the prompt. If you have any questions you are always welcome to ask your proctor.\n\nTo move on please press the "spacebar"',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_2 = keyboard.Keyboard()

# Initialize components for Routine "survey"
surveyClock = core.Clock()
text = visual.TextStim(win=win, name='text',
    text='Before we start, we just have a couple questions.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp = keyboard.Keyboard()

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

# Initialize components for Routine "discuss"
discussClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='You have one minute to tell each other about your answers.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='You have 15 more seconds.',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_discuss = visual.TextStim(win=win, name='end_discuss',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_3 = keyboard.Keyboard()

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

# Initialize components for Routine "next_question"
next_questionClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='When you are ready for the next question please hit the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

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

# Initialize components for Routine "discuss"
discussClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='You have one minute to tell each other about your answers.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='You have 15 more seconds.',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_discuss = visual.TextStim(win=win, name='end_discuss',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_3 = keyboard.Keyboard()

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

# Initialize components for Routine "next_question"
next_questionClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='When you are ready for the next question please hit the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "inflam_intro"
inflam_introClock = core.Clock()
text_13 = visual.TextStim(win=win, name='text_13',
    text="You're about to start the inflamatory introduction. Please rest for 30 seconds before beginning.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_14 = visual.TextStim(win=win, name='text_14',
    text="Please press the space bar whenever you're ready to begin.",
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_7 = keyboard.Keyboard()
skip = keyboard.Keyboard()

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
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
key_resp_6 = keyboard.Keyboard()

# Initialize components for Routine "discuss"
discussClock = core.Clock()
text_7 = visual.TextStim(win=win, name='text_7',
    text='You have one minute to tell each other about your answers.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
text_8 = visual.TextStim(win=win, name='text_8',
    text='You have 15 more seconds.',
    font='Open Sans',
    pos=(0, -0.3), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-1.0);
end_discuss = visual.TextStim(win=win, name='end_discuss',
    text=None,
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=-2.0);
key_resp_3 = keyboard.Keyboard()

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

# Initialize components for Routine "next_question"
next_questionClock = core.Clock()
text_5 = visual.TextStim(win=win, name='text_5',
    text='When you are ready for the next question please hit the spacebar.',
    font='Open Sans',
    pos=(0, 0), height=0.05, wrapWidth=None, ori=0.0, 
    color='white', colorSpace='rgb', opacity=None, 
    languageStyle='LTR',
    depth=0.0);
key_resp_5 = keyboard.Keyboard()

# Initialize components for Routine "feedback"
feedbackClock = core.Clock()

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
surveyComponents = [text, key_resp]
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
# the Routine "survey" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
practice = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_stims.xlsx', selection='0,1,2'),
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
    # update component parameters for each repeat
    text_3.setText(practice_questions)
    start_practice_discuss.keys = []
    start_practice_discuss.rt = []
    _start_practice_discuss_allKeys = []
    # keep track of which components have finished
    practice_promptComponents = [text_3, text_6, start_practice_discuss]
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
    while continueRoutine:
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
        
        # *text_6* updates
        if text_6.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            text_6.frameNStart = frameN  # exact frame index
            text_6.tStart = t  # local t and not account for scr refresh
            text_6.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_6, 'tStartRefresh')  # time at next scr refresh
            text_6.setAutoDraw(True)
        
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
        if start_practice_discuss.status == STARTED and not waitOnFlip:
            theseKeys = start_practice_discuss.getKeys(keyList=['space'], waitRelease=False)
            _start_practice_discuss_allKeys.extend(theseKeys)
            if len(_start_practice_discuss_allKeys):
                start_practice_discuss.keys = _start_practice_discuss_allKeys[-1].name  # just the last key pressed
                start_practice_discuss.rt = _start_practice_discuss_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "practice_prompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "discuss"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    discussComponents = [text_7, text_8, end_discuss, key_resp_3]
    for thisComponent in discussComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    discussClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "discuss"-------
    while continueRoutine:
        # get current time
        t = discussClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=discussClock)
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
            if tThisFlipGlobal > text_7.tStartRefresh + 65-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # *end_discuss* updates
        if end_discuss.status == NOT_STARTED and tThisFlip >= 65-frameTolerance:
            # keep track of start time/frame for later
            end_discuss.frameNStart = frameN  # exact frame index
            end_discuss.tStart = t  # local t and not account for scr refresh
            end_discuss.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_discuss, 'tStartRefresh')  # time at next scr refresh
            end_discuss.setAutoDraw(True)
        if end_discuss.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_discuss.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                end_discuss.tStop = t  # not accounting for scr refresh
                end_discuss.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_discuss, 'tStopRefresh')  # time at next scr refresh
                end_discuss.setAutoDraw(False)
        
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
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discussComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discuss"-------
    for thisComponent in discussComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('text_7.started', text_7.tStartRefresh)
    practice.addData('text_7.stopped', text_7.tStopRefresh)
    practice.addData('text_8.started', text_8.tStartRefresh)
    practice.addData('text_8.stopped', text_8.tStopRefresh)
    practice.addData('end_discuss.started', end_discuss.tStartRefresh)
    practice.addData('end_discuss.stopped', end_discuss.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    practice.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        practice.addData('key_resp_3.rt', key_resp_3.rt)
    practice.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    practice.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "discuss" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    restComponents = [rest_text, key_resp_4]
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
    while continueRoutine:
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
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "next_question"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    next_questionComponents = [text_5, key_resp_5]
    for thisComponent in next_questionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    next_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "next_question"-------
    while continueRoutine:
        # get current time
        t = next_questionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=next_questionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in next_questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "next_question"-------
    for thisComponent in next_questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    practice.addData('text_5.started', text_5.tStartRefresh)
    practice.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    practice.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        practice.addData('key_resp_5.rt', key_resp_5.rt)
    practice.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    practice.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "next_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
# completed 1.0 repeats of 'practice'


# ------Prepare to start Routine "main_intro"-------
continueRoutine = True
# update component parameters for each repeat
main_question.setText('Nice Work!\n\nNow that you\'ve had a chance to practice do you have any questions? If not press the "spacebar" and we will get started on the main task.\n')
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
        theseKeys = end_main_intro.getKeys(keyList=['space'], waitRelease=False)
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
    trialList=data.importConditions('main_stims.xlsx', selection=random(3)*7),
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
    # update component parameters for each repeat
    text_4.setText(main_questions
)
    start_main_discuss.keys = []
    start_main_discuss.rt = []
    _start_main_discuss_allKeys = []
    # keep track of which components have finished
    main_promptComponents = [text_4, text_10, start_main_discuss]
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
    while continueRoutine:
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
        
        # *text_10* updates
        if text_10.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            text_10.frameNStart = frameN  # exact frame index
            text_10.tStart = t  # local t and not account for scr refresh
            text_10.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_10, 'tStartRefresh')  # time at next scr refresh
            text_10.setAutoDraw(True)
        
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
        if start_main_discuss.status == STARTED and not waitOnFlip:
            theseKeys = start_main_discuss.getKeys(keyList=['space'], waitRelease=False)
            _start_main_discuss_allKeys.extend(theseKeys)
            if len(_start_main_discuss_allKeys):
                start_main_discuss.keys = _start_main_discuss_allKeys[-1].name  # just the last key pressed
                start_main_discuss.rt = _start_main_discuss_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "main_prompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "discuss"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    discussComponents = [text_7, text_8, end_discuss, key_resp_3]
    for thisComponent in discussComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    discussClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "discuss"-------
    while continueRoutine:
        # get current time
        t = discussClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=discussClock)
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
            if tThisFlipGlobal > text_7.tStartRefresh + 65-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # *end_discuss* updates
        if end_discuss.status == NOT_STARTED and tThisFlip >= 65-frameTolerance:
            # keep track of start time/frame for later
            end_discuss.frameNStart = frameN  # exact frame index
            end_discuss.tStart = t  # local t and not account for scr refresh
            end_discuss.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_discuss, 'tStartRefresh')  # time at next scr refresh
            end_discuss.setAutoDraw(True)
        if end_discuss.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_discuss.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                end_discuss.tStop = t  # not accounting for scr refresh
                end_discuss.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_discuss, 'tStopRefresh')  # time at next scr refresh
                end_discuss.setAutoDraw(False)
        
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
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discussComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discuss"-------
    for thisComponent in discussComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main.addData('text_7.started', text_7.tStartRefresh)
    main.addData('text_7.stopped', text_7.tStopRefresh)
    main.addData('text_8.started', text_8.tStartRefresh)
    main.addData('text_8.stopped', text_8.tStopRefresh)
    main.addData('end_discuss.started', end_discuss.tStartRefresh)
    main.addData('end_discuss.stopped', end_discuss.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    main.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        main.addData('key_resp_3.rt', key_resp_3.rt)
    main.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    main.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "discuss" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    restComponents = [rest_text, key_resp_4]
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
    while continueRoutine:
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
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "next_question"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    next_questionComponents = [text_5, key_resp_5]
    for thisComponent in next_questionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    next_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "next_question"-------
    while continueRoutine:
        # get current time
        t = next_questionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=next_questionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in next_questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "next_question"-------
    for thisComponent in next_questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    main.addData('text_5.started', text_5.tStartRefresh)
    main.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    main.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        main.addData('key_resp_5.rt', key_resp_5.rt)
    main.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    main.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "next_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'main'


# ------Prepare to start Routine "inflam_intro"-------
continueRoutine = True
# update component parameters for each repeat
key_resp_7.keys = []
key_resp_7.rt = []
_key_resp_7_allKeys = []
skip.keys = []
skip.rt = []
_skip_allKeys = []
# keep track of which components have finished
inflam_introComponents = [text_13, text_14, key_resp_7, skip]
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
    
    # *text_14* updates
    if text_14.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
        # keep track of start time/frame for later
        text_14.frameNStart = frameN  # exact frame index
        text_14.tStart = t  # local t and not account for scr refresh
        text_14.tStartRefresh = tThisFlipGlobal  # on global time
        win.timeOnFlip(text_14, 'tStartRefresh')  # time at next scr refresh
        text_14.setAutoDraw(True)
    
    # *key_resp_7* updates
    waitOnFlip = False
    if key_resp_7.status == NOT_STARTED and tThisFlip >= 30-frameTolerance:
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
    
    # *skip* updates
    waitOnFlip = False
    if skip.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
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
        theseKeys = skip.getKeys(keyList=['q'], waitRelease=False)
        _skip_allKeys.extend(theseKeys)
        if len(_skip_allKeys):
            skip.keys = _skip_allKeys[-1].name  # just the last key pressed
            skip.rt = _skip_allKeys[-1].rt
            # a response ends the routine
            continueRoutine = False
    
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
thisExp.addData('text_14.started', text_14.tStartRefresh)
thisExp.addData('text_14.stopped', text_14.tStopRefresh)
# check responses
if key_resp_7.keys in ['', [], None]:  # No response was made
    key_resp_7.keys = None
thisExp.addData('key_resp_7.keys',key_resp_7.keys)
if key_resp_7.keys != None:  # we had a response
    thisExp.addData('key_resp_7.rt', key_resp_7.rt)
thisExp.addData('key_resp_7.started', key_resp_7.tStartRefresh)
thisExp.addData('key_resp_7.stopped', key_resp_7.tStopRefresh)
thisExp.nextEntry()
# check responses
if skip.keys in ['', [], None]:  # No response was made
    skip.keys = None
thisExp.addData('skip.keys',skip.keys)
if skip.keys != None:  # we had a response
    thisExp.addData('skip.rt', skip.rt)
thisExp.addData('skip.started', skip.tStartRefresh)
thisExp.addData('skip.stopped', skip.tStopRefresh)
thisExp.nextEntry()
# the Routine "inflam_intro" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

# set up handler to look after randomisation of conditions etc
inflam = data.TrialHandler(nReps=1.0, method='random', 
    extraInfo=expInfo, originPath=-1,
    trialList=data.importConditions('main_stims.xlsx', selection=random(3)*4 ),
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
    # update component parameters for each repeat
    text_11.setText(inflam_questions)
    key_resp_6.keys = []
    key_resp_6.rt = []
    _key_resp_6_allKeys = []
    # keep track of which components have finished
    inflam_promptComponents = [text_11, text_12, key_resp_6]
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
    while continueRoutine:
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
        
        # *text_12* updates
        if text_12.status == NOT_STARTED and tThisFlip >= 5-frameTolerance:
            # keep track of start time/frame for later
            text_12.frameNStart = frameN  # exact frame index
            text_12.tStart = t  # local t and not account for scr refresh
            text_12.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_12, 'tStartRefresh')  # time at next scr refresh
            text_12.setAutoDraw(True)
        
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
        if key_resp_6.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_6.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_6_allKeys.extend(theseKeys)
            if len(_key_resp_6_allKeys):
                key_resp_6.keys = _key_resp_6_allKeys[-1].name  # just the last key pressed
                key_resp_6.rt = _key_resp_6_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "inflam_prompt" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "discuss"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_3.keys = []
    key_resp_3.rt = []
    _key_resp_3_allKeys = []
    # keep track of which components have finished
    discussComponents = [text_7, text_8, end_discuss, key_resp_3]
    for thisComponent in discussComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    discussClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "discuss"-------
    while continueRoutine:
        # get current time
        t = discussClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=discussClock)
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
            if tThisFlipGlobal > text_7.tStartRefresh + 65-frameTolerance:
                # keep track of stop time/frame for later
                text_7.tStop = t  # not accounting for scr refresh
                text_7.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_7, 'tStopRefresh')  # time at next scr refresh
                text_7.setAutoDraw(False)
        
        # *text_8* updates
        if text_8.status == NOT_STARTED and tThisFlip >= 50-frameTolerance:
            # keep track of start time/frame for later
            text_8.frameNStart = frameN  # exact frame index
            text_8.tStart = t  # local t and not account for scr refresh
            text_8.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_8, 'tStartRefresh')  # time at next scr refresh
            text_8.setAutoDraw(True)
        if text_8.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > text_8.tStartRefresh + 15-frameTolerance:
                # keep track of stop time/frame for later
                text_8.tStop = t  # not accounting for scr refresh
                text_8.frameNStop = frameN  # exact frame index
                win.timeOnFlip(text_8, 'tStopRefresh')  # time at next scr refresh
                text_8.setAutoDraw(False)
        
        # *end_discuss* updates
        if end_discuss.status == NOT_STARTED and tThisFlip >= 65-frameTolerance:
            # keep track of start time/frame for later
            end_discuss.frameNStart = frameN  # exact frame index
            end_discuss.tStart = t  # local t and not account for scr refresh
            end_discuss.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(end_discuss, 'tStartRefresh')  # time at next scr refresh
            end_discuss.setAutoDraw(True)
        if end_discuss.status == STARTED:
            # is it time to stop? (based on global clock, using actual start)
            if tThisFlipGlobal > end_discuss.tStartRefresh + 0.5-frameTolerance:
                # keep track of stop time/frame for later
                end_discuss.tStop = t  # not accounting for scr refresh
                end_discuss.frameNStop = frameN  # exact frame index
                win.timeOnFlip(end_discuss, 'tStopRefresh')  # time at next scr refresh
                end_discuss.setAutoDraw(False)
        
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
        if key_resp_3.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_3.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_3_allKeys.extend(theseKeys)
            if len(_key_resp_3_allKeys):
                key_resp_3.keys = _key_resp_3_allKeys[-1].name  # just the last key pressed
                key_resp_3.rt = _key_resp_3_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in discussComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "discuss"-------
    for thisComponent in discussComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    inflam.addData('text_7.started', text_7.tStartRefresh)
    inflam.addData('text_7.stopped', text_7.tStopRefresh)
    inflam.addData('text_8.started', text_8.tStartRefresh)
    inflam.addData('text_8.stopped', text_8.tStopRefresh)
    inflam.addData('end_discuss.started', end_discuss.tStartRefresh)
    inflam.addData('end_discuss.stopped', end_discuss.tStopRefresh)
    # check responses
    if key_resp_3.keys in ['', [], None]:  # No response was made
        key_resp_3.keys = None
    inflam.addData('key_resp_3.keys',key_resp_3.keys)
    if key_resp_3.keys != None:  # we had a response
        inflam.addData('key_resp_3.rt', key_resp_3.rt)
    inflam.addData('key_resp_3.started', key_resp_3.tStartRefresh)
    inflam.addData('key_resp_3.stopped', key_resp_3.tStopRefresh)
    # the Routine "discuss" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "rest"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_4.keys = []
    key_resp_4.rt = []
    _key_resp_4_allKeys = []
    # keep track of which components have finished
    restComponents = [rest_text, key_resp_4]
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
    while continueRoutine:
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
        if key_resp_4.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_4.getKeys(keyList=['q'], waitRelease=False)
            _key_resp_4_allKeys.extend(theseKeys)
            if len(_key_resp_4_allKeys):
                key_resp_4.keys = _key_resp_4_allKeys[-1].name  # just the last key pressed
                key_resp_4.rt = _key_resp_4_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
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
    # the Routine "rest" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    
    # ------Prepare to start Routine "next_question"-------
    continueRoutine = True
    # update component parameters for each repeat
    key_resp_5.keys = []
    key_resp_5.rt = []
    _key_resp_5_allKeys = []
    # keep track of which components have finished
    next_questionComponents = [text_5, key_resp_5]
    for thisComponent in next_questionComponents:
        thisComponent.tStart = None
        thisComponent.tStop = None
        thisComponent.tStartRefresh = None
        thisComponent.tStopRefresh = None
        if hasattr(thisComponent, 'status'):
            thisComponent.status = NOT_STARTED
    # reset timers
    t = 0
    _timeToFirstFrame = win.getFutureFlipTime(clock="now")
    next_questionClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
    frameN = -1
    
    # -------Run Routine "next_question"-------
    while continueRoutine:
        # get current time
        t = next_questionClock.getTime()
        tThisFlip = win.getFutureFlipTime(clock=next_questionClock)
        tThisFlipGlobal = win.getFutureFlipTime(clock=None)
        frameN = frameN + 1  # number of completed frames (so 0 is the first frame)
        # update/draw components on each frame
        
        # *text_5* updates
        if text_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            text_5.frameNStart = frameN  # exact frame index
            text_5.tStart = t  # local t and not account for scr refresh
            text_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(text_5, 'tStartRefresh')  # time at next scr refresh
            text_5.setAutoDraw(True)
        
        # *key_resp_5* updates
        waitOnFlip = False
        if key_resp_5.status == NOT_STARTED and tThisFlip >= 0.0-frameTolerance:
            # keep track of start time/frame for later
            key_resp_5.frameNStart = frameN  # exact frame index
            key_resp_5.tStart = t  # local t and not account for scr refresh
            key_resp_5.tStartRefresh = tThisFlipGlobal  # on global time
            win.timeOnFlip(key_resp_5, 'tStartRefresh')  # time at next scr refresh
            key_resp_5.status = STARTED
            # keyboard checking is just starting
            waitOnFlip = True
            win.callOnFlip(key_resp_5.clock.reset)  # t=0 on next screen flip
            win.callOnFlip(key_resp_5.clearEvents, eventType='keyboard')  # clear events on next screen flip
        if key_resp_5.status == STARTED and not waitOnFlip:
            theseKeys = key_resp_5.getKeys(keyList=['space'], waitRelease=False)
            _key_resp_5_allKeys.extend(theseKeys)
            if len(_key_resp_5_allKeys):
                key_resp_5.keys = _key_resp_5_allKeys[-1].name  # just the last key pressed
                key_resp_5.rt = _key_resp_5_allKeys[-1].rt
                # a response ends the routine
                continueRoutine = False
        
        # check for quit (typically the Esc key)
        if endExpNow or defaultKeyboard.getKeys(keyList=["escape"]):
            core.quit()
        
        # check if all components have finished
        if not continueRoutine:  # a component has requested a forced-end of Routine
            break
        continueRoutine = False  # will revert to True if at least one component still running
        for thisComponent in next_questionComponents:
            if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
                continueRoutine = True
                break  # at least one component has not yet finished
        
        # refresh the screen
        if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
            win.flip()
    
    # -------Ending Routine "next_question"-------
    for thisComponent in next_questionComponents:
        if hasattr(thisComponent, "setAutoDraw"):
            thisComponent.setAutoDraw(False)
    inflam.addData('text_5.started', text_5.tStartRefresh)
    inflam.addData('text_5.stopped', text_5.tStopRefresh)
    # check responses
    if key_resp_5.keys in ['', [], None]:  # No response was made
        key_resp_5.keys = None
    inflam.addData('key_resp_5.keys',key_resp_5.keys)
    if key_resp_5.keys != None:  # we had a response
        inflam.addData('key_resp_5.rt', key_resp_5.rt)
    inflam.addData('key_resp_5.started', key_resp_5.tStartRefresh)
    inflam.addData('key_resp_5.stopped', key_resp_5.tStopRefresh)
    # the Routine "next_question" was not non-slip safe, so reset the non-slip timer
    routineTimer.reset()
    thisExp.nextEntry()
    
# completed 1.0 repeats of 'inflam'


# ------Prepare to start Routine "feedback"-------
continueRoutine = True
# update component parameters for each repeat
# keep track of which components have finished
feedbackComponents = []
for thisComponent in feedbackComponents:
    thisComponent.tStart = None
    thisComponent.tStop = None
    thisComponent.tStartRefresh = None
    thisComponent.tStopRefresh = None
    if hasattr(thisComponent, 'status'):
        thisComponent.status = NOT_STARTED
# reset timers
t = 0
_timeToFirstFrame = win.getFutureFlipTime(clock="now")
feedbackClock.reset(-_timeToFirstFrame)  # t0 is time of first possible flip
frameN = -1

# -------Run Routine "feedback"-------
while continueRoutine:
    # get current time
    t = feedbackClock.getTime()
    tThisFlip = win.getFutureFlipTime(clock=feedbackClock)
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
    for thisComponent in feedbackComponents:
        if hasattr(thisComponent, "status") and thisComponent.status != FINISHED:
            continueRoutine = True
            break  # at least one component has not yet finished
    
    # refresh the screen
    if continueRoutine:  # don't flip if this routine is over or we'll get a blank screen
        win.flip()

# -------Ending Routine "feedback"-------
for thisComponent in feedbackComponents:
    if hasattr(thisComponent, "setAutoDraw"):
        thisComponent.setAutoDraw(False)
# the Routine "feedback" was not non-slip safe, so reset the non-slip timer
routineTimer.reset()

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
