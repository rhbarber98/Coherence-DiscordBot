![Logo](images/banner2.png)

# Coherence
### A logical Discord bot based on Discord.py

## Introduction

Coherence is an ultra-simple Discord chatbot written on the Discord.py API wrapper. Coherence takes simple chat commands as input and delivers static responses in the text channel.

Commands can easily be edited to your liking using a text editor, and installation is super fast and easy to do.

If you need additional assistance, please contact us through our [Official Discord Server](https://discord.gg/Wg4r2hh) using the #support channel and a member of our community will be happy to assist.

## Quick start
* [Creating an API Token](#creating-an-api-token)
* [Installation](#installation)
  * [Run Locally](#run-locally)
  * [Deploy to Heroku](#deploy-to-heroku)
* [Support](#support)

## Creating an API token

In order to run Coherence, you must first create an API token using the [Discord Developers Portal](https://discordapp.com/developers).

1. Log in using your discord account and click __New Application__.
1. Give your application a name and click __Create__.
1. On the left-hand sidebar, navigate to the __Bot__ tab.
1. Click on __Add Bot__.
1. Take note of the Token. You will need it later to configure the bot script.

## Installation

Run Coherence on your own computer using the Python command line environment, or deploy Coherence to a Heroku application.

* [Run Locally](#run-locally)
* [Deploy to Heroku](#deploy-to-heroku)

### Run Locally

Running coherence locally is easy. Simply install the required dependencies and then run the `coherence.py` script.

#### Prerequisites

In order to run Coherence locally, you must install a few files that are needed for the script to run. If you are deploying Coherence to a Heroku application, these prerequisites will be installed automatically.
* Python 3.7.3 or greater

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

#### Installing Prerequisites

To install the required prerequisites:

1. Download and install the latest version of Python from [python.org](https://www.python.org)
1. Open a terminal or command line on your computer
1. Run the following command:
  * For Windows:
  `python pip install discord.py`
  * For MacOS/Unix:
  `python3 -m pip install discord.py`

#### Configuring and Running the bot

1. Download or Clone the Coherence repository and extract the files to a preferred location on your disk.
1. Open `coherence.py` in the text editor of your choice.
1. Find the `TOKEN` variable near the top of the file and replace the filler text with your Discord bot API token created earlier and save the file.
```py
# Discord API User Token
TOKEN = 'Insert your bot token here'
```
1. Change to the directory where you extracted the files:
  * Windows:
  `cd C:\My\Project\Path`
  * MacOS/Unix:
  `cd /My/Project/Path`
1. Launch the bot script:
  * Windows:
  `python coherence.py`
  * MacOS/Unix:
  `python3 coherence.py`

You should now see `Connected to Discord API...Logged in as...` in the terminal. You have successfully installed and setup Coherence.


### Deploy to Heroku

This repository contains everything you need for a five-minute deployment to Heroku. Deployment to Heroku directly from GitHub is extremely fast and easy, and is our recommended way to run Coherence.

1. Fork the Coherence repository to your GitHub account.
1. Open `coherence.py` in the text editor of your choice.
1. Find the `TOKEN` variable near the top of the file and replace the filler text with your Discord bot API token created earlier and save the file.
```py
# Discord API User Token
TOKEN = 'Insert your bot token here'
```
1. Create a __new application__ on Heroku
1. Select __GitHub__ under __Deployment Method__.
1. Follow the steps on the Heroku Dashboard to connect your Heroku Account to GitHub if you haven't already done so.
1. Search for and select the fork of the repository you created in step 1.
1. Click on __Connect__.
1. Scroll down to the bottom of the page, select the __Master__ branch, and then click __Deploy__.
1. After the deployment is finished, go to the __Resources__ tab and toggle the switch to start the `worker python coherence.py` dyno.

You have now successfully deployed Coherence on Heroku.

## Support

If you need additional assistance, please contact us through our [Official Discord Server](https://discord.gg/Wg4r2hh) using the #support channel and a member of our community will be happy to assist.
