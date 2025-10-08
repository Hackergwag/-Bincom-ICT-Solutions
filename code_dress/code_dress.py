import re, psycopg2, random, statistics as st

# Extract colors from HTML (simulate scraping)
html = open('bincom_colors.html').read()
colors = re.findall(r'([A-Z]+)', html)
colors = [c.replace('BLEW', 'BLUE').replace('ARSH','ASH') for c in colors]

# Frequency dict
freq = {}
for c in colors:
    freq[c] = freq.get(c,0)+1
vals = list(freq.values())

# 1 Mean color (nearest to mean freq)
mean_color = min(freq, key=lambda k:abs(freq[k]-st.mean(vals)))
# 2 Most worn
most_color = max(freq, key=freq.get)
# 3 Median color
median_color = min(freq, key=lambda k:abs(freq[k]-st.median(vals)))
# 4 Variance
variance = st.pvariance(vals)
# 5 Prob of red
p_red = freq.get('RED',0)/len(colors)

print("Mean color:",mean_color)
print("Most worn:",most_color)
print("Median color:",median_color)
print("Variance:",variance)
print("P(red):",round(p_red,3))

# 6 Save to PostgreSQL
try:
    con=psycopg2.connect(dbname='bincom',user='postgres',password='1234',host='localhost')
    cur=con.cursor()
    cur.execute('CREATE TABLE IF NOT EXISTS colors(color TEXT, freq INT)')
    for c,f in freq.items():
        cur.execute('INSERT INTO colors VALUES(%s,%s)',(c,f))
    con.commit(); con.close()
    print("Data saved to DB.")
except Exception as e:
    print("DB skipped:",e)

# 7 Recursive search
def r_search(lst, x, i=0):
    return i if i<len(lst) and lst[i]==x else r_search(lst,x,i+1) if i<len(lst)-1 else -1
print("Recursive search:", r_search([2,4,6,8,10],8))

# 8 Generate random 4-bit binary and convert
b=''.join(str(random.randint(0,1)) for _ in range(4))
print("Binary:",b,"=>",int(b,2))

# 9 Sum first 50 Fibonacci
a,b,s=0,1,0
for _ in range(50): a,b=b,a+b; s+=a
print("Fibonacci sum:",s)