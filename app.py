from flask import Flask, request,jsonify
from flask_mysqldb import MySQL
from models.user_modelo import User

app = Flask(__name__)
app.config["MYSQL_USER"] = "root"
app.config["MYSQL_PASSWORD"] = ""
app.config["MYSQL_DB"] = "learnmot"
# Extra configs, optional:
app.config["MYSQL_CURSORCLASS"] = "DictCursor"
app.config["MYSQL_CUSTOM_OPTIONS"] = {"ssl": {"ca": "/path/to/ca-file"}}
mysql = MySQL(app)


@app.route("/insertar_user", methods=['POST'])
def insertar_user():
    try:    
            user_data = request.json
            user = User(**user_data)
            
            cursor = mysql.connection.cursor()

            cursor.execute("INSERT INTO users(name, last_name, sex, role, email, password) VALUES(%s, %s, %s, %s, %s, %s)",
                       (user.nombre, user.apellido, user.sex, user.role, user.email, user.password))
            
 
            mysql.connection.commit()
            cursor.close()
            return jsonify({"informacion":"empleado registrado"})
    except Exception as error:
        return jsonify({"error": "Ocurrió un error al registrar el usuario", "details": str(error)}), 500

@app.route("/usuarios", methods=['GET'])
def mostrar():
 try:    
       
            cursor = mysql.connection.cursor()
            sql = "SELECT * FROM users"
            cursor.execute(sql)
            data = cursor.fetchall()
            cursor.close()
            return jsonify(data)
 except Exception as error:
        return jsonify({"error": "Ocurrió un error al mostrar los usuarios", "details": str(error)}), 500  
    
@app.route("/update/<int:id>", methods=['PUT'])
def update(id):
    try:    
            user_data = request.json
            user = User(**user_data)
            
            cursor = mysql.connection.cursor()

            cursor.execute("UPDATE users SET name = %s, last_name = %s, sex = %s, role = %s, email = %s, password = %s WHERE id = %s",
                       (user.nombre, user.apellido, user.sex, user.role, user.email, user.password,id))
            
 
            mysql.connection.commit()
            cursor.close()
            return jsonify({"informacion":"actualizado correctamente"})
    except Exception as error:
        return jsonify({"error": "Ocurrió un error al update el usuario", "details": str(error)}), 500
@app.route("/delete/<id>", methods=['DELETE'])
def delete(id):
 try:    
       
            cursor = mysql.connection.cursor()
            
            cursor.execute("DELETE FROM users WHERE id = %s",(id,))
            cursor.close()
            mysql.connection.commit()
            #print (data)
            return jsonify({"informacion":"eliminado correctamente"})
 except Exception as error:
        return jsonify({"error": "Ocurrió un error al eliminar los usuarios", "details": str(error)}), 500  

if __name__ == '__main__':
    app.run(debug=True, port=3000)