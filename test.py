from L_Systems import LSystem

rules = {'F': 'FF', 'X': 'F[+X][-X]FX'}
axiom = 'X'
iterations = 7
segment_length = 2
alpha_zero = 90
angle = 22.7


sys = LSystem(rules, axiom, iterations, segment_length, alpha_zero, angle)
sys.run()