

<h1 align="center"><a href="https://galetos-orderapp-pp4-1411404b0904.herokuapp.com/" target="_blank">Galeto's</a></h1> 

Galeto's a Django/Python developed order app that was desinged for a friend of mine who sells roasted chicken and needed some sort of simple looking ordering/booking systems for their clients to be able to order in advance their roasted chicken, and collect best time suited. The app meets all the needs of their business and help them to organise better their future sales and avoid waste.

[**Link to Galeto's App Live **](https://galetos-orderapp-pp4-1411404b0904.herokuapp.com/)

![Alt text](static/media/images/hero-image.png "Hero image for Readme File")

# Contents

- [Contents](#contents)
  - [User Experience (UX)](#user-experience-ux)
    - [User Stories](#user-stories)
  - [Features](#features)
    - [Landing Play Page](#landing-play-page)
    - [Welcome Message](#welcome-message)
    - [Main Menu](#main-menu)
    - [Rules Menu Option](#rules-menu-option)
    - [Credits Menu Option](#credits-menu-option)
    - [Start Game Menu Option](#start-game-menu-option)
    - [Selected Valid Option](#selected-valid-option)
    - [Comparing Computer vs User choices](#comparing-computer-vs-user-choices)
    - [Tied Round](#tied-round)
    - [Game Over](#game-over)
    - [Hidden Features](#hidden-features)
    - [Future Features](#future-features)
  - [Testing](#testing)
    - [Bugs and Issues](#bugs-and-issues)
  - [Technologies Used](#technologies-used)
  - [Deployment](#deployment)
  - [Credits](#credits)
    - [Content](#content)
    - [Media](#media)
  - [Acknowledgments](#acknowledgments)
- [THANK YOU!](#thank-you)

___


## User Experience (UX)

  ### User Stories

<br>    i.   As a Site User I can register an account so that create, read, update and delete orders
<br>    ii.  As a site user I can create orders on database so that have a order created
<br>    iii. As a Site user I can view the orders I created so that manage the orders
<br>    iv.  As a site user I can edit my orders so that modify the details of the orders
<br>    v. As a site user I can delete my orders so that manage the orders
<br>    vi. As a site user I can see about us page so that check opening ours and address for collection
<br>    vii. As a site I can see the contact details and form so that get in touch with the retail if needed


  [Back to top](<#contents>)
  
  - ### FlowChart
    The flowchart was a very useful tool to plan ahead and understand how to build the application below you can see the chart that was made using the [**Lucid**](https://lucid.co/)

    ![Alt text](assets/images/rps-flowchart.png "flowchart")

[Back to top](<#contents>)

  - ### Design Choices
      The idea was to build a terminal based application with smooth transitions to make the UX even more seamless and intuitive. I added few diagrams to make the game more user friendly and make look better as you can see the [Features](#features) section.


[Back to top](<#contents>)

## Features

  ### Landing Play Page
As part of the game a landing area presents the Rock, Paper, Scissors and Gun as hints of how to "unlock" the Legend by selecting the gun to win over all options:

  ![Alt text](./assets/images/Hero-img.png "Landing Play Page") 

[Back to top](<#contents>)

  ### Welcome Message
Welcome message gives the user a clear idea of the game and a 4.5 second to see this message while game is loading is a user friendly interaction.

  ![Alt text](./assets/images/welcome-message.png "Welcome Message") 
  
[Back to top](<#contents>)
        
  ### Main Menu
The main menu gives the user clear options to select and navigate through it.

  ![Alt text](./assets/images/main-menu.png "Main Menu") 

[Back to top](<#contents>)

  ### Rules Menu Option
Rules are clear and easy to understand making user experience more effective regarding to know how to play the game and use the system.

  ![Alt text](./assets/images/rules.png "Rules") 
 
[Back to top](<#contents>)

  ### Credits Menu Option
Credits option gives the user to contact the developer in case o bugs or issues found, or to get in touch for futures projects

  ![Alt text](./assets/images/credits.png "Credits") 
 
[Back to top](<#contents>)

  ### Start Game Menu Option
Once the user start the game it prints to the console a Rock, Paper, Scissors diagram to show user the options also prints the Round counter and a score section to keep track the progress of the game. Finally asks the user to input the option as the user can type "r" "R" "rock" respectivly to the options available. If not a "Invalid option will be printed"

  ![Alt text](./assets/images/game-play.png "Game play") 
 
[Back to top](<#contents>)

  ### Selected Valid Option
Once a valid option is selected it will show what was selected and generated randomly by the computer

  ![Alt text](./assets/images/showing-choices.png "Show Choices") 
 
[Back to top](<#contents>)

  ### Comparing Computer vs User choices
The system will compare the computer and the user choice and print an outcome for that round. Also increasing the round and the score if win or lose round

  ![Alt text](./assets/images/win-round.png "Win Round")
  
  ![Alt text](./assets/images/lost-round.png "Lose Round")
 
[Back to top](<#contents>)

  ### Tied Round
In case the round is Tied a message will be showed and no score will be increased

  ![Alt text](./assets/images/tie-round.png "Tied Roun")

[Back to top](<#contents>)

  ### Game Over
After 5 rounds system will compare the scores and print a final message:

If user wins:

  ![Alt text](./assets/images/final-win.png "User Wins")

If user lose:

  ![Alt text](./assets/images/game-over.png "Game Over")

If its a tie:

  ![Alt text](./assets/images/final-tie.png "Final Tie")

 
[Back to top](<#contents>)

  ### Hidden Features
The user can see the hints and "unlock" the hidden features. If user selects the "Gun" he will automatically will the game and a "Legend" message will be printed:

  ![Alt text](./assets/images/gun.png "Gun")

If the user wins 3 out of 5 rounds the user will be asked to "finish" the computer the "Fatality" will be printed:

  ![Alt text](./assets/images/finish-him.png "Finish Him")

  ![Alt text](./assets/images/fatality.png "Fatality")

[Back to top](<#contents>)

  ### Future Features
For future features I think would be nice to make a colourful game for better user experience also implement if the user wins 3 times in a row he could activate the "nuclear bomb" and win the game. Those hidden features could make a difference and keep the users interested to play more and discover and unlock them. Also by adding a "raking" where user the input name and challange friends and keep record how many times user beated the computer.


[Back to top](<#contents>)

## Testing

The game was tested and validate with PEP8CI with no errors. However the diagrams apresented a few flags and the solution is in the [Bugs and Issues](#bugs-and-issues) section of this file.

![Alt text](assets/images/pep8.png "PEP8CI Report")

[Back to top](<#contents>)

 ### Bugs and Issues
Debugging and troubleshooting were done constantly throughout development.

the PEP8CI presented a few flags regarding to the diagrams and the solutions I found for those was to add "r" before some to the diagrams layout and a "# noqa" and the end of the diagrams, as you can see highlighted in the yellow box of the image below:

 ![Alt text](./assets/images/diagrams-solution.png "Diagrams Solution")

 The links a found the solution are credited in the [Credits](#credits) section of this file.

[Back to top](<#contents>)

___

## Technologies Used
I used the following technologies, platforms and support in building my project:
- The application was built in Python.
- The [**Code Institute**](https://codeinstitute.net/) modules/lessons aided my learning and many of the concepts learned were applied in this project.
- [**GitHub**](https://github.com/Cesargarciajr/bloom-of-life) was used for the project repository.
- [**Code Anywhere**](https://app.codeanywhere.com/) - for IDE and editor of the code.
- [**Heroku**](https://www.heroku.com/platform) was used for application deployment.
- [**PEP8CI Validator**](https://app.codeanywhere.com/) - for error and issues with the code
- [**Lucid**](https://lucid.co/) - Flowchart used on readme file.

[Back to top](<#contents>)

## Deployment

<details>
<summary>GitHub Deployment</summary>
First of all you need to have a GitHub account and I choose it because it's free and easy to create a repository to host your code and share with others.

- To create a repository you just need to go to the main page at the top right you will see a "+" button just click here and then new repository

- Select the name of the project and a description make it public and then create a repository

- Once you created your repository go the settings section and then click on pages

- Select the Branch as main and then save it.

- Finally, your repository is deployed and it should show you a link so you can share it with others.
</details>

<details>
<summary>Cloning the Repo</summary>

1. Click on the "Code" button near the top right corner of the page.
2. Copy the HTTPS or SSH URL that appears in the box.
Open your terminal (or Git Bash on Windows) and navigate to the directory where you want to clone the repository.
3. Type "git clone" followed by a space, and then paste the URL you copied in step 3.
4. Press enter to run the command. This will clone the repository onto your local machine.
5. You should now have a local copy of the GitHub repository on your machine.

</details>

<details>
<summary>Forking the Repo</summary>

1. Click the "Fork" button near the top right corner of the page. This will create a copy of the repository in your own GitHub account.
2. Once the fork is complete, you will be redirected to the forked repository in your account.
3. If you haven't already, clone the forked repository to your local machine using the steps outlined in the previous answer.
4. Make any changes or additions you want to the code in your local copy of the repository.
5. Commit your changes to your local repository using the "git commit" command.
6. Push your changes to the forked repository on GitHub using the "git push" command.
7. If you want to contribute your changes back to the original repository, create a pull request by going to the original repository's page and clicking the "New pull request" button. From there, you can compare your changes to the original repository and request that they be merged.
8. You should now have a forked copy of the GitHub repository in your account, and you can make changes to it and contribute back to the original repository if desired.

</details>

<details> 
<summary>Heroku Deployment</summary>

1. First of all you need to have a Heroku account.
2. From the Dashboard, click "New" - "Create new app".
3. Enter a name for the app. Click "Create App".
4. Connect your GitHub account and select the repository and branch to deploy.
5. When you create the app, you will need to add two buildpacks from the Settings tab. The ordering is as follows:
    - heroku/python
    - heroku/nodejs
6. You must then create a Config Var called PORT. Set this to 8000.

</details>

[Back to top](<#contents>)

## Credits

  ### Content  
  - [**Code Institute**](https://codeinstitute.net/)  - Python Module and Tutor Support.
  - [**Code Institute Python Template**](https://github.com/Code-Institute-Org/python-essentials-template) - Template for Python mock terminal in Heroku.
  - [**GitHub**](https://github.com/) - for deployment and host.
  - [**Code Anywhere**](https://app.codeanywhere.com/) - for IDE and editor of the code.
  - [**Precious Ijege**](https://www.linkedin.com/in/precious-ijege-908a00168/) - Mentor helping with insights and coding fix.
  - [**Tiago Fortaleza Gai**](https://www.linkedin.com/in/tiago-fortaleza-gai/) - Helped throughout the project developing troubleshooting and debugging. 
  - [**W3 Schools**](https://www.w3schools.com/) - used for multiples researches and tutorials in HTML and CSS.
  - [**Stack Overflow**](https://stackoverflow.com/questions/45346575/what-does-noqa-mean-in-python-comments) - solutions for the diagrams issue mentioned in the [Bugs and Issues](#bugs-and-issues) of this file
  - [**PEP8 ORG**](https://pep8.org/#maximum-line-length) - solution for the flags regarding the diagrams in the PEP8 Validator mentioned in the [Bugs and Issues](#bugs-and-issues) of this file.
  - [**Real Python**](https://realpython.com/python-pep8/#maximum-line-length-and-line-breaking) - Also provide with clarity the solution mentinoed in the [Bugs and Issues](#bugs-and-issues) of this file.

 
[Back to top](<#contents>)

  ### Media
- [**Lucid**](https://lucid.co/) - Flowchart used on readme file.
- [**Pinterest**](https://www.pinterest.ie/pin/494340496574099065/) - Background image for the page.
- [**Patorjk**](https://patorjk.com/software/taag/#p=display&f=Bloody&t=FATALITY) - provider with different fonts in diagrams terminal based.
- [**ASCII Art**](https://www.asciiart.eu/weapons/guns) - provided gun ASCII art.


[Back to top](<#contents>)

## Acknowledgments

This project was fun and challenging at the same time. I learned so much while developing and trying to enhance a simple and old game was the biggest creative challange. My mentor [**Precious Ijege**](https://www.linkedin.com/in/precious-ijege-908a00168/) was fundamental to guide me and take the right approaches to the project, I can not forget to say a huge thanks to [**Tiago Fortaleza Gai**](https://www.linkedin.com/in/tiago-fortaleza-gai/) that helped me a lot with programming logics and helped me to debbug the code when I was stucked. I loved the final version of the game and I can say I'm proud of the final version and excited to keep updating and adding future features.

by [**Cesar Garcia**](https://github.com/Cesargarciajr)

# THANK YOU!

[Back to top](<#contents>)