import random

# prompt format "a something of a" + "subject" + "of something(optional)", + "comma-separated modifiers" + "4k, 8k"

subjects = []
styles = []
adjectives = []
aspect_ratios = ["3:2", "2:3"]
outfile = "prompts.txt"

def loadFile(filename, inarr):
    f = open(filename)
    for line in f:
        inarr.append(line.rstrip())

prompts = []
loadFile('subjects', subjects)
loadFile('styles', styles)
loadFile('adjectives', adjectives)

print(subjects)

prompt_count = 500
max_adjectives = 2
max_styles = 8

adj_count = random.randint(1, max_adjectives)
style_count = random.randint(1, max_styles)
subj_length = len(subjects)
adj_length = len(adjectives)
style_length = len(styles)
out = open(outfile, 'w')

for _ in range(prompt_count):
    new_prompt = "a "
    for _ in range(random.randint(1, max_adjectives) + 1):
        adj = random.randint(0,adj_length - 2)
        new_prompt = new_prompt + " " + adjectives[adj]
    subj = random.randint(0, subj_length - 2)
    new_prompt = new_prompt + " of a " + subjects[subj] + ","
    for _ in range(random.randint(1, max_styles) + 1):
        style = random.randint(0, style_length - 2)
        new_prompt = new_prompt + " " + styles[style] + ","
    new_prompt = new_prompt + " --ar " + aspect_ratios[random.randint(0,1)]
    out.write(new_prompt + "\n")
