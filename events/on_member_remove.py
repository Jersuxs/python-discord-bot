import discord
    from discord.ext import commands
    from utils.embeds import Embeds

    class OnMemberRemove(commands.Cog):
      def __init__(self, bot):
        self.bot = bot

      @commands.Cog.listener()
      async def on_member_remove(self, member):
        embed = Embeds.goodbye(member)
        await member.send(embed=embed)

    def setup(bot):
      bot.add_cog(OnMemberRemove(bot))
