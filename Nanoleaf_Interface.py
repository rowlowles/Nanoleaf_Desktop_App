from nanoleaf import setup, Aurora
from tkinter import *
from tkinter import messagebox
import os

ips = None

while not ips:
    ips = setup.find_auroras(1)
token = 'z9HOW4b7ewPUvX2QKBjwVIRcOeaS1jA1'

aurora = Aurora(ips[0], token)
aurora.on = True
#aurora.effect = "Nemo"

def getEffects():
    all_effects = aurora.effects_list
    rhythm_effects = []
    effects = []
    for effect in all_effects:
        try:
            if aurora.effect_details(effect)['pluginType']:
                rhythm_effects.append(effect)
        except:
            effects.append(effect)
    return [effects, rhythm_effects]

def controlWindow(effect_lists):
    class Application(Frame):

        def multiComb(self, name):
            aurora.effect = name

        def createWidgets(self):
            Label(text="Nanoleaf Control" ,font=("Helvetica", 15)).pack()
            left = Frame(root)
            right = Frame(root)
            left.pack(side = LEFT)
            right.pack(side = RIGHT)

            Label(text = "Effects",font=("Helvetica", 12)).pack(in_ = left)
            Label(text = "Rhythms",font=("Helvetica", 12)).pack(in_ = right)

            for effect in effect_lists[0]:
                # Create N buttons, one for each N items in list, and create functions for each
                Button(text=effect, command=lambda x=effect: self.multiComb(x), bd=2, height=2, font=
                ('Helvetica', 10), width=20).pack(in_ = left)

            for rhy_effect in effect_lists[1]:
                Button(text=rhy_effect, command=lambda x=rhy_effect: self.multiComb(x), bd=2, height=2, font=
                ('Helvetica', 10), width=20).pack(in_ = right)

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.pack()
            self.createWidgets()

    def on_closing():
        if messagebox.askokcancel("Quit", "Do you want to quit?"):
            os._exit(1)

    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = Application(master=root)
    root.title("Nanoleaf")
    root.geometry('+%d+%d' % (100, 100))
    app.mainloop()
    root.destroy()

def main():
    effect_options = getEffects()
    controlWindow(effect_options)

if __name__ == "__main__":
    main()