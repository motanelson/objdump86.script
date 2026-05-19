import tkinter as tk
txt=""
class myapp:
    def __init__(self,root:tk.Tk):
        
        self.root=root
        self.root.title("hello world.......")
        self.root.configure(background="black")
        self.entry1=tk.Entry(background="black",foreground="white")
        self.entry1.pack(padx=10,pady=10)
        self.bt1= tk.Button(background="black",foreground="white",command=self.hello,text="press me")
        self.bt1.pack(padx=10,pady=10)
    def hello(self):
        print(self.entry1.get())






root=tk.Tk()
apps=myapp(root)
root.mainloop()
print(txt)