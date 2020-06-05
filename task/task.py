class Task:
	name: str
	sp: int

	def __init__(self, sp, name=""):
		self.sp = int(sp)
		self.name = name

	def __str__(self):
		return f"{self.sp:<3.0f} {self.name}"