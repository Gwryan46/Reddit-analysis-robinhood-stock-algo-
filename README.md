# README
This program uses praw to parse through all the subreddits looking for keywords. 
In my case I used the company Moderna since I noticed the price of this stock was heavily based on news. 
Therefore, I have created a program that first searches all the subreddits for the keyword Moderna in the title of posts. Then it searches through those titles for the keywords "Phase 3 + Approved" or "Phase 3 + Rejected". 
If it finds "Moderna" and "Phase 3 + Approved" all in the same title then it executes a buy market trade on robinhood. 
If it finds "Moderna" and "Phase 3 + Rejected" all in the same title then it executes a sell at market trade on robinhood.

Before any trade is executed it sends a notification to your devices requestion confirmation of the trade. 
Enter "yes" or "no" in the active shell to execute trade 
