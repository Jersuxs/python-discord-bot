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
