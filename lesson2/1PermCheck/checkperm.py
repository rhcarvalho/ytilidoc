# https://codility.com/demo/results/demo2M8N4P-8CU

from collections import Counter

def solution(A):
    count = Counter(A)
    for i in xrange(1, len(A) + 1):
        if count[i] != 1:
            return 0
    return 1


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

ok([4, 1, 3, 2], 1)
ok([4, 1, 3], 0)
ok([1, 1000000000], 0)
ok([1000000000], 0)
ok([1, 2, 3, 4, 5], 1)
ok([1, 1, 2], 0)
ok([1, 1, 2, 3], 0)

# -----------------------------
print
print "-" * 40
if failures:
    for case in failures:
        print "case {}: got {}, expected {}".format(*case)
else:
    print "ok"
