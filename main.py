from flask import Flask, jsonify, request
from postgre_connector import query, execute

app = Flask(__name__)

@app.route("/musicos", methods=["GET"])
def get_musicos():
    json = []
    result = query("SELECT * FROM musicos;")

    for data in result:
        json.append({
            "codigo": data[0],
            "nome": data[1],
            "genero_musical": data[2],
            "musica_mais_famosa": data[3]
        })

    return jsonify(json)

@app.route("/musicos", methods=["POST"])
def post_musicos():
    data = request.get_json()
    nome = data.get('nome')
    genero_musical = data.get('genero_musical')
    musica_mais_famosa = data.get('musica_mais_famosa')

    print(execute(f"INSERT INTO musicos(nome, genero_musical, musica_mais_famosa) VALUES ('{nome}', '{genero_musical}', '{musica_mais_famosa}');"))

    return "POST Funcionando"

@app.route("/musicos", methods=["PUT"])
def put_musicos():
    data = request.get_json()
    id = data.get('id')
    nome = data.get('nome')
    genero_musical = data.get('genero_musical')
    musica_mais_famosa = data.get('musica_mais_famosa')

    execute(f"""UPDATE musicos
                SET nome = '{nome}',
                    genero_musical = '{genero_musical}',
                    musica_mais_famosa = '{musica_mais_famosa}'
                WHERE id = {id}""")

    return "PUT Funcionando"

@app.route("/musicos", methods=["DELETE"])
def delete_musicos():
    data = request.get_json()
    nome = data.get('nome')

    execute(f"DELETE FROM musicos WHERE nome = '{nome}'")

    return "DELETE Funcionando"


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    app.run(debug=True)
