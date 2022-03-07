from typing import TypedDict


class Color(TypedDict):
	blurple: int = int("5261f8", 16)


class Default(TypedDict):
	support_server_link: str = "https://discord.com/python"
	support_server: str = f"[Support Server]({support_server_link})"
	color: int = Color.blurple


class Config(TypedDict):
	prefix: str = "."
	status: str = "Protecting Æ ༽༼#0533"
	join_channel: int = 846981584774103113
	verify_message: str = "Verify your a human!"
	logo_path: str = "C:\\Users\\Marsel\\Desktop\\Æ's bodyguard\\logo.png"