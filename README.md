# lemon-newsletter-portfolio 🍋 💹

This is the complete codebase to get you email newsletter up and running on your local machine.
But we want to deploy it on heroku as well in order to automatically receive emails


The deployment process goes as follows:

1. register on heroku https://heroku.com/
1. download the Heroku CLI https://devcenter.heroku.com/articles/heroku-cli
2. create a new app using the heroku dashboard
4. in your terminal move to your project directory
5.then write: 

    $ heroku login
    
    $ heroku git:remote -a your-app-name
    
    $ git add .
    $ git commit -am "make it better"
    $ git push heroku master (or main, depending on which branch you are)
    
    
  when that's finished you should see a message saying:
  
  remote: Verifying deploy... done.
  To https://git.heroku.com/david-trial-1.git (here of course it says your app)
  * [new branch]      main -> main (here it says your branch, in my case it was the main branch)


6. on your heroku dashboard, inside your app go to "ressources"
7. search for "Heroku Scheduler"
8. click confirm and click the link leading to the "Heroku Schedule" Dashboard
9. click "add Job"
10. choose an time interval
11. in "run command" put in the command "Heroku Scheduler has to perform"
    in our case we want to write "python3 run.py" to start our application
    
12. That's it. You should receive an Email at the Interval you chose



Want to learn more about lemon.markets and how to use our cool API🍋 


Have any problems? No biggie, we've all been there. Join our aweseome Slack community 🤝 🥳

