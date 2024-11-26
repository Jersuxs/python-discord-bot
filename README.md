# Discord Bot Avanzado

    ## Introducción

    Este es un bot de Discord.py avanzado que incluye comandos, eventos y utilidades para crear un bot de Discord personalizado. El bot está diseñado para ser fácil de usar y personalizar, y se puede utilizar para una variedad de propósitos, desde la gestión de servidores hasta la creación de juegos y aplicaciones.

    ## Código del Bot

    El código del bot se encuentra en el archivo `main.py`. En este archivo, se importan las bibliotecas necesarias y se crea una instancia del bot.

    ```python
import os
import discord
from discord.ext import commands
from handler.slash_commands import SlashCommands
from events.on_ready import OnReady
from events.on_member_join import OnMemberJoin
from events.on_member_remove import OnMemberRemove

bot = commands.Bot(command_prefix='!', intents=discord.Intents.all())

bot.add_cog(OnReady(bot))
bot.add_cog(OnMemberJoin(bot))
bot.add_cog(OnMemberRemove(bot))
bot.add_cog(SlashCommands(bot))

bot.run(os.environ['TOKEN'])
```

    ## Comandos

    Los comandos son funciones que se pueden ejecutar en el chat de Discord. En este bot, hay dos comandos:

    * `ping`: Responde con "Pong!".
    * `info`: Muestra información del bot.

    Para crear un comando, debes crear un archivo en la carpeta `commands` con el nombre del comando. Por ejemplo, para crear un comando llamado `hola`, debes crear un archivo llamado `hola.py` en la carpeta `commands`.

    En el archivo del comando, debes importar el módulo `discord` y `commands` de `discord.ext`. Luego, debes crear una clase que herede de `commands.Cog` y definir el comando en el método `__init__`.

    Por ejemplo:
    ```python
import discord
from discord.ext import commands

class Hola(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.command(name='hola', description='Hola!')
  async def hola(self, ctx):
    await ctx.send('Hola!')

def setup(bot):
  bot.add_cog(Hola(bot))
```

    ### Ejemplo de Uso

    Para utilizar el comando `hola`, simplemente escribe `!hola` en el chat de Discord.

    ## Eventos

    Los eventos son funciones que se ejecutan cuando ocurre un evento en el servidor de Discord. En este bot, hay tres eventos:

    * `on_ready`: Se ejecuta cuando el bot inicia sesión.
    * `on_member_join`: Se ejecuta cuando un miembro se une al servidor.
    * `on_member_remove`: Se ejecuta cuando un miembro se va del servidor.

    Para crear un evento, debes crear un archivo en la carpeta `events` con el nombre del evento. Por ejemplo, para crear un evento llamado `on_message`, debes crear un archivo llamado `on_message.py` en la carpeta `events`.

    En el archivo del evento, debes importar el módulo `discord` y `commands` de `discord.ext`. Luego, debes crear una clase que herede de `commands.Cog` y definir el evento en el método `__init__`.

    Por ejemplo:
    ```python
import discord
from discord.ext import commands

class OnMessage(commands.Cog):
  def __init__(self, bot):
    self.bot = bot

  @commands.Cog.listener()
  async def on_message(self, message):
    if message.author == self.bot.user:
      return

    await message.channel.send('Hola!')

def setup(bot):
  bot.add_cog(OnMessage(bot))
```

    ### Ejemplo de Uso

    Para utilizar el evento `on_message`, simplemente escribe un mensaje en el chat de Discord.

    ## Utilidades

    Las utilidades son funciones que se pueden utilizar en cualquier parte del bot. En este bot, hay una utilidad llamada `Embeds` que se utiliza para crear embeds.

    Para crear una utilidad, debes crear un archivo en la carpeta `utils` con el nombre de la utilidad. Por ejemplo, para crear una utilidad llamada `MiUtilidad`, debes crear un archivo llamado `mi_utilidad.py` en la carpeta `utils`.

    En el archivo de la utilidad, debes importar el módulo `discord` y definir la utilidad.

    Por ejemplo:
    ```python
import discord

class MiUtilidad:
  def __init__(self):
    pass

  def mi_metodo(self):
    return 'Hola!'
```

    ### Ejemplo de Uso

    Para utilizar la utilidad `MiUtilidad`, simplemente importa la clase y llama al método `mi_metodo`.

    ## Configuración

    La configuración del bot se encuentra en el archivo `config.json`. En este archivo, debes definir el token del bot y cualquier otra configuración que desees.

    Por ejemplo:
    ```json
{
  "TOKEN": "tu-token-de-discord"
}
```

    ## Ejecución

    Para ejecutar el bot, debes ejecutar el archivo `main.py` con el comando `python main.py`.

    ## Dependencias

    El bot requiere la dependencia `discord.py` para funcionar. Puedes instalarla con el comando `pip install discord.py`.

    ## Licencia

    El bot se encuentra bajo la licencia MIT. Puedes utilizar y modificar el código como desees.

    ## Contribuciones

    Si deseas contribuir al bot, puedes hacerlo enviando un pull request al repositorio de GitHub.

    ## Contacto

    Si tienes alguna pregunta o necesitas ayuda, puedes contactarme en Discord o por correo electrónico.
