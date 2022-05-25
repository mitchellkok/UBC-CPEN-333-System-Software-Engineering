# student name: Mitchell Kok
# student number: 44572246
import math

def solveQuadratic(a: float, b: float, c: float) -> str:
    """
        This function takes the coefficients of a 
        quadratic equation as its three parameters.
        It returns a string that states its roots as
        described in the specification.
    """
    checkval = (b**2 - 4*a*c) # check discriminant
    if checkval < 0: 
        # no real roots
        return "No real roots"
    elif checkval == 0: 
        # one real root
        return "The root is " + f"{-b / (2*a):.2f}"
    else: 
        # two real roots
        r1 = (-b + math.sqrt(b**2 - 4*a*c)) / (2*a)
        r2 = (-b - math.sqrt(b**2 - 4*a*c)) / (2*a)
        return "The roots are " + f"{r1:.2f}" + " and " + f"{r2:.2f}"
        
if __name__ == "__main__":
    """ 
        We will ignore this part of the code.
        You can use it to test your function.
        Do not limit your testing to these test cases.
        Make sure that you fully test your code.
    """
    Tests = [(1, 2, 3), (1, 2, 1), (1, 3, 1), (1.5, -8, -0.2)] 
    expectedOutput = ["No real roots", 
                      "The root is -1.00",  
                      "The roots are -0.38 and -2.62",
                      "The roots are 5.36 and -0.02"]
    for i in range(len(Tests)):
        print(f"Test {i} : a={Tests[i][0]}, b={Tests[i][1]} c={Tests[i][2]}")
        result = solveQuadratic(a=Tests[i][0], b=Tests[i][1], c=Tests[i][2])
        print(result)
        assert(result == expectedOutput[i])