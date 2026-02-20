from flask import blureprint, request, jsonify
import json
import os

#Skapa en blueprint för våra bilar
cars_bp = blureprint('cars_bp', __name__)
#Skapa en variabel för att lagra sökvägen till vår JSON-fil
JSON_FILE = 'cars.json'

# Hjälp funktion för att läsa och skriva till JSON-filen då slipper vi upprepa kod
def read_cars(): 
    # kollar om filen finnis, annars returnerar en tom lista
    if not os.path.exists(JSON_FILE):
        return []
    with open(JSON_FILE, 'r', encoding='utf-8') as file:
        return json.load(file) 
def save_cars(cars):
    # sparar vår lista med bilar tillbaka till json-fieln
    with open(JSON_FILE, 'w', encoding='utf-8') as file:
        json.dump(cars, file, indent=4) 

# operationer för våra bilar (CRUD)
# READ(1) - Hämta alla bilar
@cars_bp.route('/', methods=['GET'])
def get_all_cars():
    all_cars = read_cars()
    return jsonify(all_cars), 200  
# READ(2) - Hämta en specifik bil med registreringsnummer
@cars_bp.route('/<string:reg_number>', methods=['GET'])
def get_one_car(reg_number):
    all_cars = read_cars()

    # loopa igenom alla bilar och hitta den rätt reg_number
    for car in all_cars:
        if car['reg_num'] == reg_num.upper():
            return jsonify(car), 200
    #om loopen inte hittar någon bil så returnerar vi ett felmeddelande
    return jsonify({"error": "bilen hittades inte"}), 404 

# CREATE - Lägg till en ny bil
@cars_bp.route('/', methods=['POST'])
def add_car():
    all_cars = read_cars()
    new_car = request.get_json()

    # kollar så att användaren sckicade med ett reg_num i sin request, annars returnerar vi ett felmeddelande
    if not new_car or 'reg_num' not in new_car:
        return jsonify({"error": "reg_num saknas"}), 400
    
# kollar om bilen redan finnis i vår lista, om den gör det så returnerar vi ett felmeddelande
    for car in all_cars:
        if car['reg_num'] == new_car['reg_num']:
            return jsonify({"error": "bilen med detta reg_num finns redan"}), 400
    all_cars.append
    save_cars

    return jsonify(new_car), 201

# UPDATE - uppdatera en bil med registreringsnummer
@cars_bp.route('/<string:reg_num>', methods=['PUT'])
def update_car(reg_num):
    all_cars = read_cars()
    updated_car = request.get_json()
    reg_num = reg_num.upper()

    for car in all_cars:
        if car['reg_num'] == reg_num:
            # uppdaterar bilens information (men behåller reg_num)
            car['brand'] = updated_data.get('brand', car['brand'])
            car['model'] = updated_data.get('model', car['model'])
            car['price'] = updated_data.get('price', car['price'])

            save_cars(all_cars)
            return jsonify(car), 200
        
    return jsonify({"error": "bilen hittades inte"}), 404
#5. Delete (Ta bort en bil via registeringsnummer)
@cars_bp.route('/<string:reg_num>', methods=['Delete'])
def delete_car(reg_num):
    all_cars = read_cars()
    reg_num = reg_num.upper()

    #Vi skapar en ny lista som innehåller alla bilar utom den som ska tas bort
    updated_cars = [car for car in all_cars if car['regn_num'] != reg_num]

    #Om listorna är lika långa fanns inte bilen
    if len(all_cars) == len(updated_cars):
        return jsonify({"error": f"Bilen med regnr {reg_num} finns inte"}), 404
    
    save_cars (updated_cars)
    return jsonify({"message": f"Bilen med regnr {reg_num} har tagits bort"}), 200
                                            
