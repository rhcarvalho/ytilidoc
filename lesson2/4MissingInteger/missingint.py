# https://codility.com/demo/results/demoS5FA2D-JRT

def solution(A):
    N = len(A)
    count = [0] * N
    for i in xrange(N):
        if 1 <= A[i] <= N:
            count[A[i]-1] += 1
    for i, c in enumerate(count):
        if c == 0:
            return i + 1
    return N + 1


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

ok([1, 3, 6, 4, 1, 2], 5)
ok([-1, -1, 5], 1)
ok(xrange(1, 100001), 100001)
ok([1], 2)
ok([2], 1)

# -----------------------------
print
print "-" * 40
if failures:
    for case in failures:
        print "case {}: got {}, expected {}".format(*case)
else:
    print "ok"
