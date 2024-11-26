import discord

    class Embeds:
      def welcome(member):
        embed = discord.Embed(title='Bienvenido!', description=f'Bienvenido {member.mention} al servidor!')
        return embed

      def goodbye(member):
        embed = discord.Embed(title='Adiós!', description=f'Adiós {member.mention} del servidor!')
        return embed
