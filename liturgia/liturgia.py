import requests
import re


def get_liturgia():
    r = requests.get("https://liturgia.up.railway.app/v2/")
    liturgia = r.json()

    pl = liturgia['leituras']['primeiraLeitura'][0]
    salmo = liturgia['leituras']['salmo'][0]
    sl = liturgia['leituras']['segundaLeitura'][0]
    ev = liturgia['leituras']['evangelho'][0]

    def limpar_ref(ref):
        return re.sub(r'[a-zA-Z]', '', ref)
    '''resposta = (
        f"📖 Liturgia do dia:\n\n"
        f"Data: {liturgia['data']}\n"
        f"Título: {liturgia['liturgia']}\n"
        f"Leituras:\n"
        f"Primeira Leitura: {primeira_leitura} ({limpar_ref(plRef)})\n"
        f"Salmo: {salmo} ({limpar_ref(salmoRef)})\n"
        f"Segunda Leitura: {segundaLeitura} ({limpar_ref(slRef)})\n"
        f"Evangelho: {evangelho} ({limpar_ref(evRef)})\n"
    )'''
    resposta = (
        "📖 <b>Liturgia do Dia</b>\n"
        f"📅 <i>{liturgia['data']}</i>\n\n"

        f"<b>{liturgia['liturgia']}</b>\n"
        "━━━━━━━━━━━━━━\n\n"

        "📘 <b>Primeira Leitura</b>\n"
        f"{pl['titulo']}\n"
        f"<i>{limpar_ref(pl['referencia'])}</i>\n\n"

        "🎶 <b>Salmo Responsorial</b>\n"
        f"{salmo['refrao']}\n"
        f"<i>{limpar_ref(salmo['referencia'])}</i>\n\n"

        "📗 <b>Segunda Leitura</b>\n"
        f"{sl['titulo']}\n"
        f"<i>{limpar_ref(sl['referencia'])}</i>\n\n"

        "✝️ <b>Evangelho</b>\n"
        f"{ev['titulo']}\n"
        f"<i>{limpar_ref(ev['referencia'])}</i>\n"
    )
    return resposta
