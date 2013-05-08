from swampy.Gui import *
from swampy.TurtleWorld import *
import random

class SimpleWorld(TurtleWorld):

	def setup(self):
		self.row()
		self.canvas = self.ca(width=300,height=300,bg='white')
		self.col()
		self.gr(cols=2)
		self.bu(text='Make circle', command=self.make_circle)
		self.bu(text='Send',command=self.send_text)
		self.bu(text='Clear text',command=self.clear_text)
		self.bu(text='Change color',command=self.read_text)
		self.bu(text='Clear screen',command=self.canvas.delete('current'))
		self.mb = self.mb(text=self.color_list[0])
		for color in self.color_list:
			self.mi(self.mb, text=color, command=Callable(set_color,color))
		self.endgr()
		self.row(pady=20)
		self.entry = self.en()
		self.entry.bind('<Return>',self.send_text)
		self.endrow()
		self.text = self.te(width=30,height=8)
		self.endcol()
		self.endrow()

	color_list =['white','black','red','green',
			'blue','cyan','yellow','magenta']

	def set_color(self,color):
		self.mb.config(text=color)
		self.entry.insert(color)
		self.text.insert(color)

	def make_circle(self):
		global circle
		x = random.randint(-150,150)
		y = random.randint(-150,150)
		size = random.randint(5,20)
		circle = self.canvas.circle([x,y],size,fill='red')

	def send_text(self,event=None):
		words = self.entry.get() + '\n'
		self.text.insert(END, words)

	def clear_text(self):
		self.text.delete(0.0,END)

	def read_text(self):
		global circle
		global text
		color = self.entry.get()
		if circle == None:
			self.text.insert(END,'No circle exists\n')
			return None
		if color in self.color_list:
			circle.config(fill = color)
		else: 
			self.text.insert(END,'Color not valid\n')
			return None


g = SimpleWorld()
g.title('Gui')
# label = g.la(text='Press the button.')
# button = g.bu(text='Make button', command=make_button)
# button2 = g.bu(text='Make circle', command=make_circle)
# button2 = g.bu(text='No, press me!',command=make_label)
# canvas = g.ca(width=500,height=200)
# canvas.config(bg='blue')
circle = None
# entry = g.en(text='Type here...')
# text = g.te(width=100, height=5)
# # text.insert(END, 'A line of text.')
# # text.insert(1.1,'nother')
# button3 = g.bu(text='send',command=send_text)
# button4 = g.bu(text='clear',command=clear_text)
# button5 = g.bu(text='change color',command=read_text)
g.mainloop()
