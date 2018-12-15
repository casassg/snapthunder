import csv
import sqlite3
import timeit
MIL_25 = 2500000
MILL_25 = 25100000
NUM_EXECUTIONS = 4


def filter_query(end, snc):
    def f():
        snc.execute(
            "SELECT * FROM intron WHERE start>=0 AND start<= ? AND end<=? AND samples_count>=100",
            (end, end))
        snc.fetchall()

    return f

def filtercount_query(end, snc):
    def f():
        snc.execute("SELECT count(*) FROM intron WHERE start>=0 AND start<= ? AND end<=? AND samples_count>=100",
                    (end, end))
        snc.fetchall()

    return f

def simple_query(end, snc):
    def f():
        snc.execute("SELECT * FROM intron WHERE start>=0 AND start<= ? AND end<=?",
                    (end, end))
        snc.fetchall()

    return f

def simplecount_query(end, snc):
    def f():
        snc.execute("SELECT count(*) FROM intron WHERE start>=0 AND start<= ? AND end<=?",
                    (end, end))
        snc.fetchall()

    return f

def fetch_size(end, snc):
    snc.execute("SELECT count(*) FROM intron WHERE start>=0 AND start<= ? AND end<=?",(end, end))
    count_simple = snc.fetchone()[0]
    snc.execute("SELECT count(*) FROM intron WHERE start>=0 AND start<= ? AND end<=? AND samples_count>=100",(end, end))

    return count_simple, snc.fetchone()[0]

sconn = sqlite3.connect('./junctionschr1.sqlite')
snc = sconn.cursor()
print('Connected to DB')
times = [['end', 'time_simple', 'time_filter', 'time_simplecount', 'time_filtercount', 'simplecount', 'filtercount']]
for end in range(MIL_25, MILL_25, MIL_25):
    print('Query %d' % end)
    simplecount, filtercount = fetch_size(end,snc)
    simple_time = timeit.timeit(simple_query(end, snc), number=NUM_EXECUTIONS)
    print('Time simple: %s' % simple_time)
    filter_time = timeit.timeit(filter_query(end, snc), number=NUM_EXECUTIONS)
    print('Time filter: %s' % filter_time)
    filtercount_time = timeit.timeit(filtercount_query(end, snc), number=NUM_EXECUTIONS)
    print('Time filter count: %s' % filtercount_time)
    simplecount_time = timeit.timeit(simplecount_query(end, snc), number=NUM_EXECUTIONS)
    print('Time simple count: %s' % simplecount_time)

    times.append([end, simple_time, filter_time, simplecount_time, filtercount_time, simplecount, filtercount])

with open('new_times.csv', 'w+') as f:
    w = csv.writer(f)
    w.writerows(times)
