# Bu araç @keyiflerolsun tarafından | @KekikAkademi için yazılmıştır.

from pyrogram import Client, __version__
import os, sys
from dotenv import load_dotenv
from rich.console import Console

konsol = Console(log_path=False)

def hata(yazi):
   konsol.print(yazi, style="bold red")
def bilgi(yazi):
   konsol.print(yazi, style="blue")
def basarili(yazi):
   konsol.print(yazi, style="bold green")
def onemli(yazi):
   konsol.print(yazi, style="bold cyan")
def soru(soru):
   return konsol.input(f"[bold yellow]{soru}[/]")
def log_ver(bisi):
    konsol.log(bisi)

if sys.version_info[0] < 3 or sys.version_info[1] < 6:
    hata("""En az python 3.6 sürümüne sahip olmanız gerekir.
              Birden fazla özellik buna bağlıdır. Bot kapatılıyor.""")
    quit(1)

load_dotenv("ayar.env")

# Yapılandırmanın önceden kullanılan değişkeni kullanarak düzenlenip düzenlenmediğini kontrol edin.
# Temel olarak, yapılandırma dosyası için kontrol.
AYAR_KONTROL = os.environ.get("___________LUTFEN_______BU_____SATIRI_____SILIN__________", None)

if AYAR_KONTROL:
    hata("\n\tLütfen ilk hashtag'de belirtilen satırı ayar.env dosyasından kaldırın\n")
    quit(1)

API_ID          = os.environ.get("API_ID", None)
API_HASH        = os.environ.get("API_HASH", None)
BOT_TOKEN       = os.environ.get("BOT_TOKEN", None)
LOG_ID          = os.environ.get("LOG_ID", None)
YETKILI         = os.environ.get("YETKILI", None).split(',')
SESSION_ADI     = os.environ.get("SESSION_ADI", "kekikRobot")
INDIRME_ALANI   = os.environ.get("INDIRME_ALANI", "downloads/")
if not os.path.isdir(INDIRME_ALANI): os.makedirs(INDIRME_ALANI)

try:
    kekikRobot          = Client(
        api_id          = int(API_ID),
        api_hash        = API_HASH,
        session_name    = f'@{SESSION_ADI}',
        bot_token       = BOT_TOKEN,
        plugins         = dict(root="Robot/Eklentiler")
    )
except ValueError:
    hata("\n\tLütfen ayar.env dosyanızı oluşturun..\n")
    quit(1)

DESTEK_KOMUT = {}

tum_eklentiler = []
for dosya in os.listdir("./Robot/Eklentiler/"):
    if not dosya.endswith(".py") or dosya.startswith("_"):
        continue
    tum_eklentiler.append(f"📂 {dosya.replace('.py','')}")

def baslangic():
    kekikRobot.start()

    surum = f"{str(sys.version_info[0])}.{str(sys.version_info[1])}"
    konsol.print(f"\t\t[gold1]@{SESSION_ADI}[/] [yellow]:bird:[/] [bold red]Python: [/][i]{surum}[/]")
    basarili(f"  {SESSION_ADI} [magenta]v[/] [blue]{__version__}[/] [red]Pyrogram[/] tabanında [magenta]{len(tum_eklentiler)} eklentiyle[/] çalışıyor...\n")

    kekikRobot.stop()