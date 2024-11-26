import discord
    from discord.ext import commands
    from utils.embeds import Embeds

    class OnMemberJoin(commands.Cog):
      def __init__(self, bot):
        self.bot = bot

      @commands.Cog.listener()
      async def on_member_join(self, member):
        embed = Embeds.welcome(member)
        await member.send(embed=embed)

    def setup(bot):
      bot.add_cog(OnMemberJoin(bot))
