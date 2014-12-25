import math
class Floor(object):
	def __init__(self,canvas,app,name):
		self.app = app
		self.name = name
		self.shift_x = 473
		self.canvas=canvas
		if self.name!=9:
			self.upButton = canvas.create_polygon( self.shift_x+100, (10-name)*60-5 , self.shift_x+88, 60*(10-name) + 10 , self.shift_x+112, 60*(10-name) + 10 , fill="#000",activefill="cyan",tags="self.onButtonClickUp")
			canvas.tag_bind(self.upButton, '<ButtonPress-1>', self.onButtonClickUp)
		#print "Up: "+str(self.upButton)
		if self.name!=0:
			self.downButton = canvas.create_polygon( self.shift_x+88, (10-name)*60 + 15, self.shift_x+112, (10-name)*60 + 15 , self.shift_x+100, 60*(10-name) + 30, fill="#000",activefill="#CC99CC",tags="self.onButtonClickDown")
			canvas.tag_bind(self.downButton, '<ButtonPress-1>', self.onButtonClickDown)
		#print "Down: "+str(self.downButton)
		self.number = canvas.create_text(75, (10-name)*60 + 10, text=name,activefill="red")
		self.up_status = "off"
		self.down_status = "off"
		self.elevator_floor_up = None
		self.elevator_floor_down = None
		
	def onButtonClickUp(self,event):
		print "Floor "+str(self.name)+" Up Button "+str(event.x)+" "+str(event.y)
		self.canvas.itemconfigure(self.upButton,fill="cyan")
		self.up_status = "on"
		self.app.floorRequest(self.name,"up")

	def onButtonClickDown(self,event):
		print "Floor "+str(self.name)+" Down Button "+str(event.x)+" "+str(event.y)
		self.canvas.itemconfigure(self.downButton,fill="#CC99CC")
		self.down_status = "on"
		self.app.floorRequest(self.name,"down")

	def upButtonTurnOff(self):
		self.canvas.itemconfigure(self.upButton, fill = "#000")
		self.up_status = "off"

	def downButtonTurnOff(self):
		self.canvas.itemconfigure(self.downButton, fill = "#000")
		self.down_status = "off"
	