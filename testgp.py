from deap import base, creator, gp, tools

def F(x):
    return 'F' + x 

def brackets(a, b, c):
    return a + '[' + b + ']' + c

def add(x):
    return '+' + x

def sub(x):
    return '-' + x

pset = gp.PrimitiveSet("MAIN", 1)
pset.addPrimitive(F, 1)
pset.addPrimitive(brackets, 3)
pset.addPrimitive(add, 1)
pset.addPrimitive(sub, 1)
pset.addTerminal('none', '')
pset.renameArguments(ARG0='x')

creator.create("Individual", gp.PrimitiveTree)

toolbox = base.Toolbox()
toolbox.register("expr", gp.genHalfAndHalf, pset=pset, min_=1, max_=2)
toolbox.register("individual", tools.initIterate, creator.Individual, toolbox.expr)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)
toolbox.register("compile", gp.compile, pset=pset)

expr = toolbox.individual()
nodes, edges, labels = gp.graph(expr)

### Graphviz Section ###