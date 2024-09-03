
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
#### Programming PLC
#### Arduino code
#### Python script for voice processing
#### Python script for connecting PLC to server
#### Python script to receive .wav file from FSBrowser and send it server

## How to Run

In this part, you should provide instructions on how to run your project. Also if your project requires any prerequisites, mention them. 

#### Examples:
#### Build Project
Your text comes here
```bash
  build --platform=OvmfPkg/OvmfPkgX64.dsc --arch=X64 --buildtarget=RELEASE --tagname=GCC5
```

#### Run server
Your text comes here
```bash
  pyhton server.py -p 8080
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `-p` | `int` | **Required**. Server port |



## Results
In this section, you should present your results and provide an explanation for them.

Using image is required.

## Related Links
Some links related to your project come here.
 - [EDK II](https://github.com/tianocore/edk2)
 - [ESP32 Pinout](https://randomnerdtutorials.com/esp32-pinout-reference-gpios/)
 - [Django Doc](https://docs.djangoproject.com/en/5.0/)


## Authors
Authors and their github link come here.
- [@Author1](https://github.com/Sharif-University-ESRLab)
- [@Author2](https://github.com/Sharif-University-ESRLab)

