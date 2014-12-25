class Elevator(object):

	def __init__(self,building,canvas,name):
		self.canvas=canvas
		self.WIDTH = 30
		self.HEIGHT = 50
		self.SEPARATION = 105 
		self.START_X = 150
		self.START_Y = 50
		self.VELOCITY = 5
		self.VELOCITY2= 1
		self.COLOR = "green"
		self.building=building
		self.name = name
		self.body = canvas.create_rectangle(self.START_X+(self.name*self.SEPARATION),self.START_Y+535,self.START_X+self.WIDTH+(self.name*self.SEPARATION),self.START_Y+self.HEIGHT+535,fill=self.COLOR)
		self.x = canvas.coords(self.body)[0]
		self.y = canvas.coords(self.body)[1]
		self.dest = "None"
		self.left = canvas.create_rectangle(self.START_X+(self.name*self.SEPARATION)+self.WIDTH/2,self.y,self.START_X+(self.name*self.SEPARATION)+self.WIDTH/2,self.y+self.HEIGHT,fill="#FE8")
		self.right = canvas.create_rectangle(self.START_X+(self.name*self.SEPARATION)+self.WIDTH/2,self.y,self.START_X+(self.name*self.SEPARATION)+self.WIDTH/2,self.y+self.HEIGHT,fill="#FE8")
		self.floor_list = []
		for i in range(0,10):
			self.floor_list.append(False)
		self.call_queue = []
		self.dest = None
		self.gate_status = 0
		self.move_direction = "idle"
		self.open_status = 0
		self.status = "idle"
		self.current_floor = 0
		self.vel = 0
		self.people=0
		self.ready=1
	
	def sorted_queue(self,call_q):
		q_len= len(call_q)
		list1=[]
		list2=[]
		current= self.current_floor
		#print "current "+str(self.name)+"= "+str(self.current_floor)
		if (self.move_direction=="up"):
			for i in range(0,q_len):
				if call_q[i][0]>current:
					list1.append(call_q[i])
				else:
					list2.append(call_q[i])
			list1=sorted(list1, reverse=False)
			list2=sorted(list2, reverse=True)
			self.call_queue=list1+list2
			
		elif (self.move_direction=="down"):
			for i in range(0,q_len):
				if call_q[i][0]<current:
					list1.append(call_q[i])
				else:
					list2.append(call_q[i])
			list1=sorted(list1, reverse=True)
			list2=sorted(list2, reverse=False)
			self.call_queue=list1+list2
			
	def addFloor(self,floor,dir):
		if [floor,dir] not in self.call_queue:
			if ((([floor,"up"] not in self.call_queue) or ([floor,"down"] not in self.call_queue))  and dir=="none"):
				self.call_queue.append([floor,dir])
			elif dir=="up" or dir=="down":				
				self.call_queue.append([floor,dir])
				if [floor,"none"] in self.call_queue:
					self.call_queue.remove([floor,"none"])

		self.sorted_queue(self.call_queue)
		print "call queue "+ str(self.name+1)+" "+ str(self.call_queue)

	def update(self,canvas):
		if self.status == "idle":
			self.checkQueue()

		elif self.status == "moving":
			self.checkQueue()
			self.checkDestination()
			self.moveElevator(canvas)

		elif self.status == "opening":
			self.openGate(canvas)

		elif self.status == "open":
			self.keepGateOpen()

		elif self.status == "closing" and self.ready==1:
			self.closeGate(canvas)

		elif self.status == "closing" and (self.ready==2 or self.ready==3):
			self.openGate(canvas)
		
		canvas.update()

	def checkQueue(self):

		if not(len(self.call_queue)==0):
			self.dest = self.call_queue[0][0]
			if self.status == "idle":
				if self.current_floor < self.dest:
					self.vel = -self.VELOCITY
				elif self.current_floor > self.dest:
					self.vel = self.VELOCITY
				else:
					self.vel = 0

			self.status = "moving"

	def checkDestination(self):
		if not(len(self.call_queue)==0):
			self.dest = self.call_queue[0][0]
		self.sorted_queue(self.call_queue)
		self.current_floor = float(10 - float((self.y+15)/60))
		if self.dest == self.current_floor:
			if self.call_queue[0][1]=="up":
				self.building.floor_list[self.dest].upButtonTurnOff()
				self.building.floor_list[self.dest].elevator_floor_up = None
			elif self.call_queue[0][1]=="down":
				self.building.floor_list[self.dest].downButtonTurnOff()
				self.building.floor_list[self.dest].elevator_floor_down = None


			panel = self.building.p
			if self.dest==0:
				panel.canvas.itemconfig(panel.button_list[self.name][9], fill="#A9A9A9")
				panel.flag_list[self.name][9] = False
			else:
				panel.canvas.itemconfig(panel.button_list[self.name][int(self.dest)-1], fill="#A9A9A9")
				panel.flag_list[self.name][int(self.dest)-1] = False

			
			self.call_queue.remove(self.call_queue[0])


			self.status = "opening"
			self.vel = 0

	def openGate(self,canvas):
		if self.gate_status == 20:
			self.status = "open"
		else:
			self.gate_status += 1
			canvas.coords(self.left,self.x+self.WIDTH/2,self.y,self.x-self.gate_status+self.WIDTH/2,self.y+self.HEIGHT)
			canvas.coords(self.right,self.x+self.WIDTH/2,self.y,self.x+self.gate_status+self.WIDTH/2,self.y+self.HEIGHT)

	def keepGateOpen(self):
		if self.open_status >= 40 and self.ready==1:
			self.status = "closing"
			self.open_status = 0

		else:
			self.open_status += 2

	def closeGate(self,canvas):
		if self.gate_status == 0 :
			self.status = "idle"

		else:
			self.gate_status -= 1
			canvas.coords(self.left,self.x-self.gate_status+self.WIDTH/2,self.y,self.x+self.WIDTH/2,self.y+self.HEIGHT)
			canvas.coords(self.right,self.x+self.WIDTH/2+self.gate_status,self.y,self.x+self.WIDTH/2,self.y+self.HEIGHT)

	

	def moveElevator(self,canvas):
		if self.vel>0:
			self.move_direction = "down"
		elif self.vel<0:
			self.move_direction = "up"
		else:
			self.move_direction = "idle"

		canvas.move(self.body,0,self.vel)
		canvas.move(self.left,0,self.vel)
		canvas.move(self.right,0,self.vel)
		self.x = canvas.coords(self.body)[0]
		self.y = canvas.coords(self.body)[1]
