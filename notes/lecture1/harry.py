from logic import *

rain = Symbol("rain") # It is raining
hagrid = Symbol("hagrid") # Harry visited Hagrid
dumbledore = Symbol("dumbledore") # Harry visited Dumbledore

knowledge = And(
    Implication(Not(rain), hagrid), # if it is not raining harry visited hagrid
    Or(hagrid, dumbledore), # harry visited hagrid or dumbledore
    Not(And(hagrid, dumbledore)), # harry visited either hagrid or dumbledore but not both
    dumbledore # Harry visited dumbledore
)

print(model_check(knowledge, rain))