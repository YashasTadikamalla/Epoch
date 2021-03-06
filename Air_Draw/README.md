<strong>Air_Draw</strong> is a simple, yet cool tool that takes in feed from your webcam, and enables you to draw on air with your index finger, while allowing you to choose various features, like colours, thickness, etc.

I got to learn and work with modular programming, OpenCV and MediaPipe frameworks as a part of this project.

<strong>How to use Air Draw?</strong>

The key idea is to detect the tips of index and middle finger of a hand, and use that data to allow one switch to choose or draw mode.

You are in drawing mode when only your index finger is up. Your index finger's tip would act like the paint brush. The circular cursor colour will indicate the brush colour currently selected.

When you want to select a particular feature, you have to open both your index and middle fingers, and join them. Then, you will have to hover the circular cursor on the desired feature.

You also have an eraser in case you want to remove a certain portion of your drawing.

Once you are done drawing, you can save your image by hovering your two fingers on "Save".
To clear the screen, you have to hover on "Clear All".

The most interesting feature of this is that, you can choose your background. It can either be a live background, or a simple black canvas.

![Demo Image](https://github.com/YashasTadikamalla/Epoch/blob/main/Air_Draw/Demo.png)

<strong>How does Air Draw work?</strong>

Hand Track Module has the code to identify hands in a frame, detect and return information related to landmark positions, status of fingers, and marking them if required.

Air Draw Module imports the Hand Track module, modifies the output frame accordingly. It has code to draw curves, switch between drawing and selection mode, erase, and save the drawings.

draw.py is the final code snippet which can be run, once this repo is pulled into your local machine, to get started with drawing!

![Saved Image](https://github.com/YashasTadikamalla/Epoch/blob/main/Air_Draw/Saved.jpg)

This project is inspired from [link](https://youtu.be/ZiwZaAVbXQo)
