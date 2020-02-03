import ast
import numpy as np

def opMap(op):
    return {
        ast.Add: lambda x, y: x+y,
        ast.Sub: lambda x, y: x-y,
        ast.Mult: lambda x, y: x*y,
        ast.Div: lambda x, y: x/y,
        ast.Pow: lambda x, y: pow(x, y),
    }[op]


class Calc:
    def __init__(self, chop=3):
        assert chop >= 1, "Precision must be greater than or equal to 1"
        self.chop = chop

    def roundNum(self, num):
        tmp = np.format_float_scientific(num)
        tmp_spl = tmp.split('e')
        return float('e'.join([tmp_spl[0][:1+self.chop+(num<0)],tmp_spl[1]]))

    def constructTree(self, expr):
        ret = ast.parse(expr, mode="eval").body
        return ret

    def evaluateTree(self, expr):
        if isinstance(expr, ast.Num):
            return self.roundNum(expr.n)

        return self.roundNum(opMap(type(expr.op))(self.evaluateTree(expr.left),
                                                  self.evaluateTree(expr.right)))

    def compute(self, expr):
        return self.evaluateTree(self.constructTree(expr))

if __name__ == "__main__":
    calc = Calc()
    # print(calc.compute("2 - 4 * (3**(8/3))"))
    print(calc.compute("1.25**2 + .5*1.25 -.00025"))
