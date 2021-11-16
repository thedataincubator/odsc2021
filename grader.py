# This file provides only stubs for the grader functionality

def check(expression):
    """Returns True if the expression is True, throws an exception if it is False.
       Replacement for assert in miniprojects"""
    if expression:
        return True
    else:
        raise ValueError("Check failed, please see comments in this cell for suggestions")
        
def score(question, ans):
    result = ans([0,1,2,3,4])
    val = len(set([0,1,4,9,16,25]).intersection(result)) / 5
    print("==================")
    print("Your score: {:.4f}".format(val))
    print("==================")
