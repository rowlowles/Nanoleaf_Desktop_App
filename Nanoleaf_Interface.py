from nanoleaf import setup, Aurora
import sys

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

def main():
    effect_options = getEffects()

if __name__ == "__main__":
    main()