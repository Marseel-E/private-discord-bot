[![Discord server](https://discord.com/api/guilds/843994109366501376/embed.png)](https://discord.gg/DFDUpXJNdc)
[![Discord.py](https://img.shields.io/badge/Discord.py-2.0-blue)](https://github.com/Rapptz/discord.py)
[![Supported Python versions](https://img.shields.io/pypi/pyversions/discord.py.svg)](https://pypi.python.org/pypi/discord.py)

# 🤖 private-discord-bot
A simple moderation/utilities bot made for **[Æ ༽༼#0533](https://discord.com/users/470866478720090114)**'s servers.

# 📢 My bots
**[Connect 4](https://top.gg/bot/795099690609279006)** :fire:  
**[RPGBruh](https://top.gg/bot/947242264483209269)** :star:  

### 📜 [License](LICENSE)

# 📑 Table of contents
* [Notices](#notices)
* [Features](#developer-commands)
	* [Developer text-commands](#developer-commands)
	* [Events](#events)  

## Notices
* Default.support_server_link is not set.
* Update_avatar lacks custom avatars.

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
