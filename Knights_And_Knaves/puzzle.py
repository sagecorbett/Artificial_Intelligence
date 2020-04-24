from logic import *

AKnight = Symbol("A is a Knight")
AKnave = Symbol("A is a Knave")

BKnight = Symbol("B is a Knight")
BKnave = Symbol("B is a Knave")

CKnight = Symbol("C is a Knight")
CKnave = Symbol("C is a Knave")

# Puzzle 0
# A says "I am both a knight and a knave."
knowledge0 = And(
    Or(AKnave, AKnight), # A is either a Knave or a Knight

    # And The implication that we as humans know is that a knave is not a knight 
    # And a Knight is not a Knave
    And(Implication(AKnave, Not(AKnight)), Implication(AKnight, Not(AKnave))), 

    # Finally the implication is that if A is Not a Knight and a
    # Knave then A is a Knave
    Implication(Not(And(AKnight, AKnave)), AKnave)
)


# Puzzle 1
# A says "We are both knaves."
# B says nothing.
knowledge1 = And(
    Or(AKnight, AKnave), # A is either a Knight or a Knave
    Or(BKnight, BKnave), # B is either a Knight or a Knave

    # We as Humans know you cannot be both
    And(Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave))),

    # For A to imply that they themself is a Knave then we know that 
    # what ever they are saying is false
    And(Not(And(AKnave, BKnave)), AKnave)
)

# Puzzle 2
# A says "We are the same kind."
# B says "We are of different kinds."
knowledge2 = And(
    Or(AKnight, AKnave),  # A is either a Knight or a Knave
    Or(BKnight, BKnave),  # B is either a Knight or a Knave

    # We as Humans know you cannot be both
    And(Not(And(AKnight, AKnave)), Not(And(BKnight, BKnave))),

    # A implies that they are both the same 
    And(Or(And(AKnight, BKnight), And(AKnave, BKnave))),

    # B implies that they are different kinds
    And(Or(AKnave, BKnight), Or(AKnight, BKnave)),

    # If A is a Knave then they must be lying and B is a Knight
    Implication(AKnave, And(AKnave, BKnight)),

    # If A is a Knight then they must both be Knights
    Implication(AKnight, And(AKnight, BKnight)),

    # If B is a Knave then they are the same kind
    Implication(BKnave, And(AKnave, BKnave)),

    # If B is a Knight then they are different kinds
    Implication(BKnight, And(BKnight, AKnave)) 

)

# Puzzle 3
# A says either "I am a knight." or "I am a knave.", but you don't know which.
# B says "A said 'I am a knave'."
# B says "C is a knave."
# C says "A is a knight."
knowledge3 = And(
    # TODO
)


def main():
    symbols = [AKnight, AKnave, BKnight, BKnave, CKnight, CKnave]
    puzzles = [
        ("Puzzle 0", knowledge0),
        ("Puzzle 1", knowledge1),
        ("Puzzle 2", knowledge2),
        ("Puzzle 3", knowledge3)
    ]
    for puzzle, knowledge in puzzles:
        print(puzzle)
        if len(knowledge.conjuncts) == 0:
            print("    Not yet implemented.")
        else:
            for symbol in symbols:
                if model_check(knowledge, symbol):
                    print(f"    {symbol}")


if __name__ == "__main__":
    main()
