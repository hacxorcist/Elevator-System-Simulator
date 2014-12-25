from floor import *
from elevator import *
from Tkinter import *
from panel import *
import panel
import math
from test import *

class Application:    
    
    def __init__(self, master):

        global building

        self.master = master
        self.building = Canvas(master, width = 700, height = 700)
        self.building.pack(side=LEFT)

        self.panel = Canvas(master, width = 550, height = 700)
        self.panel.pack(side=LEFT)

        self.make_floors(self.building)
        self.make_elevators(self.building)
        self.draw_panel(self.panel)
        self.gui_testing()
        
    def draw_panel(self, arena):
        self.p = Panel(arena,self.elevator_list)
        arena.create_text(200, 50, text="Elevator Simulator", font=('Purisa', '20', 'bold','italic')) 


    def make_elevators(self,canvas):

        self.elevator_list = []
        for i in range(0,4):
            e = Elevator(self,canvas, i)
            self.elevator_list.append(e)

    def make_floors(self,canvas): 
              
        for i in range(0,10):
            canvas.create_rectangle(50,45+(i*60),100,95+(i*60), fill="#5190ED", activefill = "pink")
            canvas.create_rectangle(115,45+(i*60),215,95+(i*60), fill = "#BFEFFF")
            canvas.create_rectangle(220,45+(i*60),320,95+(i*60), fill = "#BFEFFF")
            canvas.create_rectangle(325,45+(i*60),425,95+(i*60), fill = "#BFEFFF")
            canvas.create_rectangle(430,45+(i*60),530,95+(i*60), fill = "#BFEFFF")
            canvas.create_rectangle(545,45+(i*60),600,95+(i*60), fill = "#5190ED", activefill = "#5B9C64")
            # \canvas.create_rectangle(615,45+(i*60),650,95+(i*60), fill = "#5190ED", activefill = "#5B9C64")
            # canvas.create_rectangle(665,45+(i*60),700,95+(i*60), fill = "#5190ED", activefill = "#5B9C64")
           

        self.floor_list = []
        for i in range(0,10):
            f = Floor(canvas,self,i)
            self.floor_list.append(f)

    def simulate(self):

        for e in self.elevator_list:
            e.update(self.building)
        # print str(panel.sim) + "aa"
        self.master.after(40,self.simulate)

    def floorRequest(self,X,direc):
        if (direc=="up"):
            A=[200]*4
            for e in self.elevator_list:
                if e.ready==1:
                    if e.move_direction=="up" and e.current_floor<=X:
                        A[e.name]=e.current_floor
                    elif e.move_direction=="idle":
                        if(len(e.call_queue)>0):
                            if e.call_queue[0][0]>e.current_floor and e.current_floor>X:
                                A[e.name]=2*max(e.call_queue)[0]-e.current_floor
                            elif e.call_queue[0][0]<e.current_floor and min(e.call_queue)[0]<=X:
                                A[e.name]=e.current_floor+X-min(e.call_queue)[0]
                            else:
                                A[e.name]=e.current_floor
                        else:
                            A[e.name]=e.current_floor
                    elif e.move_direction=="up" and e.current_floor>X:
                        A[e.name]=2*max(e.call_queue)[0]-e.current_floor
                    elif e.move_direction=="down":
                        Y=min(e.call_queue)[0]
                        if Y>X:
                            A[e.name]=e.current_floor
                        else:
                            A[e.name]=e.current_floor-Y+X-Y
            if self.elevator_list[0].ready!=1 and self.elevator_list[1].ready!=1 and self.elevator_list[2].ready!=1 and self.elevator_list[3].ready!=1:
                A[self.elevator_list[0].name]=100
            print A
            mini=abs(X-A[0])
            mini_index=0
            for i in range(0,4):
                A[i]=abs(X-A[i])
                if mini>=A[i]:
                    mini=A[i]
                    mini_index=i
            self.elevator_list[mini_index].addFloor(X,direc)

        elif (direc=="down"):
            A=[200]*4
            for e in self.elevator_list:
                if e.ready==1:
                    if e.move_direction=="down" and e.current_floor>=X:
                        A[e.name]=e.current_floor
                    elif e.move_direction=="idle":
                        if(len(e.call_queue)>0):
                            if e.call_queue[0][0]<e.current_floor and e.current_floor<X:
                                A[e.name]=2*min(e.call_queue)-e.current_floor
                            elif e.call_queue[0][0]>e.current_floor and max(e.call_queue)[0]>=X:
                                A[e.name]=e.current_floor+max(e.call_queue)[0]-X
                            else:
                                A[e.name]=e.current_floor
                        else:
                             A[e.name]=e.current_floor
                    elif e.move_direction=="down" and e.current_floor<X:
                        A[e.name]=2*min(e.call_queue)[0]-e.current_floor
                    elif e.move_direction=="up":
                        Y=max(e.call_queue)[0]
                        if Y<X:
                            A[e.name]=e.current_floor
                        else:
                            A[e.name]=Y-e.current_floor+Y-X 
                if self.elevator_list[0].ready!=1 and self.elevator_list[1].ready!=1 and self.elevator_list[2].ready!=1 and self.elevator_list[3].ready!=1:
                    A[self.elevator_list[0].name]=100      
            print A
            mini=abs(X-A[0])
            mini_index=0
            for i in range(0,4):
                A[i]=abs(X-A[i])
                if mini>=A[i]:
                    mini=A[i]
                    mini_index=i
            self.elevator_list[mini_index].addFloor(X,direc)

    def gui_testing(self):
        self.test=Test_Gui(self,self.p)
       
master = Tk()
app = Application(master)
app.simulate()
master.mainloop()