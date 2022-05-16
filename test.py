from L_Systems import LSystem

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

for arvore in arvores:
    sys = LSystem(arvore['rules'], arvore['axiom'], arvore['iterations'], arvore['segment_length'], arvore['alpha_zero'], arvore['angle'], image_size)
    sys.run('Output', arvore['name'])