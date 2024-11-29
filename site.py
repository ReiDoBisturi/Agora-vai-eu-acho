from flask import Flask, render_template

app = Flask(__name__)

# criar a 1 pagina do site
# route -> hashtagtreinamentos.com/contatos
# função -> o que voce quer exibir na página
# template

@app.route("/")
def homepage():
    return render_template("homepage.html")


@app.route("/contatos")
def contatos():
    return render_template("contatos.html")




# colocar o site no ar
if __name__ == "__main__":
    app.run(debug=True)





