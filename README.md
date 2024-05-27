Steganography Chat Application

A web-based Steganography chat application using high-level Python web framework, Django. 
Steganography embeds a secret message inside an innocent looking cover medium, stealthily, without creating any attention. The cover medium used can be a text, image, audio, video, network packets, etc. 

In this web application there are 5 main interfaces: Home page, Registration, Login, Dashboard for chat, encode, and decode, Logout.

This web application has features like user authentication, steganographic encoding/decoding, and secure transmission of steganographic images via mail. When users log in to our web app by providing username and password, the system authenticates the identity by comparing the provided credentials with stored credentials in its database. Once user is authenticated, user will be able to access the steganography chat application. Using encode interface, user will be allowed to upload an image and enter the text message to be hidden. Then, a new image with hidden text, steganographic image would be generated and, user could share steganography image to the person whom he/she wants to communicate via mail. Then, the other user/receiver receives the steganography image and decodes to read the hidden text. In this system, both users– the sender and the receiver are required to register and login to steganography chat application to encode and decode secret text messages. Later the user can log out.

For hiding text messages inside image, we are using Least significant bit (LSB) technique. Stepic, a Python module and a command-line interface hides arbitrary data within images using the LSB technique. Stepic module provides methods for encoding and decoding data in images.

SCREENSHOTS

Homepage Interface

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/169e590a-65b7-4aa7-a5b3-55498248c8ec)

Register Interface

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/44e4deb4-c27c-4d5d-8377-096040c14f2e)

Login Interface

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/27424de0-1c56-4b63-bf37-93a045d52c4d)
![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/d8c9f896-ee30-405d-969c-25fa946e031c)

User Dashboard 

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/253dc2ab-7d32-4292-9656-bf62013bb757)

User Dashboard- Home Interface

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/df74131b-f573-401c-a4a5-2a331545c5d7)

User Dashboard- Encode Interface

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/5f9b6714-25f3-4c5f-8b01-c50a692525a8)
![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/d8dbba74-536c-48e5-9fab-ccdf47ed8046)
![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/f83b0b36-9b40-4f56-b831-3c77e6873d8c)


User Dashboard- Chat Interface

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/5f3a0629-ad72-4e9b-acbc-e058d9908df9)
![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/13847b4f-438e-4ad9-b41b-0ef6d9c8cb6a)
![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/216010af-b1e2-4cbe-ab3a-75f23befb324)

Receiver’s Mail

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/71408afd-6951-431c-9ffe-97ec5a2a09cd)

Decode Interface

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/643f94ae-b26b-4c6a-a07e-611fadce1c52)
![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/d20c21e3-fd33-4b7d-805d-af9dc7dca810)
![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/df528b0b-cae1-4d01-b9b7-9ff803a59eaf)
![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/3892659a-7413-44df-8231-dcb541456c2c)

Logout Interface

![image](https://github.com/Hemagowdham/SteganoChatApp/assets/161472590/55e1cee4-cae7-4869-914f-8800b2087931)

