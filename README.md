<p align="center">
  <img src="https://github.com/user-attachments/assets/6bda9ca0-0276-436b-9940-7490677a062a" height="400"/>
</p>

# LINGUA

#### L: Live – Real-time translation of ISL into text and speech.
#### I: Interpretation – Accurate recognition and interpretation of Indian Sign Language.
#### N: Narration – Providing speech output in multiple Indian languages.
#### G: Gesture – Recognizing and processing hand gestures and signs.
#### U: Understanding – Facilitating communication and understanding between the deaf/hard-of-hearing and the hearing world.
#### A: Accessibility – Making communication more accessible for the deaf and hard-of-hearing community.

## Indian Sign Language to Text/Speech Translation (For SIH2024)

__Problem Statement__: To create a solution that translates Indian Sign Language (ISL) into text and speech in real-time, facilitating communication for the deaf and hard-of-hearing community with the hearing world.

The application is capable of recognizing and interpreting a comprehensive library of ISL signs and gestures, and then provide accurate text and speech output in multiple Indian languages.

### Proposed Solution for Round 1 Internal Hackathon (SIH2024)

A smart glove, that's capable of sensing the motion made by the fingers, through the flex sensor / gyroscopic(axis) sensor.

## Team Members (GenX H4CK3RS!)

Jayadithya G  <br/>
U Pranov Shanker <br/>
Adhithya Srivatsan <br/>
Harini A <br/>
Rohit K Manoj <br/>
Ankith A <br/>

## Data Workflow

<p align="center">
  <img src="https://github.com/user-attachments/assets/54b9f4be-b438-4aa9-9799-7afbba3dd963" />
</p>

## Pin Diagram

<p align="center">
  <img src="https://github.com/user-attachments/assets/35bf75df-062b-40f5-8ca1-7d63e7a7a197" />
</p>

## Hardware Techstack

<p align="center">
  <img src="https://github.com/user-attachments/assets/d97ce190-6987-416c-9a9c-f0f36cd8273a" />
</p>

## Software Techstack

<p align="center">
  <img src ="https://github.com/user-attachments/assets/926c8e4a-6706-4fba-94b6-ac2ff7304b11" />

</p>

## ISL Replica Testing (Video) - ML model

We used the asl architecture, fwd to training the model from scratch, giving out images, collecting the dataset ourselves and training it, after collecting 200 samples for each character._

_*Work in progress. Put ISL working video demo here later_

## Hardware Implementation (Physical Video) 

_*Work in progress. Put smart glove video here later_

## Tinkercad Virtual Simulation Setup (Developed as part of the Ideathon for Prototyping)

### Single Flex Sensor Model for Gesture Recognition..

<p align="center">
  <img src="https://github.com/user-attachments/assets/378b6deb-11a3-48fc-9a95-9d384d783845" />
</p>

### Code
<p align="center">
  <img src="https://github.com/user-attachments/assets/ece06c52-ad3e-4211-a653-f5eda93a0805" />
</p>

- In the serial monitor look for the variable value changes, acc to the code, if the values scales down below 150, then the display should redirect a different text, that's achieved in the simulation, as well.
- Access it here: https://www.tinkercad.com/things/3wKFPwO7Ksr-single-flex-sensor-recognition-system-prototypedesign
- Same thing we have tried replicating for 5 sensors, because we're making it for a hand glove, that senses the 5 fingers and to check if it achieves multiple request driven access at the same time.
- Access it here: https://www.tinkercad.com/things/9aipFft7qlW-copy-of-flex-and-lcd

## American Sign Language Code Architecture Testing

#### Checking the media pipe algorithm, Computer vision, NLP Suggestions, Text output, Text output to speech through various TTS models, like gTTS

https://github.com/user-attachments/assets/618fc4ac-aba9-44da-8c69-c3c5e13a91da

_*In plans to achieve a similar output with ISL software..._

# Future Aspects
#### Explaining it on a layman's view, keeping it completely non technical,

- Smart wearable gloves that facilitates wireless connection via a bluetooth external device (in that case go for raspberry pi, instead of arduino) <br/>
- Smart wearable glasses, that displays text as running words coming from both the text generation, as well as the NLP suggestion <br/>
- Achieving Corpus in sign language, checking grammar, punctuation, stop word removal and removing ambiguities (syntactic parsing), in NLPs...(Usually happens after the data preprocessing step, in Model training) <br/>
- Acheiving TTS model training epochs from scratch, instead of calling API calls from a pre-trained model, only to get the robotic AI voices from Chatgpt, OpenAI, and other software sources like seamless and lovo ai, though the latter helping us to leverage voice integration modules of humanised vocal versions..
  
#### Something to look out👀 for (Developer resources, that I found useful)
- https://lovo.ai/
- https://genny.lovo.ai/signup
- Genny api setup
<p align="center">
  <img src="https://github.com/user-attachments/assets/544b895e-7c69-4dde-899f-60e05679a0ba" />
</p>

## A sample tutorial could be accessed here
#### We took some references
https://lovo.ai/tutorials/using-genny-api/getting-started-with-genny-api

At 2:00 of this [video](https://www.youtube.com/watch?v=jQ3ut_pwQFI), you can see that you can mint your own voice using nfts and upload it to the platform, thereby humanizing the ai voice through voice cloning, and there are different voices of various people that's publicly accessible with different voices for different emotions, such as happy, sad, etc...

---

<p align="center">
  <img src="https://github.com/user-attachments/assets/247e25a2-e5a6-4736-882a-5a49c5a0063b" />
</p>

---
