from deap import gp, base, creator, tools, algorithms
from L_Systems import LSystem
from Evaluation_Mectrics import *
import datetime
import numpy as np
import os

def add(x):
    return '+' + x

def sub(x):
    return '-' + x

def brackets(a,b,c):
    return a + '[' + b + ']' + c

def F(x):
    return 'F' + x

pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(add, 1)
pset.addPrimitive(sub, 1)
pset.addPrimitive(F, 1)
pset.addPrimitive(brackets, 3)
pset.addTerminal('')
pset.renameArguments(ARG0='x')

def create_folder(folder):
    if not os.path.exists(folder):
        os.makedirs(folder)

################################################################

for tentative in range(10,11):
    for function in [mse_ssim]:

        if function == euclidianDistance or function == imed:
            creator.create("FitnessMax", base.Fitness, weights=(-1.0, ))
        elif function == mse_ssim:
            creator.create("FitnessMax", base.Fitness, weights=(1.0,))
            
        creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

        toolbox = base.Toolbox()
        toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
        toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
        toolbox.register("population", tools.initRepeat, list, toolbox.individual)
        toolbox.register("compile", gp.compile, pset=pset)

        expr = toolbox.individual()
        nodes, edges, labels = gp.graph(expr)

        if function == euclidianDistance:
            folder = f'ED_T_{tentative}'
        elif function == imed:
            folder = f'IMED_T_{tentative}'
        elif function == mse_ssim:
            folder = f'SSIM_T_{tentative}'
        
        create_folder(folder)

        def evaluate(individual):
            global gen

            gen = 0
            pai_1 = 'Output/_a/_a.png'
            pai_2 = 'Output/_b/_b.png'
            func = toolbox.compile(expr=individual)
            ret = func('F')
            name = f'eval_{gen}_{datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")}'
            sys = LSystem({'F' : ret}, 'F', 5, 6, 90, 25, (1250,1250))
            sys.run(folder, name)

            mse_ssim_1, ssim_1 = mse_ssim(pai_1, f'{folder}/{name}/{name}.png')
            mse_ssim_2, ssim_2 = mse_ssim(pai_2, f'{folder}/{name}/{name}.png')
            gen += 1
            return ((ssim_1 + ssim_2) // 2,)

        if tentative in [10]:
            pop = toolbox.population(n=10)
        else:
            pop = toolbox.population(n=2)

        for a in range(len(pop)):
            if a % 2 == 0:
                pop[a] = pop[a].from_string('brackets(brackets(x, add(x), x), sub(x), x)', pset)
            else:
                pop[a] = pop[a].from_string('brackets(brackets(brackets(x, add(x), x), sub(x), ""), x, "")', pset)

        toolbox.register("evaluate", evaluate)
        toolbox.register("select", tools.selTournament, tournsize=3)
        toolbox.register("mate", gp.cxOnePoint)
        toolbox.register("expr_mut", gp.genFull, min_=0, max_=2)
        toolbox.register("mutate", gp.mutUniform, expr=toolbox.expr_mut, pset=pset)

        stats_fit = tools.Statistics(lambda ind: ind.fitness.values)
        stats_size = tools.Statistics(len)
        mstats = tools.MultiStatistics(fitness=stats_fit, size=stats_size)
        mstats.register("avg", np.mean)
        mstats.register("std", np.std)
        mstats.register("min", np.min)
        mstats.register("max", np.max)

        hof = tools.HallOfFame(1)
        global gen
        gen = 0

        pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.05, 40, stats=mstats, halloffame=hof, verbose=True)

        with open('logs/log_' + folder + '.txt', 'w') as f:
            f.write(str(log))
        f.close()

        with open('logs/gen_' + folder + '.txt', 'w') as f:
            s = 0
            for i in log:
                if i['nevals'] != 0:
                    f.write(f'gen {i["gen"]} corresponds to eval {s} to {s + i["nevals"]}\n')
                    s += i['nevals']
        f.close()