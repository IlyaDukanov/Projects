import urllib.request
from tkinter import *

class Application(Frame):
	def __init__(self, master):
		super(Application, self).__init__(master)
		self.grid()
		self.create_widgets()

	def create_widgets(self):
		Label(self,
			text = 'Write a url of the file: '
			).grid(row = 0, column = 0, sticky = W)
		self.url_ent = Entry(self)
		self.url_ent.grid(row = 0, column = 1, sticky = W)
		Label(self,
			text = 'Write a name of the file: '
			).grid(row = 1, column = 0,sticky = W)
		self.name_ent = Entry(self)
		self.name_ent.grid(row = 1, column = 1,sticky = W)
		self.res_txt = Text(self, width = 40, height = 1, wrap = WORD)
		self.res_txt.grid(row = 2, column = 0, sticky = W)
		Button(self,
			text = 'Download',
			command = self.download
			).grid(row = 3, column = 0, sticky = W)

	def download(self):
		url = self.url_ent.get()
		name = self.name_ent.get()	
		try:
			urllib.request.urlretrieve(url,name)
		except urllib.request.HTTPError:
			self.res_txt.delete(0.0, END)
			self.res_txt.insert(0.0, 'Bad')
		else:
			self.res_txt.delete(0.0, END)
			self.res_txt.insert(0.0, 'Good')

root = Tk()
root.title('Download files')
app = Application(root)
root.mainloop()					