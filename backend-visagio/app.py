from flask import Flask, render_template, request, redirect, jsonify
from config import Config
from models import db, Colaborador, Avaliacao, Criterio, Nota
from sqlalchemy.exc import SQLAlchemyError
from datetime import date

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    db.create_all()


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/avaliar", methods=["POST"])
def avaliar():
    try:
        dados = request.form
        print("DADOS RECEBIDOS:", dados)

        nome = dados.get("nome")
        if not nome:
            return "Nome do colaborador é obrigatório", 400

        # Verifica ou cria colaborador
        colaborador = Colaborador.query.filter_by(nome=nome).first()
        if not colaborador:
            colaborador = Colaborador(nome=nome)
            db.session.add(colaborador)
            db.session.commit()

        # Cria nova avaliação
        nova_avaliacao = Avaliacao(
            colaborador_id=colaborador.id,
            data_avaliacao=date.today()
        )
        db.session.add(nova_avaliacao)
        db.session.flush()

        # Critérios do formulário
        criterios_map = {
            "sentimento_dono": "Sentimento de dono",
            "resiliencia": "Resiliencia nas adversidades",
            "organizacao": "Organizacao no trabalho",
            "aprendizado": "Capacidade de aprender",
            "team_player": "Ser \"team player\"",
            "qualidade": "Entregar com qualidade",
            "prazos": "Atender aos prazos",
            "eficiencia": "Fazer mais com menos",
            "criatividade": "Pensar fora da caixa"
        }

        for campo, descricao in criterios_map.items():
            valor = dados.get(campo)
            if not valor:
                return f"Campo obrigatório ausente: {campo}", 400

            criterio = Criterio.query.filter_by(descricao=descricao).first()
            if not criterio:
                return f"Critério não encontrado: {descricao}", 500

            nota = Nota(
                avaliacao_id=nova_avaliacao.id,
                criterio_id=criterio.id,
                nota=float(valor),
                justificativa=None
            )
            db.session.add(nota)

        db.session.commit()
        return redirect("/")

    except (ValueError, SQLAlchemyError) as e:
        db.session.rollback()
        return f"Erro ao processar avaliação: {str(e)}", 500


@app.route("/historico/<nome>")
def historico(nome):
    try:
        colaborador = Colaborador.query.filter_by(nome=nome).first()
        if not colaborador:
            return jsonify({"mensagem": "Colaborador não encontrado"}), 404

        avaliacoes = Avaliacao.query.filter_by(colaborador_id=colaborador.id).all()
        if not avaliacoes:
            return jsonify({"mensagem": "Nenhuma avaliação encontrada"}), 404

        historico = []
        for avaliacao in avaliacoes:
            notas = [float(n.nota) for n in avaliacao.notas]
            if notas:
                media = round(sum(notas) / len(notas), 2)
                if media > 4:
                    classificacao = "Excepcional"
                elif media >= 3.5:
                    classificacao = "Muito Bom"
                elif media >= 3:
                    classificacao = "Fez o Básico"
                else:
                    classificacao = "Precisa Melhorar"
            else:
                media = 0
                classificacao = "Sem notas"

            historico.append({
                "data": avaliacao.data_avaliacao.strftime("%d/%m/%Y"),
                "media": media,
                "classificacao": classificacao
            })

        return jsonify(historico)

    except Exception as e:
        return jsonify({"erro": str(e)}), 500

@app.route("/historico")
def pagina_historico():
    # Busca todos os colaboradores para preencher o select
    colaboradores = Colaborador.query.all()
    return render_template("historico.html", colaboradores=colaboradores)


if __name__ == "__main__":
    app.run(debug=True)
