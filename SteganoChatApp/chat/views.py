# Create your views here

from django.http import HttpResponse                
from django.shortcuts import render, redirect
from django.contrib.auth import logout
import io
from PIL import Image
import stepic

from . forms import CreateUserForm, LoginForm                 #forms:the 'forms' module provides easy way to create HTML forms and handle form data.

from .forms import EmailwithattachmentForm
from .models import Emailwithattachment       #Email form

from django.contrib.auth.decorators import login_required     #django.contrib.auth.decorators import login_required:It is used to secure views in your web applications by forcing the client to authenticate with a valid logged-in User.


# - Authentication models and functions

from django.contrib.auth.models import auth      #auth:the 'auth' module provides built-in function functionality for handling user authentication,including user login,logout,password management and user permissions.
from django.contrib.auth import authenticate, login, logout

# Email SMTP and MIME

import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

#path

import os
from django.conf import settings
from pathlib import Path

from SteganoChatApp.settings import BASE_DIR

#HOME PAGE
def homepage(request):                           #request:When a page is requested, Django creates an HttpRequest object that contains metadata about the request. Then Django loads the appropriate view, passing the HttpRequest as the first argument to the view function. Each view is responsible for returning an HttpResponse object.

    return render(request, 'chat/index.html')    #render:It is a shortcut method that combines several common steps in the view layer of a web application. The primary purpose of render() is to take a request, a template, and a dictionary of context data and return an HTTP response with the rendered HTML content. 

#REGISTRATION FORM
def register(request):

    form = CreateUserForm()                          #CreateUserForm:It is used for creating a new user that can use our web application. It has three fields: username, password1, and password2(which is basically used for password confirmation).

    if request.method == "POST":

        form = CreateUserForm(request.POST)

        if form.is_valid():                          #is_valid():When a form is submitted in Django, it is validated by calling the is_valid() method on the form instance. This method returns True if all fields are valid and False otherwise.

            form.save()                              #save():The save() method returns the instances that have been saved to the database.

            return redirect("my-login")


    context = {'registerform':form}

    return render(request, 'chat/register.html', context=context)

#LOGIN FORM
def my_login(request):

    form = LoginForm()

    if request.method == 'POST':

        form = LoginForm(request, data=request.POST)

        if form.is_valid():

            username = request.POST.get('username')
            password = request.POST.get('password')

            user = authenticate(request, username=username, password=password)

            if user is not None:

                auth.login(request, user)

                return render(request, 'chat/dashboard.html') 

    context = {'loginform':form}

    return render(request, 'chat/my-login.html', context=context)

#DASHBOARD
@login_required(login_url="my-login")
def dashboard(request):

    return render(request, 'chat/dashboard.html')


#HOME
@login_required(login_url="my-login")
def home(request):

    return render(request, 'chat/home.html')


#CHAT PAGE
@login_required(login_url="my-login")
def chatpage(request):
    if not request.user.is_authenticated:
        return redirect("my-login")              #redirect:Used to redirect the user to a different URL.
    context = {}                                 #context:Used within views to pass data to a template.Allows to send variables from the view to the template.
    #return render(request, 'chat/chatpage.html', context=context)   Hema commented

    #return render(request, 'chat/chatwindow.html', context=context)    Hema commented

    return redirect("email")


#STEGANOGRAPHY - ENCODE AND DECODE

def hide_text_in_image(image, text):
    data = text.encode('utf-8')
    '''encode('utf-8') on a string, it translates the human-readable 
    characters into a sequence of bytes using the UTF-8 encoding.
     The result is a bytes object in Python.'''
    return stepic.encode(image, data)
#stepic.encode method is called to hide these bytes within the image

@login_required(login_url="my-login")
def encode_view(request):
    message = ''
    if request.method == 'POST':
        text = request.POST['text']
        image_file = request.FILES['image']
        image = Image.open(image_file)

        # Convert to PNG if not already in that format
        if image.format != 'PNG':  # checks whether the image format is not PNG.
            image = image.convert('RGBA')
            # image is converted to RGBA mode if it's not already
            # This ensures the image has the correct color channels.
            buffer = io.BytesIO()
            # A BytesIO object is created,
            # which is a binary stream (an in-memory bytes buffer).
            image.save(buffer, format="PNG")
            image = Image.open(buffer)

        # hide text in image
        new_image = hide_text_in_image(image, text)

        # save the new image in a project folder
        image_path = 'media/stegano_images/' + 'new_' + image_file.name
        new_image.save(image_path, format="PNG")

        message = 'Stegano image is generated, Check stegano images folder'

    return render(request, 'chat/encode.html', {'message': message})

@login_required(login_url="my-login")
def decode_view(request):
    text = ''
    if request.method == 'POST':
        image_file = request.FILES['image']
        image = Image.open(image_file)

        # Convert to PNG if not already in that format
        if image.format != 'PNG':#checks whether the image format is not PNG.
            image = image.convert('RGBA')
            #image is converted to RGBA mode if it's not already
            #This ensures the image has the correct color channels.
            buffer = io.BytesIO()
            #A BytesIO object is created,
            # which is a binary stream (an in-memory bytes buffer).
            image.save(buffer, format="PNG")
            image = Image.open(buffer)

        # extract text from image
        text = extract_text_from_image(image)

    return render(request, 'chat/decode.html', {'text': text})


def extract_text_from_image(image):
    data = stepic.decode(image)
    # uses the decode function from the stepic library to extract the
    # hidden data from the given image. This hidden data is
    # typically stored as bytes.
    if isinstance(data, bytes):
        return data.decode('utf-8')
    return data


#SENDING STEGANO IMAGE THROUGH EMAIL

@login_required(login_url="my-login")
def email_attatchment_send(request):
 
    if request.method == 'POST':
        form = EmailwithattachmentForm(request.POST, request.FILES)

        if form.is_valid():
            form.save()
            sender = request.POST.get('sender_email_address')
            password = request.POST.get('sender_email_password')
            receivername = request.POST.get('receiver_name')
            receiver = request.POST.get('receiver_email_address')
            steganoimagefile = request.FILES['stegano_image']
            print("CURRENT WORKING DIR", os.getcwd())
            print(steganoimagefile)
            print("PATH: ", os.path.abspath(steganoimagefile.name))

            message = MIMEMultipart()
            message['From'] = sender
            message['To'] = receiver
            message['Subject'] = "Hi " + receivername + ", New Media file"

            body = "Images speak better than words"
            message.attach(MIMEText(body, 'plain'))

            #msg.attach_file(os.path.join(BASE_DIR, 'static', 'file.file'))
            filename = os.path.join(BASE_DIR, 'media/stegano_images/', steganoimagefile.name)            
            #filename = os.path.abspath(steganoimagefile.name)
            print("FILE NAME PASSED TO open(): ", filename)
            #with open('geeks / upload/'+f.name, 'wb+') as destination: 
            with open(filename, 'rb') as file:
                attachment = MIMEApplication(file.read(), _subtype = 'jpeg')
                attachment.add_header('content-Disposition', 'attachment', filename=steganoimagefile.name)
                message.attach(attachment)

            #with smtplib.SMTP('smtp.gmail.com', 465) as smtp:\
            email_smtp = "smtp.gmail.com"
            smtp = smtplib.SMTP(email_smtp, '587')
            smtp.ehlo()
            smtp.starttls()
            smtp.login(sender, password)
            smtp.send_message(message)
            smtp.quit()

            message = "Click send button to send another stegano image via email"

            return render(request, 'chat/email.html', {'message': message})
 
    else:
        form = EmailwithattachmentForm()
    return render(request, 'chat/email.html', {'form': form})
 
 
#LOGOUT
def logout_user(request):

    logout(request)
    print("logout")
    return render(request, 'chat/logout-user.html')
