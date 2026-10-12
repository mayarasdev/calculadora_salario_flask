
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route("/")
def index():
    return render_template("form.html")


@app.route("/resultado", methods=["POST"])
def resultado():
    try:
        texto_salario = request.form.get("salario", "").strip()

        if "," in texto_salario:
            texto_salario = texto_salario.replace(".", "").replace(",", ".")

        salario = float(texto_salario)
        dependentes = int(request.form.get("dependentes", "0"))

        if salario <= 0:
            raise ValueError

        if dependentes < 0:
            raise ValueError

    except (ValueError, TypeError):
        return (
            "Dados inválidos. Informe um salário positivo "
            "e um número de dependentes igual ou maior que zero.",
            400,
        )

    # Parâmetros simplificados para a simulação educativa.
    percentual_inss = 0.08
    percentual_vt = 0.06
    valor_por_dependente = 200.00

    inss = salario * percentual_inss
    vale_transporte = salario * percentual_vt
    valor_dependentes = dependentes * valor_por_dependente

    salario_liquido = (
        salario
        - inss
        - vale_transporte
        + valor_dependentes
    )

    return render_template(
        "resultado.html",
        salario=salario,
        dependentes=dependentes,
        percentual_inss=percentual_inss * 100,
        percentual_vt=percentual_vt * 100,
        inss=inss,
        vale_transporte=vale_transporte,
        valor_por_dependente=valor_por_dependente,
        valor_dependentes=valor_dependentes,
        salario_liquido=salario_liquido,
    )


if __name__ == "__main__":
    app.run(debug=True)








