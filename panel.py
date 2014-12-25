import math
import pygame
import time


class Panel(object):

    def __init__(self,canvas,elevator_list):
        self.cp_1_x=-20
        self.cp_1_y=-200
        self.cp_2_x=170
        self.cp_3_y=100
        self.canvas=canvas
        self.button_list = []
        for i in range (0, 4):  
            self.button_list.append([])
        self.elevator_list=elevator_list
        self.flag_list = []
        for i in range (0, 4):
            new = []
            for j in range (0, 12):
                new.append(False)
            self.flag_list.append(new)


        ####   LIFT 1

        #MAIN PANEL BODY
        self.body_1 = canvas.create_rectangle(50+self.cp_1_x,300+self.cp_1_y,200+self.cp_1_x,550+self.cp_1_y,fill="#fff",activefill="#C1E950")        
        self.display_half_1   = canvas.create_rectangle(50+self.cp_1_x,300+self.cp_1_y,200+self.cp_1_x,350+self.cp_1_y,fill="#B18D92")
        self.name_1 = canvas.create_text(120+self.cp_1_x,285+self.cp_1_y, text="LIFT-1 Control", activefill="red")
        
        #BUTTON +
        self.button_1_13   = canvas.create_rectangle(60+self.cp_1_x,310+self.cp_1_y,90+self.cp_1_x,340+self.cp_1_y,fill="#A9A9A9")
        self.button_1_13_id = canvas.create_text(70+self.cp_1_x, 320+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_13_id, text="+")
        canvas.tag_bind(self.button_1_13, '<Button-1>', lambda x: self.PeopleButtonClicked(1,"+"))
        canvas.tag_bind(self.button_1_13_id, '<Button-1>', lambda x: self.PeopleButtonClicked(1,"+"))
        
        #BUTTON people
        self.button_1_14   = canvas.create_rectangle(110+self.cp_1_x,310+self.cp_1_y,140+self.cp_1_x,340+self.cp_1_y,fill="white")
        self.button_1_14_id = canvas.create_text(120+self.cp_1_x, 320+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_14_id, text=self.elevator_list[0].people)
        
        #BUTTON -
        self.button_1_15   = canvas.create_rectangle(160+self.cp_1_x,310+self.cp_1_y,190+self.cp_1_x,340+self.cp_1_y,fill="#A9A9A9")
        self.button_1_15_id = canvas.create_text(170+self.cp_1_x, 320+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_15_id, text="-")
        canvas.tag_bind(self.button_1_15, '<Button-1>', lambda x: self.PeopleButtonClicked(1,"-"))
        canvas.tag_bind(self.button_1_15_id, '<Button-1>', lambda x: self.PeopleButtonClicked(1,"-"))

        #BUTTON A
        self.button_1_16   = canvas.create_rectangle(200+self.cp_1_x,520+self.cp_1_y,230+self.cp_1_x,550+self.cp_1_y,fill="#A9A9A9")
        self.button_1_16_id = canvas.create_text(210+self.cp_1_x, 527+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_16_id, text="A")
        canvas.tag_bind(self.button_1_16, '<Button-1>', lambda x: self.AlarmButtonClicked(1,"A"))
        canvas.tag_bind(self.button_1_16_id, '<Button-1>', lambda x: self.AlarmButtonClicked(1,"A"))
        
        #BUTTON 1
        self.button_1_1   = canvas.create_rectangle(60+self.cp_1_x,360+self.cp_1_y,90+self.cp_1_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_1_1_id = canvas.create_text(70+self.cp_1_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_1_id, text="1")
        canvas.tag_bind(self.button_1_1, '<Button-1>', lambda x: self.PanelButtonClicked(1,1,self.flag_list[0][0]))
        canvas.tag_bind(self.button_1_1_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,1,self.flag_list[0][0]))
        self.button_list[0].append(self.button_1_1)
        
        #BUTTON 2
        self.button_1_2 = canvas.create_rectangle(110+self.cp_1_x,360+self.cp_1_y,140+self.cp_1_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_1_2_id = canvas.create_text(120+self.cp_1_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_2_id, text="2")
        canvas.tag_bind(self.button_1_2, '<Button-1>', lambda x: self.PanelButtonClicked(1,2,self.flag_list[0][1]))
        canvas.tag_bind(self.button_1_2_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,2,self.flag_list[0][1]))
        self.button_list[0].append(self.button_1_2)

        #BUTTON 3
        self.button_1_3 = canvas.create_rectangle(160+self.cp_1_x,360+self.cp_1_y,190+self.cp_1_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_1_3_id = canvas.create_text(170+self.cp_1_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_3_id, text="3")
        canvas.tag_bind(self.button_1_3, '<Button-1>', lambda x: self.PanelButtonClicked(1,3,self.flag_list[0][2]))
        canvas.tag_bind(self.button_1_3_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,3,self.flag_list[0][2]))
        self.button_list[0].append(self.button_1_3)

        #BUTTON 4
        self.button_1_4 = canvas.create_rectangle(60+self.cp_1_x,410+self.cp_1_y,90+self.cp_1_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_1_4_id = canvas.create_text(70+self.cp_1_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_4_id, text="4")
        canvas.tag_bind(self.button_1_4, '<Button-1>', lambda x: self.PanelButtonClicked(1,4,self.flag_list[0][3]))
        canvas.tag_bind(self.button_1_4_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,4,self.flag_list[0][3]))
        self.button_list[0].append(self.button_1_4)

        #BUTTON 5
        self.button_1_5 = canvas.create_rectangle(110+self.cp_1_x,410+self.cp_1_y,140+self.cp_1_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_1_5_id = canvas.create_text(120+self.cp_1_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_5_id, text="5")
        canvas.tag_bind(self.button_1_5, '<Button-1>', lambda x: self.PanelButtonClicked(1,5,self.flag_list[0][4]))
        canvas.tag_bind(self.button_1_5_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,5,self.flag_list[0][4]))
        self.button_list[0].append(self.button_1_5)

        #BUTTON 6
        self.button_1_6 = canvas.create_rectangle(160+self.cp_1_x,410+self.cp_1_y,190+self.cp_1_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_1_6_id = canvas.create_text(170+self.cp_1_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_6_id, text="6")
        canvas.tag_bind(self.button_1_6, '<Button-1>', lambda x: self.PanelButtonClicked(1,6,self.flag_list[0][5]))
        canvas.tag_bind(self.button_1_6_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,6,self.flag_list[0][5]))
        self.button_list[0].append(self.button_1_6)
        
        #BUTTON 7
        self.button_1_7 = canvas.create_rectangle(60+self.cp_1_x,460+self.cp_1_y,90+self.cp_1_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_1_7_id = canvas.create_text(70+self.cp_1_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_7_id, text="7")
        canvas.tag_bind(self.button_1_7, '<Button-1>', lambda x: self.PanelButtonClicked(1,7,self.flag_list[0][6]))
        canvas.tag_bind(self.button_1_7_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,7,self.flag_list[0][6]))
        self.button_list[0].append(self.button_1_7)
        
        #BUTTON 8
        self.button_1_8 = canvas.create_rectangle(110+self.cp_1_x,460+self.cp_1_y,140+self.cp_1_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_1_8_id = canvas.create_text(120+self.cp_1_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_8_id, text="8")
        canvas.tag_bind(self.button_1_8, '<Button-1>', lambda x: self.PanelButtonClicked(1,8,self.flag_list[0][7]))
        canvas.tag_bind(self.button_1_8_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,8,self.flag_list[0][7]))
        self.button_list[0].append(self.button_1_8)
        
        #BUTTON 9
        self.button_1_9 = canvas.create_rectangle(160+self.cp_1_x,460+self.cp_1_y,190+self.cp_1_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_1_9_id = canvas.create_text(170+self.cp_1_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_9_id, text="9")
        canvas.tag_bind(self.button_1_9, '<Button-1>', lambda x: self.PanelButtonClicked(1,9,self.flag_list[0][8]))
        canvas.tag_bind(self.button_1_9_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,9,self.flag_list[0][8]))
        self.button_list[0].append(self.button_1_9)
        
        #BUTTON G
        self.button_1_10 = canvas.create_rectangle(110+self.cp_1_x,510+self.cp_1_y,140+self.cp_1_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_1_10_id = canvas.create_text(120+self.cp_1_x, 520+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_10_id, text="G")
        canvas.tag_bind(self.button_1_10, '<Button-1>', lambda x: self.PanelButtonClicked(1,'G',self.flag_list[0][9]))
        canvas.tag_bind(self.button_1_10_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,'G',self.flag_list[0][9]))
        self.button_list[0].append(self.button_1_10)
        
         #BUTTON Open
        self.button_1_11 = canvas.create_rectangle(60+self.cp_1_x,510+self.cp_1_y,90+self.cp_1_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_1_11_id = canvas.create_text(65+self.cp_1_x, 517+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_11_id, text="<|>")
        canvas.tag_bind(self.button_1_11, '<Button-1>', lambda x: self.PanelButtonClicked(1,'O',self.flag_list[0][10]))
        canvas.tag_bind(self.button_1_11_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,'O',self.flag_list[0][10]))
        self.button_list[0].append(self.button_1_11)
        
        #BUTTON Close
        self.button_1_12 = canvas.create_rectangle(160+self.cp_1_x,510+self.cp_1_y,190+self.cp_1_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_1_12_id = canvas.create_text(165+self.cp_1_x, 517+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_1_12_id, text=">|<")
        canvas.tag_bind(self.button_1_12, '<Button-1>', lambda x: self.PanelButtonClicked(1,'C',self.flag_list[0][11]))
        canvas.tag_bind(self.button_1_12_id, '<Button-1>', lambda x: self.PanelButtonClicked(1,'C',self.flag_list[0][11]))
        self.button_list[0].append(self.button_1_12)
        

        ####   LIFT 2

        #MAIN PANEL BODY
        self.body_2 = canvas.create_rectangle(50+self.cp_2_x,300+self.cp_1_y,200+self.cp_2_x,550+self.cp_1_y,fill="#fff",activefill="#C1E950")        
        self.display_half_2   = canvas.create_rectangle(50+self.cp_2_x,300+self.cp_1_y,200+self.cp_2_x,350+self.cp_1_y,fill="#B18D92")
        self.name_2 = canvas.create_text(120+self.cp_2_x,285+self.cp_1_y, text="LIFT-2 Control", activefill="red")

        #BUTTON +
        self.button_2_13   = canvas.create_rectangle(60+self.cp_2_x,310+self.cp_1_y,90+self.cp_2_x,340+self.cp_1_y,fill="#A9A9A9")
        self.button_2_13_id = canvas.create_text(70+self.cp_2_x, 320+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_13_id, text="+")
        canvas.tag_bind(self.button_2_13, '<Button-1>', lambda x: self.PeopleButtonClicked(2,"+"))
        canvas.tag_bind(self.button_2_13_id, '<Button-1>', lambda x: self.PeopleButtonClicked(2,"+"))
        
        #BUTTON people
        self.button_2_14   = canvas.create_rectangle(110+self.cp_2_x,310+self.cp_1_y,140+self.cp_2_x,340+self.cp_1_y,fill="white")
        self.button_2_14_id = canvas.create_text(120+self.cp_2_x, 320+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_14_id, text=self.elevator_list[1].people)
        
        #BUTTON -
        self.button_2_15   = canvas.create_rectangle(160+self.cp_2_x,310+self.cp_1_y,190+self.cp_2_x,340+self.cp_1_y,fill="#A9A9A9")
        self.button_2_15_id = canvas.create_text(170+self.cp_2_x, 320+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_15_id, text="-")
        canvas.tag_bind(self.button_2_15, '<Button-1>', lambda x: self.PeopleButtonClicked(2,"-"))
        canvas.tag_bind(self.button_2_15_id, '<Button-1>', lambda x: self.PeopleButtonClicked(2,"-"))

        #BUTTON A
        self.button_2_16   = canvas.create_rectangle(200+self.cp_2_x,520+self.cp_1_y,230+self.cp_2_x,550+self.cp_1_y,fill="#A9A9A9")
        self.button_2_16_id = canvas.create_text(210+self.cp_2_x, 527+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_16_id, text="A")
        canvas.tag_bind(self.button_2_16, '<Button-1>', lambda x: self.AlarmButtonClicked(2,"A"))
        canvas.tag_bind(self.button_2_16_id, '<Button-1>', lambda x: self.AlarmButtonClicked(2,"A"))
        
        #BUTTON 1
        self.button_2_1   = canvas.create_rectangle(60+self.cp_2_x,360+self.cp_1_y,90+self.cp_2_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_2_1_id = canvas.create_text(70+self.cp_2_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_1_id, text="1")
        canvas.tag_bind(self.button_2_1, '<Button-1>', lambda x: self.PanelButtonClicked(2,1,self.flag_list[1][0]))
        canvas.tag_bind(self.button_2_1_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,1,self.flag_list[1][0]))
        self.button_list[1].append(self.button_2_1)
        
        #BUTTON 2
        self.button_2_2 = canvas.create_rectangle(110+self.cp_2_x,360+self.cp_1_y,140+self.cp_2_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_2_2_id = canvas.create_text(120+self.cp_2_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_2_id, text="2")
        canvas.tag_bind(self.button_2_2, '<Button-1>', lambda x: self.PanelButtonClicked(2,2,self.flag_list[1][1]))
        canvas.tag_bind(self.button_2_2_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,2,self.flag_list[1][1]))
        self.button_list[1].append(self.button_2_2)
        
        #BUTTON 3
        self.button_2_3 = canvas.create_rectangle(160+self.cp_2_x,360+self.cp_1_y,190+self.cp_2_x,390+self.cp_1_y,fill="#A9A9A9")
        self.button_2_3_id = canvas.create_text(170+self.cp_2_x, 370+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_3_id, text="3")
        canvas.tag_bind(self.button_2_3, '<Button-1>', lambda x: self.PanelButtonClicked(2,3,self.flag_list[1][2]))
        canvas.tag_bind(self.button_2_3_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,3,self.flag_list[1][2]))
        self.button_list[1].append(self.button_2_3)
        
        #BUTTON 4
        self.button_2_4 = canvas.create_rectangle(60+self.cp_2_x,410+self.cp_1_y,90+self.cp_2_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_2_4_id = canvas.create_text(70+self.cp_2_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_4_id, text="4")
        canvas.tag_bind(self.button_2_4, '<Button-1>', lambda x: self.PanelButtonClicked(2,4,self.flag_list[1][3]))
        canvas.tag_bind(self.button_2_4_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,4,self.flag_list[1][3]))
        self.button_list[1].append(self.button_2_4)
        
        #BUTTON 5
        self.button_2_5 = canvas.create_rectangle(110+self.cp_2_x,410+self.cp_1_y,140+self.cp_2_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_2_5_id = canvas.create_text(120+self.cp_2_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_5_id, text="5")
        canvas.tag_bind(self.button_2_5, '<Button-1>', lambda x: self.PanelButtonClicked(2,5,self.flag_list[1][4]))
        canvas.tag_bind(self.button_2_5_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,5,self.flag_list[1][4]))
        self.button_list[1].append(self.button_2_5)
        
        #BUTTON 6
        self.button_2_6 = canvas.create_rectangle(160+self.cp_2_x,410+self.cp_1_y,190+self.cp_2_x,440+self.cp_1_y,fill="#A9A9A9")
        self.button_2_6_id = canvas.create_text(170+self.cp_2_x, 420+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_6_id, text="6")
        canvas.tag_bind(self.button_2_6, '<Button-1>', lambda x: self.PanelButtonClicked(2,6,self.flag_list[1][5]))
        canvas.tag_bind(self.button_2_6_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,6,self.flag_list[1][5]))
        self.button_list[1].append(self.button_2_6)
        
        #BUTTON 7
        self.button_2_7 = canvas.create_rectangle(60+self.cp_2_x,460+self.cp_1_y,90+self.cp_2_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_2_7_id = canvas.create_text(70+self.cp_2_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_7_id, text="7")
        canvas.tag_bind(self.button_2_7, '<Button-1>', lambda x: self.PanelButtonClicked(2,7,self.flag_list[1][6]))
        canvas.tag_bind(self.button_2_7_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,7,self.flag_list[1][6]))
        self.button_list[1].append(self.button_2_7)
        
        #BUTTON 8
        self.button_2_8 = canvas.create_rectangle(110+self.cp_2_x,460+self.cp_1_y,140+self.cp_2_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_2_8_id = canvas.create_text(120+self.cp_2_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_8_id, text="8")
        canvas.tag_bind(self.button_2_8, '<Button-1>', lambda x: self.PanelButtonClicked(2,8,self.flag_list[1][7]))
        canvas.tag_bind(self.button_2_8_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,8,self.flag_list[1][7]))
        self.button_list[1].append(self.button_2_8)
        
        #BUTTON 9
        self.button_2_9 = canvas.create_rectangle(160+self.cp_2_x,460+self.cp_1_y,190+self.cp_2_x,490+self.cp_1_y,fill="#A9A9A9")
        self.button_2_9_id = canvas.create_text(170+self.cp_2_x, 470+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_9_id, text="9")
        canvas.tag_bind(self.button_2_9, '<Button-1>', lambda x: self.PanelButtonClicked(2,9,self.flag_list[1][8]))
        canvas.tag_bind(self.button_2_9_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,9,self.flag_list[1][8]))
        self.button_list[1].append(self.button_2_9)
        
        #BUTTON G
        self.button_2_10 = canvas.create_rectangle(110+self.cp_2_x,510+self.cp_1_y,140+self.cp_2_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_2_10_id = canvas.create_text(120+self.cp_2_x, 520+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_10_id, text="G")
        canvas.tag_bind(self.button_2_10, '<Button-1>', lambda x: self.PanelButtonClicked(2,'G',self.flag_list[1][9]))
        canvas.tag_bind(self.button_2_10_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,'G',self.flag_list[1][9]))
        self.button_list[1].append(self.button_2_10)
        
         #BUTTON Open
        self.button_2_11 = canvas.create_rectangle(60+self.cp_2_x,510+self.cp_1_y,90+self.cp_2_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_2_11_id = canvas.create_text(65+self.cp_2_x, 517+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_11_id, text="<|>")
        canvas.tag_bind(self.button_2_11, '<Button-1>', lambda x: self.PanelButtonClicked(2,'O',self.flag_list[1][10]))
        canvas.tag_bind(self.button_2_11_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,'O',self.flag_list[1][10]))
        self.button_list[1].append(self.button_2_11)
        
        #BUTTON Close
        self.button_2_12 = canvas.create_rectangle(160+self.cp_2_x,510+self.cp_1_y,190+self.cp_2_x,540+self.cp_1_y,fill="#A9A9A9")
        self.button_2_12_id = canvas.create_text(165+self.cp_2_x, 517+self.cp_1_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_2_12_id, text=">|<")
        canvas.tag_bind(self.button_2_12, '<Button-1>', lambda x: self.PanelButtonClicked(2,'C',self.flag_list[1][11]))
        canvas.tag_bind(self.button_2_12_id, '<Button-1>', lambda x: self.PanelButtonClicked(2,'C',self.flag_list[1][11]))
        self.button_list[1].append(self.button_2_12)
        
        ####   LIFT 3

        #MAIN PANEL BODY
        self.body_3 = canvas.create_rectangle(50+self.cp_1_x,300+self.cp_3_y  ,200+self.cp_1_x,550+self.cp_3_y   ,fill="#fff",activefill="#C1E950")        
        self.display_half_3   = canvas.create_rectangle(50+self.cp_1_x,300+self.cp_3_y   ,200+self.cp_1_x,350+self.cp_3_y   ,fill="#B18D92")
        self.name_3 = canvas.create_text(120+self.cp_1_x,285+self.cp_3_y   , text="LIFT-3 Control", activefill="red")

        #BUTTON +
        self.button_3_13   = canvas.create_rectangle(60+self.cp_1_x,310+self.cp_3_y,90+self.cp_1_x,340+self.cp_3_y,fill="#A9A9A9")
        self.button_3_13_id = canvas.create_text(70+self.cp_1_x, 320+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_13_id, text="+")
        canvas.tag_bind(self.button_3_13, '<Button-1>', lambda x: self.PeopleButtonClicked(3,"+"))
        canvas.tag_bind(self.button_3_13_id, '<Button-1>', lambda x: self.PeopleButtonClicked(3,"+"))
        
        #BUTTON people
        self.button_3_14   = canvas.create_rectangle(110+self.cp_1_x,310+self.cp_3_y,140+self.cp_1_x,340+self.cp_3_y,fill="white")
        self.button_3_14_id = canvas.create_text(120+self.cp_1_x, 320+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_14_id, text=self.elevator_list[2].people)
        
        #BUTTON -
        self.button_3_15   = canvas.create_rectangle(160+self.cp_1_x,310+self.cp_3_y,190+self.cp_1_x,340+self.cp_3_y,fill="#A9A9A9")
        self.button_3_15_id = canvas.create_text(170+self.cp_1_x, 320+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_15_id, text="-")
        canvas.tag_bind(self.button_3_15, '<Button-1>', lambda x: self.PeopleButtonClicked(3,"-"))
        canvas.tag_bind(self.button_3_15_id, '<Button-1>', lambda x: self.PeopleButtonClicked(3,"-"))

        #BUTTON A
        self.button_3_16   = canvas.create_rectangle(200+self.cp_1_x,520+self.cp_3_y,230+self.cp_1_x,550+self.cp_3_y,fill="#A9A9A9")
        self.button_3_16_id = canvas.create_text(210+self.cp_1_x, 527+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_16_id, text="A")
        canvas.tag_bind(self.button_3_16, '<Button-1>', lambda x: self.AlarmButtonClicked(3,"A"))
        canvas.tag_bind(self.button_3_16_id, '<Button-1>', lambda x: self.AlarmButtonClicked(3,"A"))
        
        
        #BUTTON 1
        self.button_3_1   = canvas.create_rectangle(60+self.cp_1_x,360+self.cp_3_y   ,90+self.cp_1_x,390+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_1_id = canvas.create_text(70+self.cp_1_x, 370+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_1_id, text="1")
        canvas.tag_bind(self.button_3_1, '<Button-1>', lambda x: self.PanelButtonClicked(3,1,self.flag_list[2][0]))
        canvas.tag_bind(self.button_3_1_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,1,self.flag_list[2][0]))
        self.button_list[2].append(self.button_3_1)
        
        #BUTTON 2
        self.button_3_2 = canvas.create_rectangle(110+self.cp_1_x,360+self.cp_3_y   ,140+self.cp_1_x,390+self.cp_3_y  ,fill="#A9A9A9")
        self.button_3_2_id = canvas.create_text(120+self.cp_1_x, 370+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_2_id, text="2")
        canvas.tag_bind(self.button_3_2, '<Button-1>', lambda x: self.PanelButtonClicked(3,2,self.flag_list[2][1]))
        canvas.tag_bind(self.button_3_2_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,2,self.flag_list[2][1]))
        self.button_list[2].append(self.button_3_2)
        
        #BUTTON 3
        self.button_3_3 = canvas.create_rectangle(160+self.cp_1_x,360+self.cp_3_y   ,190+self.cp_1_x,390+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_3_id = canvas.create_text(170+self.cp_1_x, 370+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_3_id, text="3")
        canvas.tag_bind(self.button_3_3, '<Button-1>', lambda x: self.PanelButtonClicked(3,3,self.flag_list[2][2]))
        canvas.tag_bind(self.button_3_3_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,3,self.flag_list[2][2]))
        self.button_list[2].append(self.button_3_3)
        
        #BUTTON 4
        self.button_3_4 = canvas.create_rectangle(60+self.cp_1_x,410+self.cp_3_y   ,90+self.cp_1_x,440+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_4_id = canvas.create_text(70+self.cp_1_x, 420+self.cp_3_y  , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_4_id, text="4")
        canvas.tag_bind(self.button_3_4, '<Button-1>', lambda x: self.PanelButtonClicked(3,4,self.flag_list[2][3]))
        canvas.tag_bind(self.button_3_4_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,4,self.flag_list[2][3]))
        self.button_list[2].append(self.button_3_4)
        
        #BUTTON 5
        self.button_3_5 = canvas.create_rectangle(110+self.cp_1_x,410+self.cp_3_y   ,140+self.cp_1_x,440+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_5_id = canvas.create_text(120+self.cp_1_x, 420+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_5_id, text="5")
        canvas.tag_bind(self.button_3_5, '<Button-1>', lambda x: self.PanelButtonClicked(3,5,self.flag_list[2][4]))
        canvas.tag_bind(self.button_3_5_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,5,self.flag_list[2][4]))
        self.button_list[2].append(self.button_3_5)
        
        #BUTTON 6
        self.button_3_6 = canvas.create_rectangle(160+self.cp_1_x,410+self.cp_3_y   ,190+self.cp_1_x,440+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_6_id = canvas.create_text(170+self.cp_1_x, 420+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_6_id, text="6")
        canvas.tag_bind(self.button_3_6, '<Button-1>', lambda x: self.PanelButtonClicked(3,6,self.flag_list[2][5]))
        canvas.tag_bind(self.button_3_6_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,6,self.flag_list[2][5]))
        self.button_list[2].append(self.button_3_6)
        
        #BUTTON 7
        self.button_3_7 = canvas.create_rectangle(60+self.cp_1_x,460+self.cp_3_y   ,90+self.cp_1_x,490+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_7_id = canvas.create_text(70+self.cp_1_x, 470+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_7_id, text="7")
        canvas.tag_bind(self.button_3_7, '<Button-1>', lambda x: self.PanelButtonClicked(3,7,self.flag_list[2][6]))
        canvas.tag_bind(self.button_3_7_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,7,self.flag_list[2][6]))
        self.button_list[2].append(self.button_3_7)
        
        #BUTTON 8
        self.button_3_8 = canvas.create_rectangle(110+self.cp_1_x,460+self.cp_3_y   ,140+self.cp_1_x,490+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_8_id = canvas.create_text(120+self.cp_1_x, 470+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_8_id, text="8")
        canvas.tag_bind(self.button_3_8, '<Button-1>', lambda x: self.PanelButtonClicked(3,8,self.flag_list[2][7]))
        canvas.tag_bind(self.button_3_8_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,8,self.flag_list[2][7]))
        self.button_list[2].append(self.button_3_8)
        
        #BUTTON 9
        self.button_3_9 = canvas.create_rectangle(160+self.cp_1_x,460+self.cp_3_y   ,190+self.cp_1_x,490+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_9_id = canvas.create_text(170+self.cp_1_x, 470+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_9_id, text="9")
        canvas.tag_bind(self.button_3_9, '<Button-1>', lambda x: self.PanelButtonClicked(3,9,self.flag_list[2][8]))
        canvas.tag_bind(self.button_3_9_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,9,self.flag_list[2][8]))
        self.button_list[2].append(self.button_3_9)
        
        #BUTTON G
        self.button_3_10 = canvas.create_rectangle(110+self.cp_1_x,510+self.cp_3_y   ,140+self.cp_1_x,540+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_10_id = canvas.create_text(120+self.cp_1_x, 520+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_10_id, text="G")
        canvas.tag_bind(self.button_3_10, '<Button-1>', lambda x: self.PanelButtonClicked(3,'G',self.flag_list[2][9]))
        canvas.tag_bind(self.button_3_10_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,'G',self.flag_list[2][9]))
        self.button_list[2].append(self.button_3_10)
        
         #BUTTON Open
        self.button_3_11 = canvas.create_rectangle(60+self.cp_1_x,510+self.cp_3_y   ,90+self.cp_1_x,540+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_11_id = canvas.create_text(65+self.cp_1_x, 517+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_11_id, text="<|>")
        canvas.tag_bind(self.button_3_11, '<Button-1>', lambda x: self.PanelButtonClicked(3,'O',self.flag_list[2][10]))
        canvas.tag_bind(self.button_3_11_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,'O',self.flag_list[2][10]))
        self.button_list[2].append(self.button_3_11)
        
        #BUTTON Close
        self.button_3_12 = canvas.create_rectangle(160+self.cp_1_x,510+self.cp_3_y  ,190+self.cp_1_x,540+self.cp_3_y   ,fill="#A9A9A9")
        self.button_3_12_id = canvas.create_text(165+self.cp_1_x, 517+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_3_12_id, text=">|<")
        canvas.tag_bind(self.button_3_12, '<Button-1>', lambda x: self.PanelButtonClicked(3,'C',self.flag_list[2][11]))
        canvas.tag_bind(self.button_3_12_id, '<Button-1>', lambda x: self.PanelButtonClicked(3,'C',self.flag_list[2][11]))
        self.button_list[2].append(self.button_3_12)
        
        ####   LIFT 4

        #MAIN PANEL BODY
        self.body_4 = canvas.create_rectangle(50+self.cp_2_x,300+self.cp_3_y   ,200+self.cp_2_x,550+self.cp_3_y   ,fill="#fff",activefill="#C1E950")        
        self.display_half_4   = canvas.create_rectangle(50+self.cp_2_x,300+self.cp_3_y,200+self.cp_2_x,350+self.cp_3_y   ,fill="#B18D92")
        self.name_4 = canvas.create_text(120+self.cp_2_x,285+self.cp_3_y   , text="LIFT-4 Control",activefill="red")

        #BUTTON +
        self.button_4_13   = canvas.create_rectangle(60+self.cp_2_x,310+self.cp_3_y,90+self.cp_2_x,340+self.cp_3_y,fill="#A9A9A9")
        self.button_4_13_id = canvas.create_text(70+self.cp_2_x, 320+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_13_id, text="+")
        canvas.tag_bind(self.button_4_13, '<Button-1>', lambda x: self.PeopleButtonClicked(4,"+"))
        canvas.tag_bind(self.button_4_13_id, '<Button-1>', lambda x: self.PeopleButtonClicked(4,"+"))
        
        #BUTTON people
        self.button_4_14   = canvas.create_rectangle(110+self.cp_2_x,310+self.cp_3_y,140+self.cp_2_x,340+self.cp_3_y,fill="white")
        self.button_4_14_id = canvas.create_text(120+self.cp_2_x, 320+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_14_id, text=self.elevator_list[3].people)
        
        #BUTTON -
        self.button_4_15   = canvas.create_rectangle(160+self.cp_2_x,310+self.cp_3_y,190+self.cp_2_x,340+self.cp_3_y,fill="#A9A9A9")
        self.button_4_15_id = canvas.create_text(170+self.cp_2_x, 320+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_15_id, text="-")
        canvas.tag_bind(self.button_4_15, '<Button-1>', lambda x: self.PeopleButtonClicked(4,"-"))
        canvas.tag_bind(self.button_4_15_id, '<Button-1>', lambda x: self.PeopleButtonClicked(4,"-"))

        #BUTTON A
        self.button_4_16   = canvas.create_rectangle(200+self.cp_2_x,520+self.cp_3_y,230+self.cp_2_x,550+self.cp_3_y,fill="#A9A9A9")
        self.button_4_16_id = canvas.create_text(210+self.cp_2_x, 527+self.cp_3_y, anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_16_id, text="A")
        canvas.tag_bind(self.button_4_16, '<Button-1>', lambda x: self.AlarmButtonClicked(4,"A"))
        canvas.tag_bind(self.button_4_16_id, '<Button-1>', lambda x: self.AlarmButtonClicked(4,"A"))
        
        #BUTTON 1
        self.button_4_1   = canvas.create_rectangle(60+self.cp_2_x,360+self.cp_3_y   ,90+self.cp_2_x,390+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_1_id = canvas.create_text(70+self.cp_2_x, 370+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_1_id, text="1")
        canvas.tag_bind(self.button_4_1, '<Button-1>', lambda x: self.PanelButtonClicked(4,1,self.flag_list[3][0]))
        canvas.tag_bind(self.button_4_1_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,1,self.flag_list[3][0]))
        self.button_list[3].append(self.button_4_1)
        
        #BUTTON 2
        self.button_4_2 = canvas.create_rectangle(110+self.cp_2_x,360+self.cp_3_y   ,140+self.cp_2_x,390+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_2_id = canvas.create_text(120+self.cp_2_x, 370+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_2_id, text="2")
        canvas.tag_bind(self.button_4_2, '<Button-1>', lambda x: self.PanelButtonClicked(4,2,self.flag_list[3][1]))
        canvas.tag_bind(self.button_4_2_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,2,self.flag_list[3][1]))
        self.button_list[3].append(self.button_4_2)
        
        #BUTTON 3
        self.button_4_3 = canvas.create_rectangle(160+self.cp_2_x,360+self.cp_3_y   ,190+self.cp_2_x,390+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_3_id = canvas.create_text(170+self.cp_2_x, 370+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_3_id, text="3")
        canvas.tag_bind(self.button_4_3, '<Button-1>', lambda x: self.PanelButtonClicked(4,3,self.flag_list[3][2]))
        canvas.tag_bind(self.button_4_3_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,3,self.flag_list[3][2]))
        self.button_list[3].append(self.button_4_3)
        
        #BUTTON 4
        self.button_4_4 = canvas.create_rectangle(60+self.cp_2_x,410+self.cp_3_y   ,90+self.cp_2_x,440+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_4_id = canvas.create_text(70+self.cp_2_x, 420+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_4_id, text="4")
        canvas.tag_bind(self.button_4_4, '<Button-1>', lambda x: self.PanelButtonClicked(4,4,self.flag_list[3][3]))
        canvas.tag_bind(self.button_4_4_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,4,self.flag_list[3][3]))
        self.button_list[3].append(self.button_4_4)
        
        #BUTTON 5
        self.button_4_5 = canvas.create_rectangle(110+self.cp_2_x,410+self.cp_3_y   ,140+self.cp_2_x,440+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_5_id = canvas.create_text(120+self.cp_2_x, 420+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_5_id, text="5")
        canvas.tag_bind(self.button_4_5, '<Button-1>', lambda x: self.PanelButtonClicked(4,5,self.flag_list[3][4]))
        canvas.tag_bind(self.button_4_5_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,5,self.flag_list[3][4]))
        self.button_list[3].append(self.button_4_5)
        
        #BUTTON 6
        self.button_4_6 = canvas.create_rectangle(160+self.cp_2_x,410+self.cp_3_y   ,190+self.cp_2_x,440+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_6_id = canvas.create_text(170+self.cp_2_x, 420+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_6_id, text="6")
        canvas.tag_bind(self.button_4_6, '<Button-1>', lambda x: self.PanelButtonClicked(4,6,self.flag_list[3][5]))
        canvas.tag_bind(self.button_4_6_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,6,self.flag_list[3][5]))
        self.button_list[3].append(self.button_4_6)
                
        #BUTTON 7
        self.button_4_7 = canvas.create_rectangle(60+self.cp_2_x,460+self.cp_3_y   ,90+self.cp_2_x,490+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_7_id = canvas.create_text(70+self.cp_2_x, 470+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_7_id, text="7")
        canvas.tag_bind(self.button_4_7, '<Button-1>', lambda x: self.PanelButtonClicked(4,7,self.flag_list[3][6]))
        canvas.tag_bind(self.button_4_7_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,7,self.flag_list[3][6]))
        self.button_list[3].append(self.button_4_7)
        
        #BUTTON 8
        self.button_4_8 = canvas.create_rectangle(110+self.cp_2_x,460+self.cp_3_y   ,140+self.cp_2_x,490+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_8_id = canvas.create_text(120+self.cp_2_x, 470+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_8_id, text="8")
        canvas.tag_bind(self.button_4_8, '<Button-1>', lambda x: self.PanelButtonClicked(4,8,self.flag_list[3][7]))
        canvas.tag_bind(self.button_4_8_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,8,self.flag_list[3][7]))
        self.button_list[3].append(self.button_4_8)
        
        #BUTTON 9
        self.button_4_9 = canvas.create_rectangle(160+self.cp_2_x,460+self.cp_3_y   ,190+self.cp_2_x,490+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_9_id = canvas.create_text(170+self.cp_2_x, 470+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_9_id, text="9")
        canvas.tag_bind(self.button_4_9, '<Button-1>', lambda x: self.PanelButtonClicked(4,9,self.flag_list[3][8]))
        canvas.tag_bind(self.button_4_9_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,9,self.flag_list[3][8]))
        self.button_list[3].append(self.button_4_9)
        
        #BUTTON G
        self.button_4_10 = canvas.create_rectangle(110+self.cp_2_x,510+self.cp_3_y   ,140+self.cp_2_x,540+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_10_id = canvas.create_text(120+self.cp_2_x, 520+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_10_id, text="G")
        canvas.tag_bind(self.button_4_10, '<Button-1>', lambda x: self.PanelButtonClicked(4,'G',self.flag_list[3][9]))
        canvas.tag_bind(self.button_4_10_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,'G',self.flag_list[3][9]))
        self.button_list[3].append(self.button_4_10)
        
         #BUTTON Open
        self.button_4_11 = canvas.create_rectangle(60+self.cp_2_x,510+self.cp_3_y ,90+self.cp_2_x,540+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_11_id = canvas.create_text(65+self.cp_2_x, 517+self.cp_3_y   , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_11_id, text="<|>")
        canvas.tag_bind(self.button_4_11, '<Button-1>', lambda x: self.PanelButtonClicked(4,'O',self.flag_list[3][10]))
        canvas.tag_bind(self.button_4_11_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,'O',self.flag_list[3][10]))
        self.button_list[3].append(self.button_4_11)
        
        #BUTTON Close
        self.button_4_12 = canvas.create_rectangle(160+self.cp_2_x,510+self.cp_3_y   ,190+self.cp_2_x,540+self.cp_3_y   ,fill="#A9A9A9")
        self.button_4_12_id = canvas.create_text(165+self.cp_2_x, 517+self.cp_3_y  , anchor="nw", activefill="red")
        canvas.itemconfig(self.button_4_12_id, text=">|<")
        canvas.tag_bind(self.button_4_12, '<Button-1>', lambda x: self.PanelButtonClicked(4,'C',self.flag_list[3][11]))
        canvas.tag_bind(self.button_4_12_id, '<Button-1>', lambda x: self.PanelButtonClicked(4,'C',self.flag_list[3][11]))
        self.button_list[3].append(self.button_4_12)
        
    def PanelButtonClicked(self,liftno,event,flag):
        print "Lift "+str(liftno)+" : Button "+str(event)
        
        if flag == False:
            
            if event == 'G':
                self.canvas.itemconfig(self.button_list[liftno-1][9], fill="#ff0")
                self.flag_list[liftno-1][9] = True
                self.elevator_list[liftno-1].addFloor(0,"none")
            elif not(event == 'C') and not(event == 'O'):    
                self.canvas.itemconfig(self.button_list[liftno-1][event-1], fill="#ff0")
                self.flag_list[liftno-1][event-1] = True

            if  event == 'C' or event == 'O' or event =='G':
                if event == 'O':
                    if self.elevator_list[liftno-1].status == "closing" or self.elevator_list[liftno-1].status == "idle":
                        self.elevator_list[liftno-1].status = "opening"         
                elif event == 'C':
                    if self.elevator_list[liftno-1].status == "opening" or self.elevator_list[liftno-1].status == "open":
                        self.elevator_list[liftno-1].status = "closing"
            else:
                self.elevator_list[liftno-1].addFloor(event,"none")

    def PeopleButtonClicked(self,liftno,event):
        if event== '+' and self.elevator_list[liftno-1].move_direction=="idle" and not self.elevator_list[liftno-1].status=="idle":
            self.elevator_list[liftno-1].people=self.elevator_list[liftno-1].people+1
            if self.elevator_list[liftno-1].status=="closing":
                self.elevator_list[liftno-1].status="opening"
            # print "people= "+str(liftno)+" "+str(self.elevator_list[liftno-1].people) 
        elif event== '-' and self.elevator_list[liftno-1].move_direction=="idle" and not self.elevator_list[liftno-1].status=="idle":
            if(self.elevator_list[liftno-1].people>0):
                self.elevator_list[liftno-1].people=self.elevator_list[liftno-1].people-1
                if self.elevator_list[liftno-1].status=="closing":
                    self.elevator_list[liftno-1].status="opening"
        
        if(self.elevator_list[liftno-1].people>6):
            if(self.elevator_list[liftno-1].ready==1):
                self.elevator_list[liftno-1].ready=2
            if liftno==1:
                self.canvas.itemconfig(self.button_1_14, fill="red")
                self.canvas.itemconfig(self.button_1_14_id, activefill="white")
            elif liftno==2:
                self.canvas.itemconfig(self.button_2_14, fill="red")
                self.canvas.itemconfig(self.button_2_14_id, activefill="white")
            elif liftno==3:
                self.canvas.itemconfig(self.button_3_14, fill="red")
                self.canvas.itemconfig(self.button_3_14_id, activefill="white")
            elif liftno==4:
                self.canvas.itemconfig(self.button_4_14, fill="red")
                self.canvas.itemconfig(self.button_4_14_id, activefill="white")
        else:
            if(self.elevator_list[liftno-1].ready==2):
                self.elevator_list[liftno-1].ready=1
            if liftno==1:
                self.canvas.itemconfig(self.button_1_14, fill="white")
                self.canvas.itemconfig(self.button_1_14_id, activefill="red")
            elif liftno==2:
                self.canvas.itemconfig(self.button_2_14, fill="white")
                self.canvas.itemconfig(self.button_2_14_id, activefill="red")
            elif liftno==3:
                self.canvas.itemconfig(self.button_3_14, fill="white")
                self.canvas.itemconfig(self.button_3_14_id, activefill="red")
            elif liftno==4:
                self.canvas.itemconfig(self.button_4_14, fill="white")
                self.canvas.itemconfig(self.button_4_14_id, activefill="red")

        
        self.canvas.itemconfig(self.button_1_14_id, text=self.elevator_list[0].people)
        self.canvas.itemconfig(self.button_2_14_id, text=self.elevator_list[1].people)
        self.canvas.itemconfig(self.button_3_14_id, text=self.elevator_list[2].people)
        self.canvas.itemconfig(self.button_4_14_id, text=self.elevator_list[3].people)

    def AlarmButtonClicked(self,liftno,event):

        if(self.elevator_list[liftno-1].move_direction=="up"):
            self.elevator_list[liftno-1].call_queue.append([math.ceil(self.elevator_list[liftno-1].current_floor),"none"])
        elif(self.elevator_list[liftno-1].move_direction=="down"):
            self.elevator_list[liftno-1].call_queue.append([math.floor(self.elevator_list[liftno-1].current_floor),"none"])
        elif(self.elevator_list[liftno-1].move_direction=="idle"):
            self.elevator_list[liftno-1].status="opening"
        self.elevator_list[liftno-1].ready=3 
        
        pygame.init()
        pygame.mixer.music.load("strikerfoul.mp3")
        pygame.mixer.music.play(-1)
        time.sleep(.30)
        pygame.mixer.music.stop()
        
        if liftno==1:
            self.canvas.itemconfig(self.button_1_16, fill="red")
        elif liftno==2:
            self.canvas.itemconfig(self.button_2_16, fill="red")
            
        elif liftno==3:
            self.canvas.itemconfig(self.button_3_16, fill="red")
            
        elif liftno==4:
            self.canvas.itemconfig(self.button_4_16, fill="red")