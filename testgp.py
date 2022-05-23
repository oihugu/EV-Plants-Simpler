from deap import gp, base, creator, tools, algorithms
from L_Systems import LSystem
from Evaluation_Mectrics import *
import datetime

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

creator.create("FitnessMax", base.Fitness, weights=(1.0, -1.0))
creator.create("Individual", gp.PrimitiveTree, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

expr = toolbox.individual()
nodes, edges, labels = gp.graph(expr)



def evaluate(individual):
    pai_1 = 'Output/a/a.png'
    pai_2 = 'Output/b/b.png'
    func = toolbox.compile(expr=individual)
    ret = func('F')
    name = f'test_{datetime.datetime.now().strftime("%Y%m%d%H%M%S.%f")}'
    sys = LSystem({'F' : ret}, 'F', 5, 7, 90, 25, (1250,1250))
    sys.run('Temp_1', name)

    #mse_ssim_1, ssim_1 = mse_ssim(pai_1, f'Temp_1/{name}/{name}.png')
    #mse_ssim_2, ssim_2 = mse_ssim(pai_2, f'Temp_1/{name}/{name}.png')
    return (euclidianDistance(pai_1, f'Temp_1/{name}/{name}.png') + euclidianDistance(pai_2, f'Temp_1/{name}/{name}.png')) // 2

pop = toolbox.population(n=2)

pop[0] = pop[0].from_string('brackets(brackets(x, add(x), x), sub(x), x)', pset)
pop[1] = pop[1].from_string('brackets(brackets(brackets(x, add(x), x), sub(x), ""), x, "")', pset)

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
pop, log = algorithms.eaSimple(pop, toolbox, 0.5, 0.1, 40, stats=mstats, halloffame=hof, verbose=True)