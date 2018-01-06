from nanoleaf import setup, Aurora
from tkinter import *

ips = None

while not ips:
    # Continuously search for an Aurora until it finds one. There have been issues with the Aurora not appearing even
    # after searching for a while. Retrying the statement fixes those issues.
    ips = setup.find_auroras(1)

# Authorization token to access the Aurora. Specific to the device.
token = 'z9HOW4b7ewPUvX2QKBjwVIRcOeaS1jA1'

# Authorize the Aurora using the IP address and token
aurora = Aurora(ips[0], token)

def get_effects():
    """
    Get a list of all the effects currently loaded on my Aurora and their details. Parse through the effects and split
    the list into passive effects and effects that make use of the Rhythm module on the Aurora. Return these lists.
    :return:
    """
    # Returns a JSON of all the effects and their details
    all_effects = aurora.effect_details_all()
    rhythm_effects = []
    effects = []

    for effect in all_effects['animations']:
        try:
            # 'pluginType' is only present for Rhythm effects, so this will be the attribute the list is split around
            if effect['pluginType']:
                rhythm_effects.append(effect['animName'])
        except:
            effects.append(effect['animName'])

    return [effects, rhythm_effects]


def control_window(effect_lists):
    class Application(Frame):
        # Create the GUI to control the Nanoleaf.

        def send_effect(self, name):
            # Send the effect to the Nanoleaf via the API
            aurora.effect = name

        def create_widgets(self):
            Label(text="Nanoleaf Control", font=("Helvetica", 15)).pack()

            left = Frame(root)
            right = Frame(root)
            left.pack(side=LEFT)
            right.pack(side=RIGHT)

            Label(text="Effects", font=("Helvetica", 12)).pack(in_=left)
            Label(text="Rhythms", font=("Helvetica", 12)).pack(in_=right)

            for effect in effect_lists[0]:
                # Create a button for every passive effect
                Button(text=effect, command=lambda x=effect: self.send_effect(x), bd=2, height=2, font=(
                    'Helvetica', 10), width=20).pack(in_=left)

            for rhy_effect in effect_lists[1]:
                # Create a button for every rhythm effect
                Button(text=rhy_effect, command=lambda x=rhy_effect: self.send_effect(x), bd=2, height=2, font=(
                    'Helvetica', 10), width=20).pack(in_=right)

        def __init__(self, master=None):
            Frame.__init__(self, master)
            self.pack()
            self.create_widgets()

    def on_closing():
        # Close the GUI
        root.destroy()

    root = Tk()
    root.protocol("WM_DELETE_WINDOW", on_closing)
    app = Application(master=root)
    root.title("Nanoleaf")
    root.geometry('+%d+%d' % (100, 100))
    app.mainloop()


def main():
    # Get the effects from the Aurora and then send them to the GUI.
    effect_options = get_effects()
    control_window(effect_options)


if __name__ == "__main__":
    main()
