# CS 410P: Computers, Sound, and Music Term Project
### SinePiano
Authors: Angie McGraw (mangie@pdx.edu), Tu Vu (vutu@pdx.edu)

#### Project Description: 
This program allows the user to play "piano" using their mouse. The piano key tones are based on sine waves, instead of the traditional piano. Using sine waves allows users to exeperience different tones of sine waves. It also allows for reduction of the number of wav files needed for the program. There are 3 octaves: 36 notes. The base note is C3, and the following 35 notes are built on it through semitones. This program creates and uses two wav files; one for the base note and one for the generated notes. To do so, we imported Professor Massey's sampler.py. This program features an on-screen piano visual. The intended function of this program is to play simple tones on a piano keyboard using their mouse. 

#### How to Build and Run the Project
Simply "python3 sinepiano.py". This program uses: simpleaudio, tkinter, numpy, sampler, and scipy.io.wavfile. Please ensure that sampler.py is in the same directory as sinepiano.py. 

After typing in "python3 sinepiano.py", the on-screen keyboard should show up in a few seconds. Simply hit the key on the screen to hear the sine wave tone. The user can easily run through a scale, such as the major key scale, or any other scale that they wish to play. It functions like a regular keyboard, but just sounds different. 

#### Testing Done to Make Sure the Project Works
To ensure that the binding worked, we tested clicking on object out of screen. This ensured that nothing was being affected and that the keys were correctly bound. 

To ensure that the notes follow the same tone as an actual piano, we used a tuner app on our phones to confirm that the notes were what they were supposed to be. 

To ensure that the base wav and the generated wav files were in accordance with each other, we ran both in Audacity and observed the sample rate, sample time, and the image of the sample. We confirmed that these files have the same sample rate of 44100 Hz, the sample sample time of 1 second, and takes the form of a sine wave. 

#### What Worked
The most ambitious part about this project was the visuals. Both of us are not that familiar with visuals, so it took a lot of reading textbooks to figure out what components we needed and how to build those components. 

We thought of having 36 wav files of the notes recorded from the piano, however, we could not find a clean version of the keys that we wanted and neither of us had the recording capabilities to record the keys from an actual piano. So, we decided to take what we learned from class about generating sine waves and pitching them. We were unsure about using sine waves at first, but it proved to be successful once implemented. 

#### What Didn't Work
Initally, we had planned to have computer keyboard and on-screen capabilities. Mapping the computer keyboard to play sound proved to be a little harder than we thought. The complicated part was connecting the keyboard mapping to the visuals that were built. Eventually, we decided to stick to playing the piano solely on-screen through the user's mouse. 

For some reason, the sound is a little sharp through headphones, however, it sounds just fine without. 

#### Satisfaction 
In the time given and how much we have learned in this class about computers, sound, and music, we are satisfied with how much we have learned and the work we have done. 

#### Improvements
In the future, we would like to have computer keyboard playing capabilities, because we think that's cooler than just solely playing with the mouse. It would be interesting to see if we could map all 88 keys to the computer keyboard as well. 

More features could include: using actual piano sounds and adding recording capabilities. 


