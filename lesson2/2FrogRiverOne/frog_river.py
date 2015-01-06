# https://codility.com/demo/results/demoG8FSMD-H4Y

def solution(X, A):
    count = [0] * X
    found = 0
    for i, a in enumerate(A):
        count[a-1] += 1
        if count[a-1] == 1:
            found += 1
        if found == X:
            return i
    return -1


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

ok((5, [1, 3, 1, 4, 2, 3, 5, 4]), 6)
ok((5, [1, 3, 1, 4, 2, 3, 4, 4]), -1)
ok((5, [1, 3, 1, 4, 2, 3, 5, 5, 4]), 6)
ok((5, [1, 3, 1, 4, 2, 3, 4, 5, 4]), 7)
ok((1, [1, 1]), 0)

# -----------------------------
print
print "-" * 40
if failures:
    for case in failures:
        print "case {}: got {}, expected {}".format(*case)
else:
    print "ok"
