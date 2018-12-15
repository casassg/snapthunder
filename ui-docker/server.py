import logging
import os
import json

from flask import Flask, request, json, render_template
import psycopg2

app = Flask(__name__)

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

logging.basicConfig(
    format='%(asctime)s.%(msecs)s:%(name)s:%(thread)d:%(levelname)s:%(process)d:%(message)s',
    level=logging.INFO
)

@app.route('/')
def home():
    return render_template('query.html', chromosomes=sorted(['chr1_KI270712v1_random', 'chr22_KI270733v1_random', 'chrUn_KI270748v1', 'chr15', 'chrUn_KI270757v1', 'chrUn_KI270507v1', 'chr2_KI270716v1_random', 'chrUn_KI270750v1', 'chrM', 'chrUn_KI270515v1', 'chr1_KI270709v1_random', 'chrUn_KI270333v1', 'chrUn_KI270538v1', 'chr22_KI270736v1_random', 'chrUn_KI270336v1', 'chr14_GL000009v2_random', 'chr22_KI270739v1_random', 'chr7', 'chr11', 'chr5', 'chr17_KI270730v1_random', 'chrUn_KI270751v1', 'chr19', 'chr13', 'chrUn_GL000195v1', 'chr9_KI270717v1_random', 'chrUn_KI270509v1', 'chr14_GL000194v1_random', 'chrUn_KI270741v1', 'chr16_KI270728v1_random', 'chr22_KI270731v1_random', 'chr3', 'chrUn_KI270468v1', 'chrUn_KI270755v1', 'chrUn_KI270579v1', 'chr2', 'chrUn_KI270588v1', 'chr9', 'chrUn_GL000216v2', 'chr14_KI270725v1_random', 'chrUn_GL000214v1', 'chr22_KI270737v1_random', 'chrUn_KI270754v1', 'chr18', 'chrUn_KI270753v1', 'chrUn_KI270311v1', 'chrUn_KI270756v1', 'chrUn_KI270752v1', 'chrUn_GL000218v1', 'chrUn_KI270589v1', 'chrUn_KI270584v1', 'chrUn_KI270466v1', 'chr22_KI270738v1_random', 'chrUn_KI270519v1', 'chr6', 'chr1_KI270708v1_random', 'chr14_KI270724v1_random', 'chrUn_KI270742v1', 'chr14_GL000225v1_random', 'chr1_KI270713v1_random', 'chr17_KI270729v1_random', 'chr1_KI270714v1_random', 'chr14', 'chrUn_GL000213v1', 'chr21', 'chr2_KI270715v1_random', 'chrUn_KI270587v1', 'chrUn_KI270516v1', 'chr17', 'chr14_KI270726v1_random', 'chrUn_KI270517v1', 'chrUn_KI270435v1', 'chr1_KI270711v1_random', 'chr3_GL000221v1_random', 'chrY', 'chrUn_KI270465v1', 'chrUn_KI270364v1', 'chrUn_KI270330v1', 'chr14_KI270723v1_random', 'chrUn_KI270438v1', 'chr9_KI270719v1_random', 'chrUn_KI270744v1', 'chr22_KI270732v1_random', 'chr17_GL00chr17_GL00chr17_G10',  'chr1', 'chr22',
    ]))

@app.route('/query', methods=['POST'])
def submit():
    sql = """
    SELECT * 
    FROM intron 
    WHERE chrom = '{chrm}' 
        AND "start" >= {start} 
        AND "start" <= {end} 
        AND "end" <= {end}
            AND samples_count >= {samples_count}
    order by snaptron_id
    LIMIT 5
    """.format(chrm=request.form.get('chrm','chr1'), start=request.form.get('start',0), end=request.form.get('end',0), samples_count=request.form.get('samples_count',0))
    
    host = '{chr}postgres.default.svc.cluster.local'.format(chr=request.form.get('chrm','chr1'))
    # host = 'localhost'
    # sconn = psycopg2.connect(dbname="admin", user="admin", host=host)
    sconn = psycopg2.connect(dbname="postgres", user="postgres", host=host)
    snc = sconn.cursor()
    snc.execute(sql)
    results = snc.fetchall()
    snc.close()
    return json.dumps([{'text':','.join(map(str,r))} for r in results])


@app.route('/query_all', methods=['POST'])
def submit_all():
    sql = """
    SELECT * 
    FROM intron 
    WHERE chrom = '{chrm}' 
        AND "start" >= {start} 
        AND "start" <= {end} 
        AND "end" <= {end}
            AND samples_count >= {samples_count}
    order by snaptron_id
    """.format(chrm=request.form.get('chrm','chr1'), start=request.form.get('start',0), end=request.form.get('end',0), samples_count=request.form.get('samples_count',0))
    
    host = '{chr}postgres.default.svc.cluster.local'.format(chr=request.form.get('chrm','chr1'))
    # host = 'localhost'
    # sconn = psycopg2.connect(dbname="admin", user="admin", host=host)
    sconn = psycopg2.connect(dbname="postgres", user="postgres", host=host)
    snc = sconn.cursor()
    snc.execute(sql)
    return json.dumps(snc.fetchall())

if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0')