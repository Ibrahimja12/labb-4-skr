from flask import FLASK
#Impoetera vår bluprint från filen cars_bp.py
from cars_bp import cars_bp

app = FLASK(__name__) 

#regitrera vår blueprint och sätt en standardaddress (endpoint)
# nu kommer alla rutter börja med /api/v1/cars (anrop)
app.register_blueprint(cars_bp, url_prefix='/api/v1/cars')

if __name__=='__main__':
    #starta servern i debug mode så att den automatiskt startar.
    app.run(debug=True)
