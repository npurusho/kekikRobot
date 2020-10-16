# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from Robot.Edevat.zenginLog import log_yolla, hata_log
from Robot import DESTEK_KOMUT
from pathlib import Path

DESTEK_KOMUT.update({
    Path(__file__).stem : {
        "aciklama"  : "botun hayatta olup olmadığı kontrolü..",
        "kullanim"  : [
            "mesaj",
            "yanıtlanan mesaj"
            ],
        "ornekler"  : [
            ".ping"
            ]
    }
})

from pyrogram import Client, filters
from Robot.Edevat._pyrogram.pyro_yardimcilari import yanitlanan_mesaj
from Robot import YETKILI
import asyncio, datetime

@Client.on_message(filters.command(['ping'], ['!','.','/']))
async def ping(client, message):
    # < Başlangıç
    await log_yolla(client, message)
    yanitlanacak_mesaj = yanitlanan_mesaj(message)
    ilk_mesaj = await message.reply("__Bekleyin..__",
        disable_web_page_preview    = True,
        parse_mode                  = "Markdown",
        reply_to_message_id         = yanitlanacak_mesaj
    )
    #------------------------------------------------------------- Başlangıç >

    basla = datetime.datetime.now()

    mesaj = "__Pong!__"

    bitir = datetime.datetime.now()
    sure = (bitir - basla).microseconds
    mesaj += f"\n\n**Tepki Süresi :** `{sure} ms`"

    await ilk_mesaj.edit(mesaj)

    await asyncio.sleep(3)
    await ilk_mesaj.edit("__şimdi mutlu musun?__")
    await asyncio.sleep(1)

    try:
        await ilk_mesaj.edit(mesaj)
    except Exception as hata:
        await hata_log(client, hata)
        await ilk_mesaj.edit(f'**Hata Var !**\n\n`{type(hata).__name__}`\n\n__{hata}__')

@Client.on_message(filters.command(['json'], ['!','.','/']))
async def jsn_ver(client, message):
    await log_yolla(client, message)
    yanitlanacak_mesaj = yanitlanan_mesaj(message)

    if str(message.from_user.id) not in YETKILI:
        await message.reply("__admin değilmişsin kekkooo__", reply_to_message_id=yanitlanacak_mesaj)
        return

    await message.reply(f"```{message.reply_to_message}```")