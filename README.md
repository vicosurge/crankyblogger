#Cranky Blogger CLI

This script interacts with the Google Blogger API V3. Its purpose is to enable
command line blog posting. Flags can be used as follows

1. -f, --file "Filename" - Points to the file to be uploaded
2. -p, --publish - Indicates if the post is to be published or not, default is no
3. -t, --title - Title of the blogpost
4. -l, --label - Labels to be used for the post, use commas to separate them

Before you can run the program you will need to login into the google API
console setup an app and download a blogger key. Put the .json file in the same
directory as the script.

When you first run the program a web browser will launch and you will give the
app permission to access your blogger account.

Don't forget to edit the following configurable variables, these can be
found in the my_blog.json file

1. blogId - The id of your blog, this is required to post
2. postFile - By default this is set as False, so the post will be set as draft,
if set as True then the post will always be sent to your blog
3. defaultTitle - The default title to use if one is not specified
4. defaultLabels - defaults are used when no labels are given on CLI

#TIPS
1. You can use html2text to view the post in the command line 
2. or simply fire it up in a browser to see if formating is correct.
3. Don't forget to use the spellcheck in your editor :)
4. Your post should be a plain html file
5. Please enjoy and I welcome public contributions!

#TODO
Implement editing and deleting of blog posts

#LICENSE
Do what ever you want with it. No WARRANTY. If you share a copy with someone
else, it must be under the same license.
