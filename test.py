import random
class Test_Gui():
	def __init__(self,main,panel):
		self.app=main
		self.panel=panel
		self.test_move()

	def test_move(self):
		'''
		for elevator in self.app.elevator_list:
			for i in range(0,10):
				elevator.addFloor(i,"none")
		for elevator in self.app.elevator_list:
			for i in range(0,10):
				elevator.addFloor(9-i,"none")
		
		for elevator in self.app.elevator_list:
			elevator.addFloor(random.randint(0,9),"none")

		for i in range(0,10):
			self.app.floorRequest(random.randint(0,8),"up");
			self.app.floorRequest(random.randint(1,9),"down");'''