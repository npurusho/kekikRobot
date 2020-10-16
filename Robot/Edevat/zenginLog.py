# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

import datetime, pytz
from Robot import LOG_ID, SESSION_ADI, log_ver
from pyrogram import Client
from pyrogram.types import Message

tarih   = lambda : datetime.datetime.now(pytz.timezone("Turkey")).strftime("%d-%m-%Y")
saat    = lambda : datetime.datetime.now(pytz.timezone("Turkey")).strftime("%H:%M:%S")

async def log_yolla(client:Client, message:Message):
    log_dosya   = f"[{saat()} | {tarih()}] "
    sohbet      = await client.get_chat(message.chat.id)

    if message.from_user.username:
        log_mesaj   = f"@{message.from_user.username}"
        log_konsol  = f"[bold red]@{message.from_user.username}[/] [green]||[/] "
        log_dosya  += f"@{message.from_user.username} | "
    else:
        log_mesaj   = f"[{message.from_user.first_name}](tg://user?id={message.from_user.id})"
        log_konsol  = f"[bold red]{message.from_user.first_name}[/] [green]||[/] "
        log_dosya  += f"{message.from_user.first_name} | "

    if message.chat.type in ['private', 'bot']:
        log_mesaj   += f"\n\n\t\t`{message.text}` __yolladı..__"
        log_konsol  += f"[yellow]{message.text}[/] "
        log_dosya   += f"{message.text} "
    else:
        grup_ad      = f'@{sohbet.username}' if sohbet.username else sohbet.title
        log_mesaj   += f"\n\n\t\t**{grup_ad}**__'den__ \n\n\t`{message.text}` __yolladı..__"
        log_konsol  += f"[yellow]{message.text}[/]\t[green]||[/] [bold cyan]{grup_ad}[/] "
        log_dosya   += f"{message.text} | {grup_ad} "

    log_mesaj   +=  f"\n\n**Sohbet Türü :** __{message.chat.type}__"
    log_konsol  += f"  [green]||[/] [magenta]{message.chat.type}[/]"
    log_dosya   += f"\t| {message.chat.type}\n"

    log_ver(f"{log_konsol}")                             # zenginKonsol'a log gönder
    await client.send_message(int(LOG_ID), log_mesaj)    # log_id'ye log gönder

    with open(f"@{SESSION_ADI}.log", "a+") as log_yaz:   # dosyaya log yaz
        log_yaz.write(log_dosya)

async def hata_log(client:Client, hata_soyle):
    hata_mesaj   =  f"\n\n**Hata Var !** __{hata_soyle}__"
    hata_konsol  = f"\t\t[bold magenta]||[/] [bold grey74]{hata_soyle}[/]"
    hata_dosya   = f"\n\t\t\t\t\t{hata_soyle}\n\n"

    log_ver(f"{hata_konsol}")                             # zenginKonsol'a log gönder
    await client.send_message(int(LOG_ID), hata_mesaj)    # log_id'ye log gönder

    with open(f"@{SESSION_ADI}.log", "a+") as log_yaz:    # dosyaya log yaz
        log_yaz.write(hata_dosya)
