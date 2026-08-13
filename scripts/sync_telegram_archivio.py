#!/usr/bin/env python3
"""
Scarica i PDF inviati dal bot Telegram @salvatore_omelie_bot (le omelie generate
dalle routine cloud) e li salva in 01_Parrocchia_e_Ministero/Omelie/.

Pensato per girare una volta al giorno, quando Salvatore è al PC (via LaunchAgent,
vedi setup_launchagent.sh nella stessa cartella). Idempotente: tiene traccia
dell'ultimo messaggio scaricato e del giorno in cui ha già sincronizzato, quindi
è sicuro rilanciarlo più volte senza scaricare doppioni o senza fare nulla se
oggi ha già sincronizzato.

SETUP UNA TANTUM (fatto una volta sola, poi lo script gira da solo):
1. pip3 install --user telethon
2. Vai su https://my.telegram.org/apps (login con lo stesso account Telegram
   usato per ricevere i messaggi del bot), crea un'app, annota api_id e api_hash.
3. Crea il file ~/.config/omelie_sync/config.json con questo contenuto:
   {"api_id": 1234567, "api_hash": "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx", "phone": "+39..."}
4. Esegui questo script UNA VOLTA A MANO da terminale (non via LaunchAgent):
   python3 sync_telegram_archivio.py
   La prima volta chiede il codice ricevuto su Telegram (e l'eventuale password
   2FA): dopo aver risposto crea un file di sessione riutilizzabile e le
   esecuzioni successive (anche automatiche) non richiedono più login.
"""
import asyncio
import json
import os
import sys
from datetime import date
from pathlib import Path

from telethon import TelegramClient

CONFIG_DIR = Path.home() / ".config" / "omelie_sync"
CONFIG_PATH = CONFIG_DIR / "config.json"
SESSION_PATH = CONFIG_DIR / "session"
STATE_PATH = CONFIG_DIR / "state.json"
ARCHIVE_DIR = Path(
    "/Users/salvatoremonte/Desktop/claude Workspace/01_Parrocchia_e_Ministero/Omelie"
)
BOT_USERNAME = "salvatore_omelie_bot"


def load_state():
    if STATE_PATH.exists():
        return json.loads(STATE_PATH.read_text())
    return {"last_message_id": 0, "last_sync_date": None}


def save_state(state):
    STATE_PATH.write_text(json.dumps(state, indent=2))


async def main():
    if not CONFIG_PATH.exists():
        print(f"Config mancante: {CONFIG_PATH}")
        print('Crea il file con: {"api_id": ..., "api_hash": "...", "phone": "+39..."}')
        sys.exit(1)

    cfg = json.loads(CONFIG_PATH.read_text())
    state = load_state()

    today = date.today().isoformat()
    force = "--force" in sys.argv
    if state.get("last_sync_date") == today and not force:
        print(f"Già sincronizzato oggi ({today}). Nulla da fare (usa --force per forzare).")
        return

    CONFIG_DIR.mkdir(parents=True, exist_ok=True)
    ARCHIVE_DIR.mkdir(parents=True, exist_ok=True)

    client = TelegramClient(str(SESSION_PATH), cfg["api_id"], cfg["api_hash"])
    await client.start(phone=cfg["phone"])

    entity = await client.get_entity(BOT_USERNAME)
    last_id = state.get("last_message_id", 0)
    new_last_id = last_id
    downloaded = []

    async for msg in client.iter_messages(entity, min_id=last_id, reverse=True):
        new_last_id = max(new_last_id, msg.id)
        if not msg.document:
            continue
        # Solo PDF
        if msg.document.mime_type != "application/pdf":
            continue
        filename = None
        for attr in msg.document.attributes:
            if hasattr(attr, "file_name") and attr.file_name:
                filename = attr.file_name
        filename = filename or f"Vangelo_msg{msg.id}.pdf"
        dest = ARCHIVE_DIR / filename
        if dest.exists():
            stem, ext = os.path.splitext(filename)
            dest = ARCHIVE_DIR / f"{stem}_{msg.id}{ext}"
        await client.download_media(msg, file=str(dest))
        downloaded.append(str(dest))

    state["last_message_id"] = new_last_id
    state["last_sync_date"] = today
    save_state(state)

    await client.disconnect()

    if downloaded:
        print(f"Scaricati {len(downloaded)} PDF in {ARCHIVE_DIR}:")
        for d in downloaded:
            print(" -", d)
    else:
        print("Nessun nuovo PDF trovato dal bot.")


if __name__ == "__main__":
    asyncio.run(main())
