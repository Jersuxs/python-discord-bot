import discord
    from discord.ext import commands

    class SlashCommands(commands.Cog):
      def __init__(self, bot):
        self.bot = bot

      @commands.slash_command(name='ping', description='Pong!')
      async def ping(self, ctx):
        await ctx.respond('Pong!')

      @commands.slash_command(name='info', description='Información del bot')
      async def info(self, ctx):
        embed = discord.Embed(title='Información del bot', description='Este es un bot de Discord.py avanzado')
        await ctx.respond(embed=embed)

    def setup(bot):
      bot.add_cog(SlashCommands(bot))
