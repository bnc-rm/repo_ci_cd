from flask import Flask, request, render_template
import pickle
import os

application = Flask(__name__)

# preparo il classificatore addestrato deserializzando il file
cur_dir = os.path.dirname(__file__)
ppn = pickle.load(open(os.path.join(cur_dir, 
                                    'pkl_objects/perceptron.pkl'), 
                                    'rb'))

# preparo l'insieme di test X_test_std e i risultati attesi y_test
from sklearn import datasets
iris = datasets.load_iris()
X = iris.data[:, [2, 3]]
y = iris.target
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = \
    train_test_split(X, y, test_size=0.3, random_state=0)
from sklearn.preprocessing import StandardScaler
sc = StandardScaler()
sc.fit(X_train)
X_test_std = sc.transform(X_test)
risultati_attesi = list(iris.target_names) 

@application.route('/')
def index():
    tabella=[]
    cont=0     
    for i, j in X_test:
        cod_ris_atteso = y_test[cont]
        riga={'lunghezza':i,'larghezza':j, \
              'risultato':risultati_attesi[cod_ris_atteso],'record':cont}
        tabella.append(riga)
        cont=cont+1         
    return render_template('index.html', output=tabella)
	
@application.route('/results', methods=['GET'])
def results():
    if request.method == 'GET':
        record=int(request.args.get('record',''))
        return render_template('result.html', \
                               output=\
                               str(risultati_attesi\
                                [ppn.predict(X_test_std)[record]]))
		
if __name__ == "__main__":
    ENVIRONMENT_DEBUG = os.environ.get('APP_DEBUG', True)
    ENVIRONMENT_PORT = os.environ.get('APP_PORT', 80)
    application.run(host='0.0.0.0', 
                    port=ENVIRONMENT_PORT, 
                    debug=ENVIRONMENT_DEBUG)		