# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful

# import scraperwiki
# import lxml.html
#
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".

# coding: utf-8

# In[ ]:


import smtplib, ssl


# In[ ]:


port = 465 # for SSL


# In[ ]:


smtp_server = "smtp.gmail.com"


# In[ ]:


password = ("4Forestgreen")


# In[ ]:


# Create a secure SSL context
context = ssl.create_default_context()


# In[6]:


print("What is your name? Please type your name the format \"Lastname, Firstname.\" So for example: \"Kent, Clark\" is what you might type. \n It's important that you include your name this way exactly, with the comma in the middle, so that your grade is recorded correctly.")


# In[7]:


name = input()


# In[ ]:


Print("What is the difference between Race and Ethnicity in government data?\n
a) Race refers to a birth certificate designation, whereas race does not.\n
b) There is no difference between Race and Ethnicity.\n
c) It depends on the data set.\n
d) Ethnicity can include Hispanic and White.\n")


# In[8]:


Answer1 = input ()


# In[9]:


print("What is the average airspeed velocity of a swallow?")


# In[10]:


Answer2 = input ()


# In[11]:


sender_email = "OUDataJournalism@gmail.com"
receiver_email = "OUDataJournalism@gmail.com"
message = f"""Subject: QuizAnswers

{name}, {Answer1}, {Answer2}."""

# Send email here


# In[ ]:


context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)

