# https://codility.com/demo/results/demo9R2B2Y-BMZ

def solution(A):
    return sum(xrange(1, len(A)+2)) - sum(A)


# --------- little test framework ----------
import sys
failures = []

def ok(A, out):
    def run():
        s = solution(A)
        if s == out:
            return "."
        failures.append((A, s, out))
        return "F"
    sys.stdout.write(run())

# ------------ tests ----------

ok([2, 3, 1, 5], 4)
ok([1, 2, 3, 4, 5, 7], 6)
ok([1], 2)
ok([2], 1)
ok([1, 2], 3)


# -----------------------------
print
print "-" * 40
if failures:
    for case in failures:
        print "case {}: got {}, expected {}".format(*case)
else:
    print "ok"
