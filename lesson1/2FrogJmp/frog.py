# https://codility.com/demo/results/demoS4PWQ5-WZK/

import math

def solution(X, Y, D):
    return int(math.ceil((Y - X) / float(D)))


# --------- little test framework ----------
import sys
failures = []

def ok(inp, out):
    def run():
        s = solution(*inp)
        if s == out:
            return "."
        failures.append((inp, s, out))
        return "F"
    sys.stdout.write(run())

# ------------ tests ----------

ok((10, 85, 30), 3)
ok((1, 1, 1), 0)
ok((1, 2, 1), 1)
ok((1, 1000000000, 1), 1000000000-1)

# -----------------------------
print
print "-" * 40
if failures:
    for case in failures:
        print "case {}: got {}, expected {}".format(*case)
else:
    print "ok"
