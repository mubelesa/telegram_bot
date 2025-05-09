# 🤖 FURIA Bot - Telegram Chatbot com Pandascore API

Este bot foi criado como parte de um desafio técnico para a FURIA, com o objetivo de aproximar os fãs do time de CS2 com uma experiência conversacional prática e divertida.

## 🔥 Funcionalidades

- `/start` – Boas-vindas e comandos
- `/agenda` – Próximos jogos do time via Pandascore API
- `/elenco` – Elenco atual (mock)
- `/curiosidades` – Fatos interessantes
- `/sobre` – Informações sobre o projeto

## 💻 Como rodar

1. Clone o repositório:
```bash
git clone https://github.com/mubelesa/telegram_bot__FURIA_ESports
cd telegram_bot__FURIA_ESports
```

2. Instale dependências:
```bash
pip install python-telegram-bot requests
```

3. Substitua os tokens no `furiabelesa_bot.py`.

4. Rode:
```bash
python furiabelesa_bot.py
```

## 📌 Observações

- A Pandascore requer token para uso da API.
- O comando `/elenco` é mockado por falta de endpoint direto.

## 📄 Licença

MIT
