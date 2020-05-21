
from probability import BayesNet, enumeration_ask, elimination_ask, gibbs_ask

# Utility variables
T, F = True, False

# From AIMA code (probability.py) - Fig. 14.2 - burglary example
cancer = BayesNet([
    ('Cancer', '', 0.01),
    ('Test1', 'Cancer', {T: 0.90, F: 0.2}),
    ('Test2', 'Cancer', {T: 0.90, F: 0.2})
    ])

# Compute P(Cancer | positive results on both tests)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=T), cancer).show_approx())

# Compute P(Cancer | a positive result on test 1, but a negative result on test 2)
print(enumeration_ask('Cancer', dict(Test1=T, Test2=F), cancer).show_approx())

'''
The results make sense because the chance of getting cancer is 
low while the chance of getting a false positive is high.

P(Cancer | Test1 ∧ Test2)=  α P(C, t1, t2) = α P(c) * P(t1| C) * P(t2| C)
= α <.01*.9*.9, .99*.2*.2>
= (1/.0081+.0396) <0.0081,0.0396>
= <0.17,0.83> 

P(Cancer | Test1 ∧ ¬Test2) = α P(C, t1, ¬t2) = α P(c) * P(t1| C) * P(¬t2| C)
= α <.01*.9*.2, .99*.2*.9>
= α <.0018,.1782>
= <.01,.99>

'''
