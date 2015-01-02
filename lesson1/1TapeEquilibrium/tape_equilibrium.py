# 1st try, scored 41% https://codility.com/demo/results/demo2Q2PHM-G4B/
# 2nd try, scored 100% https://codility.com/demo/results/demoQK975J-7WA/

import sys

INF = sys.maxint


def solution(A):
    s = sum(A)
    m = INF
    for p in xrange(1, len(A)):
        s -= 2 * A[p-1]
        m = min(m, abs(s))
    return m


# --------- little test framework ----------
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

ok([3, 1, 2, 4, 3], 1)
ok([-1, -2, -3], 0)
ok([-1, 2, -3], 0)
ok([100, 1], 99)
ok([1, 100], 99)
ok([1, 100, 1], 100)
ok([1, 100, -1], 98)
ok([1, 2, 3, 4, 5], 3)
ok([5, 4, 3, 2, 1], 3)


# -----------------------------
print
print "-" * 40
if failures:
    for case in failures:
        print "case {}: got {}, expected {}".format(*case)
else:
    print "ok"
