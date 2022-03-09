[![Discord server](https://discord.com/api/guilds/843994109366501376/embed.png)](https://discord.gg/DFDUpXJNdc)

# 🤖 private-discord-bot
A simple moderation/utilities bot made for **[Æ ༽༼#0533](https://discord.com/users/470866478720090114)**'s servers.

# 📢 My bots
**[Connect 4](https://top.gg/bot/795099690609279006)** :fire:  
**[RPGBruh](https://top.gg/bot/947242264483209269)** :star:  

# 📜 License
This code is free to use as long as you understand it.

# 📑 Table of contents
* [Notices](#notices)
* [Setup](#setup)
* [Config](#config)
* [Features](#developer-commands)
	* [Developer text-commands](#developer-commands)
	* [Events](#events)  

## Notices
* Default.support_server_link is not set.
* Update_avatar lacks custom avatars.
* Missing adding roles on verification

## Setup
1. Download & Install [Python](https://python.org/download). 
2. Install the latest version of [discord.py](https://github.com/Rapptz/discord.py) by running the following command in a shell (console).
```bash
py -m pip install -U git+https://github.com/Rapptz/discord.py
```
3. Make a discord application thru [Discord's developer portal](https://discord.com/developers/applications)
4. Create a bot on the [bot](https://discord.com/developers/applications) tab. (Generate an invite link thru the [Oauth](https://discord.com/developers/applications) tab and invite the bot to your server)
5. Generate a token by clicking the `Regenerate token` button & copy it by clikcing the `Copy` button.
6. Clone this repository by running the following command. (Requires [GIT](https://git-scm.com/downloads))
```bash
git clone https://Marseel-E/private-discord-bot.git
```
7. Open the folder with your desired IDE/Text edittor.
8. Create a `.env` file in the parent directory.
9. Write the following in the `.env` file, replacing `YOUR_BOT_TOKEN` with the token you copied in step 5 earlier.
```
TOKEN = "YOUR_BOT_TOKEN"
```
10. Open a shell in the parent directory. (You can do that by going to your folders/finder and writting `cmd` in the path then clicking ENTER)
11. Install the dependencies by running the following command.
```bash
pip install -U -r requirements.txt
```
12. Run the [main.py](https://github.com/Marseel-E/private-discord-bot/blob/main/main.py) file to start the bot. (You can either manually run the file from the folder or run the following command in the shell you started previously)
```bash
python main.py
```
13. Finally go to [Discord](https://discord.com) and your bot should be online.

## Config
Theres a couple variables you can configure to your own:
> prefix (The bot's prefix)  
> status (The bot's status)  
> join_channel (The join channel ID)  
> verify_message (The verify message content)  
> logo_path (The PATH to the logo image file)  

These can be configured in the [tools.py](https://github.com/Marseel-E/private-discord-bot/blob/main/utils/tools.py) file inside the [utils](https://github.com/Marseel-E/private-discord-bot/blob/main/utils) directory.
(Just edit the values after the `=` sign)

## Developer commands
* ### direct_message `.direct_message|dm @user message [embeded=False]`
```py
""" Sends a direct message to the specified user.

Parameters:
-----------
	member <discord.User> - The user to send the message to. (Required)
	message <str> - The message to send to the user. (Required)
			
	embeded <bool> - Whether to send an embed or not.
""" 
```
* ### update_avatar `.update_avatar|ua`
```py
""" Updates the bot's avatar. 

Parameters:
-----------
	new_avatar <bool> - Whether to use a custom avatar or not.
"""
```
* ### update_username `.update_username|uu new_username`
```py
""" Updates the bot's username.

Parameters:
-----------
	new_username <str> - The new username.
"""
```
* ### test_verify `.test_verify|tv [msg]`
```py
""" Sends a test message for the join message event.

Parameters:
-----------
	verify_message <str> - The message to be in the message.
"""
```
* ### eval `.eval|python|py [unformatted=False] cmd`
```py
""" Evaluates python code

Parameters:
-----------
	cmd <str> - The ccode to evalutae. (Required)
			
	unformatted <bool> - Whether to send the text in a styalized embed or not.
"""
```
* ### load `.load [cog=None]`
```py
""" Loads a cog.

Parameters:
-----------
	cog <str> - The cog name.
"""
```
* ### unload `.unload [cog=None]`
```py
""" Unloads a cog.
		
Parameters:
-----------
	cog <str> - The cog name.
"""
```
* ### reload `.reload [cog=None]`
```py
""" Reloads a cog.

Parameters:
-----------
	cog <str> - The cog name.
"""
```

## Events
* ### on_member_join
```py
""" Sends a message to the specified channel whenever a member joins with a specific view to them only for verification. """
```
