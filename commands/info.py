import discord
    from discord.ext import commands

    class Info(commands.Cog):
      def __init__(self, bot):
        self.bot = bot

      @commands.command(name='info', description='Información del bot')
      async def info(self, ctx):
        embed = discord.Embed(title='Información del bot', description='Este es un bot de Discord.py avanzado')
        await ctx.send(embed=embed)

    def setup(bot):
      bot.add_cog(Info(bot))
