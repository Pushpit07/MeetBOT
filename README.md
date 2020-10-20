# MeetBOT: A Google Meet Bot

## Description
A tool that attends your Google Meet(s) for you on autopilot while you sleep or work on something else. It also disables your Meet camera & microphone in-Meet! It is also equipped with color-coded, concise activity logging with timestamps of all joining & ending activities for each Meet session.

This project is created in Python.

## Features
- Mulitple Meet sessions supported, according to the user-defined Meet schedule
- Works even with the display on sleep (and does not wake it up either)
- Works even in the background while you do other work (as long as you do not *explicitly* "Minimize" the browser window MeetNinja generates; just keep it open in the background, beneath your current open window(s))
- Color-coded & concise activity logging with timestamps of all activities
- Supported web browsers: Google Chrome

## Usage
1. Clone / Download this repository.

2. pip-install all the required packages by running `pip install -r requirements.txt` in the MeetBOT directory.

3. Do not run MeetBOT.py just yet. First, open it using any editor, and substitute your inputs (Google Meet URLs, their start times, duration of all Meets). 

4. Make a .env file in the MeetBOT directory. Set your Google email, password, path to the web driver file as specified below-

`EMAIL=Your email`

`PASSWORD=Your password`

`BROWSER_DRIVER=Path to the chromedriver`

5. Save your changes, and run the program.

### What MeetBOT Does
Upon execution, MeetNinja generates a new Google Chrome / Mozilla Firefox window in Developer Mode, and this new window stays idle until it is time to join your first Meet (according to your schedule). Once it is time, MeetNinja automatically logs you into your Google account, navigates to the first Meet URL, disables your camera & microphone, joins the Meet session, and then waits until the duration specified (60 minutes by default) before ending the call and repeating the same for the *next* Meet session (whenever it may be) and so on, until your schedule has exhausted *(phew)*