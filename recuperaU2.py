#Author:Estrad Angeles
#Fecha:05/11/2025

from flask import Flask, request, jsonify, render_template_string

app = Flask(__name__)

dispositivos = {}

# Mostrar los dispositivos
@app.route('/dispositivos_html', methods=['GET'])
def mostrar_dispositivos_html():
    html = """
        <html>
    <head>
        <title>Listado de Dispositivos</title>
        <style>
            table {
                border-collapse: collapse;
                width: 100%;
                background: purple;
                font-family: cursive;
            }
            th, td {
                border: 2px solid #000000;
                padding: 5px;
                text-align: left;
            }
            th {
                background-color: black;
            }
        </style>
    </head>
    <body>
        <center><h1>Diccionario de dispositivos</h1></center>

        <table>
            <thead>
                <tr>
                    <th>ID</th>
                    <th>Nombre</th>
                    <th>Descripción</th>
                    <th>IP</th>
                    <th>MAC</th>
                    <th>Ubicación</th>
                    <th>Tipo</th>
                    <th>Otros</th>
                </tr>
            </thead>
            <tbody>
                {% for d in dispositivos.values() %}
                <tr>
                    <td>{{ d.id }}</td>
                    <td>{{ d.nombre }}</td>
                    <td>{{ d.descripcion }}</td>
                    <td>{{ d.ip }}</td>
                    <td>{{ d.mac }}</td>
                    <td>{{ d.ubicacion }}</td>
                    <td>{{ d.tipo }}</td>
                    <td>{{ d.otros }}</td>
                </tr>
                {% endfor %}
            </tbody>
        </table>

    </body>
</html>

    """
    return render_template_string(html, dispositivos=dispositivos)

#Agregamos dispositivos
@app.route('/dispositivos', methods=['POST'])
def agregar_dispositivo():
    data = request.get_json()
    if not data or "id" not in data:
        return jsonify({"error": "Faltan datos o ID"}), 400


    dispositivos[data["id"]] = data
    return jsonify({"mensaje": "Dispositivo agregado", "dispositivo": data}), 201

#modificar dispositivos 
@app.route('/dispositivos',methods=['PUT'])
def modificar_dispositivos():
    data = request.get_json()
    return jsonify({"mensaje": "Dispositivos agregado", "dispositivo": data}),201


@app.route('/dispositivos/<id>', methods=['PUT'])
def modificar_dispositivo(id):
    if id not in dispositivos:
        return jsonify({"error": "Dispositivo no encontrado"}), 404


    data = request.get_json()
    for clave, valor in data.items():
        dispositivos[id][clave] = valor


    return jsonify({"mensaje": "Dispositivo modificado", "dispositivo": dispositivos[id]}), 200

@app.route('/', methods=['GET'])
def test():
    return "API funcionando correctamente"





if __name__ == '__main__':
    app.run(debug=True)