![Logo](images/banner2.png)

# Coherence
### A logical Discord bot based on Discord.py

## Introduction

Coherence is an ultra-simple Discord bot written on the Discord.py API wrapper. Coherence takes simple chat commands as input and delivers static responses.

Commands can easily be edited using a text editor, and installation is fast and easy to do on any Windows or MacOS/Unix system.

If you need additional assistance, please contact us through our [Official Discord Server](https://discord.gg/Wg4r2hh) using the #support channel and a member of our community will be happy to assist.

## Quick Start
* [Creating an API Token](#creating-an-api-token)
* [Adding the bot user](#adding-the-bot-user)
* [Installation](#installation)
  * [Deploy to Heroku (Recommended)](#deploy-to-heroku)
  * [Run Locally](#run-locally)
    * [Prerequisites](#prerequisites)
      * [Installing Prerequisites](#installing-prerequisites)
    * [Configuring and Running the bot](#configuring-and-running-the-bot)
* [Support](#support)

### Creating an API token

In order to run Coherence, you must first create a Discord bot user and accompanying API token using the [Discord Developer Portal](https://discordapp.com/developers).

1. Log in using your discord account and click __New Application__.
1. Give your application a name and click __Create__.
1. On the left-hand sidebar, navigate to the __Bot__ tab.
1. Click on __Add Bot__.
1. Take note of the __token__. You will need it later to configure the bot script.

### Adding the bot user

In order to use the bot, you must first invite the bot user you just created to a Discord server.

1. From the Discord Developer Portal, navigate to the __OAuth2__ tab.
1. Scroll down to the __OAuth2 URL Generator__ and check the __Bot__ scope.
1. You will notice a new set of check boxes has appeared below the scopes section. Select the permissions you would like your bot user to start with. You can always modify the bot's roles later to grant or revoke permissions. Note that the bot requires the __View Channels__ and __Send Messages__ permissions in order to receive and respond to chat commands.
1. Once you have selected the permissions you would like to grant your bot, copy the link below the scope selector and paste it into your web browser.
1. Log in using your discord account and select a server you'd like your bot to join. You must be an administrator on a server in order to add a bot.

You should now see the bot in your members list on the Discord client.

### Installation

You can deploy Coherence to a Heroku application, or run Coherence on your own computer using the Python command line environment. We recommend Heroku for a seamless deployment.

* [Deploy to Heroku (Recommended)](#deploy-to-heroku)
* [Run Locally](#run-locally)

#### Deploy to Heroku

This repository contains everything you need for a five-minute deployment to Heroku. Predefined build instructions mean all prerequisites will be installed automatically, resulting an an extremely fast and simple deployment.

1. Fork the Coherence repository to your GitHub account.
1. Create a __new application__ on Heroku and give it a name.
1. Go to the __Settings__ tab inside your new application and select __Reveal Config Vars__.
1. In the __KEY__ field, input `API_KEY`. In the __VALUE__ field, input your Discord API token you created earlier.
1. Click on __Add__ to set the API environment variable, and then return to the __Deploy__ tab.
1. Select __GitHub__ under __Deployment Method__.
1. Follow the steps on the Heroku Dashboard to connect your Heroku Account to GitHub.
1. Select the newly forked repository created in step 1.
1. Click on __Connect__.
1. Scroll down to the bottom of the page, select the __Master__ branch, and then click __Deploy__.
1. After the deployment is finished, go to the __Resources__ tab and start the __worker python coherence.py__ dyno.

If everything is setup correctly, your bot user created earlier should now show up online in the Discord client.

#### Run Locally

Running coherence locally is easy. Simply install the required dependencies and then run the __coherence.py__ script.

##### Prerequisites

In order to run Coherence locally, you must install a few files that are needed for the script to run. If you are deploying Coherence to a Heroku application, these prerequisites will be installed automatically from the build instructions.

* Python version 3.7.3 or greater

Along with the following Python modules:

* Discord.py - v1.2.3 or greater
* aiohttp - v3.5.4 or greater
* async-timeout - v3.0.1 or greater
* attrs - v19.1.0 or greater
* certifi - v2019.6.16 or greater
* chardet - v3.0.4 or greater
* idna - v2.8 or greater
* multidict - v4.5.2 or greater
* websockets - v6.0 or greater
* yarl - v1.3.0 or greater

###### Installing Prerequisites

To install the required prerequisites listed above:

1. Download and install the latest version of Python from [python.org](https://www.python.org)
1. Open a terminal or command line on your computer
1. Run the following command:
  * For Windows:
  `py -3 -m pip install discord.py`
  * For MacOS/Unix:
  `python3 -m pip install discord.py`

##### Configuring and Running the bot

1. Download or Clone the Coherence repository and extract the files to a preferred location on your disk.
1. In the files you just downloaded, locate __config.py.local__ and rename it to __config.py__. When asked, __replace__ the existing file with the one you just renamed.
1. Open the new __config.py__ file in the text editor of your choice.
1. Input your Discord API token you created earlier.
```py
API_KEY = 'Your Discord API Token'
```
1. Save changes, then open a new terminal or command prompt.
1. Change to the directory where you extracted the files:
  * Windows:
  `cd C:\Path\To\Files`
  * MacOS/Unix:
  `cd /Path/To/Files`
1. Launch the bot script:
  * Windows:
  `py -3 coherence.py`
  * MacOS/Unix:
  `python3 coherence.py`

You should now see `Connected to Discord API...Logged in as...` in the terminal. You have successfully installed and setup Coherence.

## Support

If you need additional assistance, please contact us through our [Official Discord Server](https://discord.gg/Wg4r2hh) using the #support channel and a member of our community will be happy to assist.
