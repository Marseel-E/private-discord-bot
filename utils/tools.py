class _Color:
	def __init__(self):
		self.blurple = int("5261f8", 16)


	def custom(self, hex_code: str) -> int:
		return int(str(hex_code), 16)

Color = _Color()



class _Default:
	def __init__(self):
		self.support_server_link = "https://discord.com/python"
		self.support_server = f"[Support Server]({self.support_server_link})"
		self.color = Color.blurple

Default = _Default()