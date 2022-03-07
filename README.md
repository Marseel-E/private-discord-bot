# private-discord-bot
A simple moderation/utilities bot made for Æ's servers.
# Table of contents
* [Developer text-commands](#developer-commands)
* [Events](#events)

## Developer commands
* ### direct_message `.direct_message|dm @member message [embeded=False]`
```py
""" Sends a direct message to the specified member.

Parameters:
-----------
	member <discord.Member> - The member to send the message to. (Required)
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
* ### test_join_message `.test_join_message|tjm [msg="Verify your a human!"]`
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
## Events
* ### on_member_join
```py
""" Sends a message to the specified channel whenever a member joins with a specific view to them only for verification. """
```
