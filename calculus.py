import math
def Calculus(x):
    sine = math.sin(x)
    cos = math.cos(x)
    tan = math.tan(x)
    return [sine,cos,tan]
print("sine", Calculus(1))
print("cos", Calculus(0))
print("tan", Calculus(-1))
