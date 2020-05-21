from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
happiness = BayesNet([
    ('Sunny', '', 0.7),
    ('Raise', '', 0.01),
    ('Happy', 'Sunny Raise', {(T, T): 1.0, (T, F): 0.7, (F, T): 0.9, (F, F): 0.1})
    ])

print(enumeration_ask('Raise', dict(Sunny=T), happiness).show_approx())

print(enumeration_ask('Raise', dict(Happy=T, Sunny=T), happiness).show_approx())

'''
P(Raise | sunny) = <T=.01,F=.99>
The result makes sense as the sunny weather should not impact no the raise occurring.

P(Raise | happy ∧ sunny) = <T=.0142,F=.986>
The small increase also makes sense as raise and sunny could both make happy.

P(Raise | Sunny)= <.01,.99> 
P(Raise | Happy ∧ Sunny) = α P(C, t1, ¬t2) = α P(H | R, S) * P(R|S) = α P(H | R, S) * P(R)
= α <1*.01,.7*.99>
= <.0142,.986>

'''

print(enumeration_ask('Raise', dict(Happy=T), happiness).show_approx())

print(enumeration_ask('Raise', dict(Happy=T, Sunny=F), happiness).show_approx())

'''
P(Raise | happy) = <T=0.0185,F=.982>

P(Raise | happy ∧ ¬sunny) = <T=0.0833,F=0.917>

It makes sense because a raise would make a person happy than others.
Second also makes sense as chance of happiness is likely from something else from raise.
'''