# (77%) https://codility.com/demo/results/demoE7T88E-7FZ

def solution(N, A):
    count = [0] * N
    mx = 0
    for X in A:
        if 1 <= X <= N:
            # increase(X)
            count[X-1] += 1
            mx = max(mx, count[X-1])
        elif X == N+1:
            # max counter
            count = [mx] * N
    return count


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

ok((5, [3, 4, 4, 6, 1, 4, 4]), [3, 2, 2, 4, 2])
ok((5, [6, 6, 3, 4, 4, 6, 1, 4, 4]), [3, 2, 2, 4, 2])
ok((5, [3, 4, 4, 1, 4, 4]), [1, 0, 1, 4, 0])
ok((5, [1]), [1, 0, 0, 0, 0])
ok((5, [6]), [0, 0, 0, 0, 0])
ok((1, [1]), [1])
ok((2, [1, 1, 1, 1, 3, 1]), [5, 4])

# -----------------------------
print
print "-" * 40
if failures:
    for case in failures:
        print "case {}: got {}, expected {}".format(*case)
else:
    print "ok"
