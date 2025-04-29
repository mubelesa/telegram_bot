from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
import requests

PANDASCORE_TOKEN = "_G0vK5dIdMMlnYykY4OoWJWT4mxsOmlePzIc71lOG31jKX9t35M"  # Token de acesso à API da Pandascore (substitua pelo seu token)
# ⚠️ Lembre-se de manter o token em segredo e não expô-lo publicamente.
TEAM_ID = 1656  # ID da FURIA na Pandascore (confirmado)

headers = {
    "Authorization": f"Bearer {"_G0vK5dIdMMlnYykY4OoWJWT4mxsOmlePzIc71lOG31jKX9t35M"}"
}

# 🔥 Comandos

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🔥 Bem-vindo ao FURIA Bot!\n"
        "Comandos disponíveis:\n"
        "/agenda - Próximos jogos\n"
        "/elenco - Jogadores do time\n"
        "/curiosidades - Fatos sobre a FURIA\n"
        "/sobre - Sobre este bot"
    )

# 📅 Agenda via Pandascore
async def agenda(update: Update, context: ContextTypes.DEFAULT_TYPE):
    url = f"https://api.pandascore.co/csgo/matches/upcoming?filter[opponent_id]={TEAM_ID}&sort=begin_at"
    r = requests.get(url, headers=headers)
    if r.status_code != 200:
        await update.message.reply_text("Erro ao buscar os jogos.")
        return

    data = r.json()
    if not data:
        await update.message.reply_text("Nenhum jogo encontrado.")
        return

    msg = "📅 Próximos jogos da FURIA:\n"
    for match in data[:3]:
        teams = " vs ".join([team["name"] for team in match["opponents"]])
        date = match["begin_at"].replace("T", " ").split("+")[0]
        msg += f"- {teams} em {date}\n"

    await update.message.reply_text(msg)

# 🧑‍🤝‍🧑 Elenco atual (mock, pois Pandascore não dá elenco por padrão)
async def elenco(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🎮 Elenco CS2 Atual:\n"
        "- KSCERATO\n"
        "- yuurih\n"
        "- FalleN\n"
        "- chelo\n"
        "- arT"
    )

async def curiosidades(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "📌 Curiosidade:\n"
        "- A FURIA foi o primeiro time brasileiro a montar base nos EUA!\n"
        "- O estilo agressivo é uma marca registrada da equipe."
    )

async def sobre(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "🤖 Este bot foi criado como parte de um desafio técnico para a FURIA.\n"
        "Feito em Python usando a API Pandascore."
    )

# 🚀 Inicializa o bot
def main():
    app = ApplicationBuilder().token("7776998408:AAGnrBU-XrXJKKtN-37K2Yzgm97RO9oy-e8").build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("agenda", agenda))
    app.add_handler(CommandHandler("elenco", elenco))
    app.add_handler(CommandHandler("curiosidades", curiosidades))
    app.add_handler(CommandHandler("sobre", sobre))

    print("Bot rodando...")
    app.run_polling()

if __name__ == "__main__":
    main()
