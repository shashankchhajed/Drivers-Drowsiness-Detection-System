## Driver's Drowsiness Detection

## Project Overview

This project aims to address the alarming issue of drowsy driving, a significant cause of road accidents. Using Python, I have developed a drowsiness detection system that monitors the driver's eyes in real-time, sounding an alarm if signs of fatigue are detected. By analyzing frames captured through a webcam, the system identifies the driver's irises and triggers an alert if they are not found for an extended period.

## Problem Statement

Drowsy driving is a serious concern, with statistics showing a high incidence of accidents related to driver fatigue. My goal is to create a sleepiness detection system using image processing techniques to mitigate the risks associated with drowsy driving.

## Project Logic

The core algorithm relies on Fourier Transformation, emphasizing the relationship between time and frequency. This mathematical approach helps in identifying patterns indicative of drowsiness, allowing the system to react promptly.

## Implementation Details

### Idea
The system uses a webcam to continuously capture the driver's face during a ride. A detection algorithm analyzes each frame to determine the state of the driver's eyes. If the eyes remain closed for more than 2 seconds, the system triggers an alert, effectively preventing potential accidents.

### Programming Language
The entire implementation is done in Python, leveraging its robust image processing libraries.

### Output
The system displays frames with a rectangle around the eyes for irises if detected. A buzzer sound is produced if the detected eyes are closed for an extended period.

### Steps

1. Real-time Face Detection: Extract frames from the webcam feed at a rate of 25 frames per second.

2. Dot Hough Transform: Apply Dot Hough transform on each frame to detect the nose, which subsequently helps in iris detection.

3. Rectangular Hough Transform: Utilize Rectangular Hough transform on each frame to detect the irises.

4. Blink Signal: When the eyes close, the rectangular detection shape disappears, indicating a blink. A buzzer sound is triggered if irises are not found for 50 consecutive frames.

## System Configuration

For successful drowsiness detection, manual input of parameters such as threshold and radius is essential. These parameters may vary across frames and are critical for the system's accuracy.

## Project Conclusion

My drowsiness detection system provides a proactive solution to mitigate the risks associated with driver fatigue. By leveraging image processing techniques and real-time monitoring, the system can effectively alert drivers, contributing to safer road conditions. Continuous improvement and parameter optimization are crucial for enhancing the system's accuracy and reliability.
