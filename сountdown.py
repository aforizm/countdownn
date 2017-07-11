from tkinter import *
from delorean import Delorean
from datetime import *
import pickle, shelve

class Application(Frame):
	"""docstring for Application"""
	countdown = 0
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.AddWidgets()
	
	def AddWidgets(self):
		#надпись
		Label(self,
			  text = "Прошло дней",
			  font=("Bookman Old Style", 12)
			  ).grid(row = 0, column = 0, columnspan = 1, sticky = W)

		#счетчик
		self.count_lbl = IntVar()
		self.count_lbl.set(0)
		self.lbl = Label(self,
			  textvariable = self.count_lbl,
			  font=("Bookman Old Style", 12)
			  )
		self.lbl.grid(row = 0, column = 2, columnspan = 1, sticky = W)

		f = open('date.dat', 'rb')
		prev_date = pickle.load(f)		
		today = Delorean()
		
		countdown = today - prev_date
		self.count_lbl.set(countdown.days)
		f.close()
		
		#кнопка обнулить
		Button(self,
			text = "Обнулить",
			command = self.button_clkd,
			font=("Bookman Old Style", 12),
			).grid(row = 2, column = 0,  sticky = W)

	def button_clkd(self):
		today = Delorean()		
		f = open('date.dat', 'wb')
		pickle.dump(today, f)
		f.close
		

def main():
	root = Tk()
	root.title('Countdown')
	root.resizable(0,0)
	app = Application(root)
	root.mainloop()

if __name__ == "__main__":
	main()