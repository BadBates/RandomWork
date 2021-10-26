import praw
import re
import time

reddit = praw.Reddit(client_id= 'uvARHIHEMMykx6',
                client_id= 'kK1NgMo4C8amNpnTDQEJ6_LJYzs',
                user_agent= '<console:Reddit_Bot:0.0.1 (by /u/BadBates)>'
                username= 'BadBates',
                password= 'Snow36Board')
                
subreddit = ['Powered_People']
posts = 0  
comments = 0

url = "https://www.reddit.com/r/Powered_People/"

def highlight():
    global subreddit
    global posts
    global comments
    
    subreddit - reddit.subreddit([posts])
    subreddit.submit(title, url=url)
   
   if(posts ==  '..?..'):        #pixel [r,g,b]= img.getpixel((x,y))
        
    
        