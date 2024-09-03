
![Untitled design (1) (2)](https://github.com/user-attachments/assets/501c571e-d38d-446e-85cd-96618305d61d)


# Project Title

AI voice assistant to manage PLC and HMI panels.
This project is aiming to assist people who are not familiar with PLC tags. 
A person can simply press a button and start talking into a microphone and ask what they want to do and the task is automatically done. (if it's previously programmed and defined in the PLC)

## Tools
- INMP441 microphone
- S7-1200 PLC (In our case we used TIA Portal)
- ESP32 microcontroller
- Any micro SD card slot module and a SD card(preferred)
- I2S Stereo Decoder (UDA1334A), if you need a real-time feedback from LLM. 


## Implementation Details

Our implementation consists of 5 parts:
#### Programming PLC:
First we wrote a simple program in Ladder that has 3 tags "turn_on_light", "turn_off_light" and "light"

#### Arduino code:
For our arduino program we wrote a code that gets the input audio from INPM441 microphone, makes a .wav file and uploads it on FSBrowser so we can download it in the server.

#### Python script for voice processing:
In the server side we have a python script that receives the wav file, converts the audio to text using gstt library then makes the a Chat-gpt prompt and sends the prompt to chat-gpt via Openai API and extracts the PLC command from it then makes an audio file using gtts to read the feedback for user.

#### Python script for connecting PLC to server:
We also connect to PLC via ethernet which is implemented in this script.

#### Python script to receive .wav file from FSBrowser and send it server:
This script downloads the .wav file from FSBrowser and sends it to server.


## How to Run
First you have to connect the ESP32 to your PC and upload the .ino file to it. After you successfully uploaded the code in Arduino IDE you'll see that your voice is getting recorded for 15 seconds. When it's done you'll see an url which your .wav file is available on. Copy the url and replace it with the value of "audio_url" in the Client code.
Now you have to run the server. Navigate to the directory which you have your Server.py file and run the following command in cmd:
```bash
  pyhton Server.py
```
then copy the server ip and port and replace it with the "SERVER_URL" value in the Client code.
Open another cmd, navigate to Client.py directory and run this command and follow the instruction:
```bash
  pyhton Client.py
```
Now you have to find the PLC ip address in your network and replace it with the value of "ip" in Connecting_to_plc file and run the script.
Your voice assistant is ready to use. From now on all you have to do is press the EN button on the EPS32, start talking and do the Client instruction.(download and send)

## Results
In Arduino IDE:

![image](https://github.com/user-attachments/assets/f67ce5ca-5c2c-41f5-bba0-47f0af7ad277)

In Client:

![image](https://github.com/user-attachments/assets/880bbb39-0039-45f1-beda-4bdb82c61acc)

In Server:

![image](https://github.com/user-attachments/assets/c35b4913-de9e-49c3-a0e7-b7c7120e1132)

Audio files you're expected to see:

![image](https://github.com/user-attachments/assets/ef881693-a367-40e4-886e-4d0971965bca)


## Related Links
Some links related to your project come here.
 - [INMP441 Pinout](https://invensense.tdk.com/wp-content/uploads/2015/02/INMP441.pdf)
 - [ESP32 Pinout](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)
 - [flask Doc](https://flask.palletsprojects.com/en/3.0.x/)


## Authors
Authors and their github link come here.
- [@Sina Moshtaghyun](https://github.com/Sina-Moshtaghyun)
- [@Arefe Boushehrian](https://github.com/ArefeBoushehrian)
- [@Hamidreza Alipour](https://github.com/hamidalipour)

