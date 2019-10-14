#!/usr/bin/env python3
# Original file by Adept-, link below:
# https://github.com/Adept-/crankyblogger
import json
import webbrowser
import os.path
import argparse
import httplib2
from oauth2client import client
from apiclient.discovery import build
from oauth2client.file import Storage

with open("my_blog.json") as json_file:
    data = json.load(json_file)

# Defining argparse and flags, below are the locks to prevent the script from continuing
parser = argparse.ArgumentParser(description="This script can upload documents to our blogspot blog, refer to the flags below for more information")
parser.add_argument("-d","--debug", help="Debug application, set to 1 for debuging, default 0", 
    default=0, type=int, dest="debug")
parser.add_argument("-f","--file", help="File to be uploaded", 
    dest="file_upload")
parser.add_argument("-t","--title", help="Title of the blog post", default=data["defaultTitle"],
    dest="title")
parser.add_argument("-l","--label", help="Labels for blog, these need to be comma separated", 
    default=data["defaultLabels"], dest="label")
parser.add_argument("-p","--publish", 
    help="Publish file immediately, set to 1 to publish, default is set to 0,", 
    dest="publish", default=0, type=int)
flags = parser.parse_args()
 
# Cruise control for Cool
if flags.file_upload:
    file_upload = flags.file_upload
else:
    print("[X] File required in order to create post, ending program")
    exit()
if flags.title == data["defaultTitle"]:
    while True:
        question_1 = input("[!] Default title being used, do you wish to change it? [Y/N] ")
        if question_1.lower() in ["n","no"]:
            print("[!] Default title is being used")
            blog_title = flags.title
            break
        elif question_1.lower() in ["y","yes"]:
            blog_title = input("New title for blog post: ")
            break
if flags.label:
    labels = flags.label

# If there is no userkey authenticate with Google and save the key.
if(os.path.exists('userkey') == False):
    flow = client.flow_from_clientsecrets('client_id.json',
            scope='https://www.googleapis.com/auth/blogger',
            redirect_uri='urn:ietf:wg:oauth:2.0:oob'
            )

    auth_uri = flow.step1_get_authorize_url()
    webbrowser.open_new(auth_uri)
    auth_code = input('Enter the auth code: ')
    credentials = flow.step2_exchange(auth_code)
    http_auth = credentials.authorize(httplib2.Http())

    # Store the credentials
    storage = Storage('userkey')
    storage.put(credentials)

# If the userkey already exists use it.
else:
    storage = Storage('userkey')
    credentials = storage.get()
    http_auth = credentials.authorize(httplib2.Http())

# Initialize the blogger service and get the blog
blogger_service = build('blogger', 'v3', http=http_auth)

# Open file for reading
try:
    f = open(file_upload, 'r')
except Exception as e:
    print("Error open file. Aborting, see error below:\n")
    print(e)
    exit()

#build a label list
labels_list = labels.split(',')

#build body object
body = {
        "content": f.read(),
        "title": blog_title,
        "labels": labels_list
        }
#Insert the post
try:
    post = blogger_service.posts().insert(blogId=data["blogId"], body=body, isDraft=bool(data["postFile"])).execute()
except Exception as e:
    print("[X] Something went wrong uploading this post, check the error below\n")
    print(e)
    exit()

print("Title: %s" % post['title'])
print("Is Draft: %s" % bool(data["postFile"]))
if(bool(data["postFile"]) == False):
    print("URL: %s" % post['url'])
print("Labels: %s" % post['labels'])