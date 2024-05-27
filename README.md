Steganography Chat Application

A web-based Steganography chat application using high-level Python web framework, Django. 
Steganography embeds a secret message inside an innocent looking cover medium, stealthily, without creating any attention. The cover medium used can be a text, image, audio, video, network packets, etc. 

In this web application there are 5 main interfaces: 
        Home page
        Registration
        Login
        Dashboard for chat, encode, and decode
        Logout

This web application has features like user authentication, steganographic encoding/decoding, and secure transmission of steganographic images via mail. When users log in to our web app by providing username and password, the system authenticates the identity by comparing the provided credentials with stored credentials in its database. Once user is authenticated, user will be able to access the steganography chat application. Using encode interface, user will be allowed to upload an image and enter the text message to be hidden. Then, a new image with hidden text, steganographic image would be generated and, user could share steganography image to the person whom he/she wants to communicate via mail. Then, the other user/receiver receives the steganography image and decodes to read the hidden text. In this system, both users– the sender and the receiver are required to register and login to steganography chat application to encode and decode secret text messages. Later the user can log out.

For hiding text messages inside image, we are using Least significant bit (LSB) technique. Stepic, a Python module and a command-line interface hides arbitrary data within images using the LSB technique. Stepic module provides methods for encoding and decoding data in images.
