import pandas as pd
from L_Systems import LSystem
from Evaluation_Mectrics import *
from deap import base, creator, tools
import random

image_size = (1250,1500)
arvores = [
{
'name' : 'a',
'rules' : {'F': 'F[+F]F[-F]F'},
'axiom' : 'F',
'iterations' : 5,
'segment_length' : 3,
'alpha_zero' : 90,
'angle' : 25.7,
},
{
'name' : 'b',
'rules' : {'F': 'F[+F]F[-F][F]'},
'axiom' : 'F',
'iterations' : 5,
'segment_length' : 10, #5
'alpha_zero' : 90,
'angle' : 20,
},
{
'name' : 'c',
'rules' : {'F': 'FF-[-F+F+F]+[+F-F-F]'},
'axiom' : 'F',
'iterations' : 4,
'segment_length' : 12,
'alpha_zero' : 90,
'angle' : 22.5,
},
{
'name' : 'd',
'rules' : {'F': 'FF', 'X': 'F[+X]F[-X]+X'},
'axiom' : 'X',
'iterations' : 7,
'segment_length' : 2,
'alpha_zero' : 90,
'angle' : 20,
},
{
'name' : 'e',
'rules' : {'F': 'FF', 'X': 'F[+X][-X]FX'},
'axiom' : 'X',
'iterations' : 7,
'segment_length' : 2,
'alpha_zero' : 90,
'angle' : 25.7,
},
{
'name' : 'f',
'rules' : {'F': 'FF', 'X': 'F-[[X]+X]+F[+FX]-X'},
'axiom' : 'X',
'iterations' : 7,
'segment_length' : 2,
'alpha_zero' : 90,
'angle' : 22.5,
}]


class Arvore():

    def __init__(self, rules) -> None:
        self.name = random.randrange(100,10000)
        self.axiom = 'X'
        self.iterations = 6
        self.segment_length = 2
        self.alpha_zero = 90
        self.angle = 25.7
        self.rules = rules


"""
for arvore in arvores:
sys = LSystem(arvore['rules'], arvore['axiom'], arvore['iterations'], arvore['segment_length'], arvore['alpha_zero'], arvore['angle'], image_size)
sys.run('Output', arvore['name'])
"""

# euclidianDistance MINIMIZE format == [y]
# templateMatching MAXIMIZE format == [[y]]
# mse_ssim

'''
imgaes = ['./Output/a/a.png', './Output/b/b.png', './Output/c/c.png', './Output/d/d.png', './Output/e/e.png', './Output/f/f.png']
functions = [euclidianDistance, templateMatching, mse_ssim]
list_df = []
for function in functions:
    df = []
    for image_a in imgaes:
        line = []
        for image_b in imgaes:
            line.append(function(image_a, image_b))
        df.append(line)
    df = pd.DataFrame(df, index=imgaes, columns=imgaes)
    list_df.append(df)

for df in list_df:
    print(df)

df.to_csv('results.csv')
'''
images = ['./Output/a/a.png', './Output/b/b.png', './Output/c/c.png', './Output/d/d.png', './Output/e/e.png', './Output/f/f.png']
print(euclidianDistance(images[0], images[0]))
print(mse_ssim(images[0], images[0]))
print(euclidianDistance(images[0], images[1]))
print(mse_ssim(images[0], images[1]))
print(euclidianDistance(images[0], images[2]))
print(mse_ssim(images[0], images[2]))



"""# Creating fitness function and individual
creator.create("FitnessMax", base.Fitness, weights=(1.0,))
creator.create("Individual", list, fitness=creator.FitnessMax)

def initPopulation():    
    return arvores

# Creating toolbox
toolbox = base.Toolbox()
toolbox.register("attr_arvore", random.choice, ['F', '+', '-'])
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_arvore, n=len(arvores))
toolbox.register("population", tools.initRepeat, list, toolbox.individual)


ind = toolbox.individual()
pop = toolbox.population(n=3)

def evalOneMax(individual):
    return sum(individual),

toolbox.register("evaluate", evalOneMax)
toolbox.register("mate", tools.cxTwoPoint)
toolbox.register("mutate", tools.mutFlipBit, indpb=0.05)
toolbox.register("select", tools.selTournament, tournsize=3)


print(pop)
print(pop[0])
"""
