# LINGUA
---
![Homepage view 1](https://github.com/user-attachments/assets/6bda9ca0-0276-436b-9940-7490677a062a)


 L: Live – Real-time translation of ISL into text and speech. <br/>
<br/>
 I: Interpretation – Accurate recognition and interpretation of Indian Sign Language. <br/>
<br/>
 N: Narration – Providing speech output in multiple Indian languages. <br/>
<br/>
 G: Gesture – Recognizing and processing hand gestures and signs. <br/>
<br/>
 U: Understanding – Facilitating communication and understanding between the deaf/hard-of-hearing and the hearing world. <br/>
<br/>
 A: Accessibility – Making communication more accessible for the deaf and hard-of-hearing community. <br/>
<br/>

Indian Sign Language to Text/Speech translation (For SIH2024)
-
P.S : To create a solution that translates Indian Sign Language (ISL) into text and speech in real-time, facilitating communication for the deaf and hard-of-hearing community with the hearing world. <br/> 
<br/>
The application is capable of recognizing and interpreting a comprehensive library of ISL signs and gestures, and then provide accurate text and speech output in multiple Indian languages.



Proposed solution for round 1 internal hackathon (SIH2024)
-
A smart glove, that's capable of sensing the motion made by the fingers, through the flex sensor / gyroscopic(axis) sensor
-

Data workflow
-

![WhatsApp Image 2024-09-05 at 12 45 25_5f6d03d0](https://github.com/user-attachments/assets/54b9f4be-b438-4aa9-9799-7afbba3dd963)


Pin Diagram:-
-
![WhatsApp Image 2024-09-05 at 13 25 26_88a407de](https://github.com/user-attachments/assets/35bf75df-062b-40f5-8ca1-7d63e7a7a197)


Hardware techstack:-
-
![WhatsApp Image 2024-09-05 at 12 54 25_d4890245](https://github.com/user-attachments/assets/d97ce190-6987-416c-9a9c-f0f36cd8273a)

![navigation view 1](https://github.com/user-attachments/assets/247e25a2-e5a6-4736-882a-5a49c5a0063b)

ISL Replica testing (Video) //ML model
-
//we used the asl architecture, fwd to training the model from scratch, giving out images, collecting the dataset ourselves and training it, after collecting 200 samples for each character
-

//work in progress
......... //put isl working video demo here, later

Hardware implementation (physical video) 
-
//work in progress
.........//put smart glove video here later

Tinkercad Virtual Simulation setup could be accessed here, developed as part of the ideathon for prototyping:-
-
=>Single flex sensor model for gesture recognition..
-
![WhatsApp Image 2024-09-02 at 23 03 22_1cf5d9bc](https://github.com/user-attachments/assets/378b6deb-11a3-48fc-9a95-9d384d783845)
Code
-
![WhatsApp Image 2024-09-02 at 23 01 43_2547976b](https://github.com/user-attachments/assets/ece06c52-ad3e-4211-a653-f5eda93a0805)
<br/>
in the serial monitor look for the variable value changes, acc to the code, if the values scales down below 150, then the display should redirect a different text, that's achieved in the simulation, as well <br/>

Access it here: https://www.tinkercad.com/things/3wKFPwO7Ksr-single-flex-sensor-recognition-system-prototypedesign

=>same thing we have tried replicating for 5 sensors, coz we're making it for a hand glove, that senses the 5 fingers ryt, and to check if it achieves multiple request driven access at the same time
-

Access it here: https://www.tinkercad.com/things/9aipFft7qlW-copy-of-flex-and-lcd
<br/>

American Sign Language Code architecture testing:- (checking the media pipe algorithm, Computer vision, NLP Suggestions, Text output, Text output to speech through various TTS models, like gTTS) <br/>
-
//in plans to achieve a similar output with ISL Software, cross checking all the dependencies..<br/>
-

https://github.com/user-attachments/assets/618fc4ac-aba9-44da-8c69-c3c5e13a91da



Future aspects (explaining it on a layman's view, keeping it completely non technical) <br/>
-

=> Smart wearable gloves that facilitates wireless connection via a bluetooth external device (in that case go for raspberry pi, instead of arduino) <br/>
=> Smart wearable glasses, that displays text as running words coming from both the text generation, as well as the NLP suggestion <br/>
=> Achieving Corpus in sign language, checking grammar, punctuation, stop word removal and removing ambiguities (syntactic parsing), in NLPs...(Usually happens after the data preprocessing step, in Model training) <br/>
=> Acheiving TTS model training epochs from scratch, instead of calling API calls only to get the robotic AI voices from Chatgpt, OpenAI, and other software sources like seamless and lovo ai, though the latter helping us to leverage voice integration modules of humanised vocal versions..<br/>
<br/>
//smtg to look out👀 (Developer resources, that i found useful) <br/>
https://lovo.ai/ <br/>
https://genny.lovo.ai/signup  <br/>
genny api setup <br/>
<br/>
![WhatsApp Image 2024-09-04 at 22 21 53_efd85b5b](https://github.com/user-attachments/assets/544b895e-7c69-4dde-899f-60e05679a0ba) <br/>

A sample tutorial could be accessed here (we took some references):-
-

https://lovo.ai/tutorials/using-genny-api/getting-started-with-genny-api

at 2:00 of this video: https://www.youtube.com/watch?v=jQ3ut_pwQFI , you can see that you can mint your own voice using nfts and upload it to the platform, thereby humanizing the ai voice through voice cloning, and there are different voices of various people that's publicly accessible with different voices for different emotions, such as happy, sad, etc..,








