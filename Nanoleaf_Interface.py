from nanoleaf import setup, Aurora

ips = setup.find_auroras(5)
token = 'z9HOW4b7ewPUvX2QKBjwVIRcOeaS1jA1'

aurora = Aurora(ips[0], token)
aurora.on = True
#aurora.effect = "Nemo"

effects = aurora.effects_list
panels = aurora.panel_positions

rhythm_effects = []
for effect in effects:
    try:
        if aurora.effect_details(effect)['pluginType']:
            rhythm_effects.append(effect)
    except:
        pass


print (effects)
print (rhythm_effects)

print ("End of system")

def main():
    print ("Refacotr here")

if "__name__" == "__main__":
    main()