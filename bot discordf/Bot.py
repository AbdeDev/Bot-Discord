from ast import Delete
from email import message
from http import client
from multiprocessing import context
from pickle import FALSE, TRUE
from turtle import title
import discord
from discord.ext import commands
import youtube_dl


bot = commands.Bot(command_prefix="smart ")
musics = {} 
ytdl = youtube_dl.YoutubeDL()

@bot.event
async def on_ready():
    print("Le bot est pret")
    channel = bot.get_channel(981790678080172062)
    await channel.send("Bienvenue sur le serveur crée par Abdramane et accène, taper smart hello ;)")


@bot.command()
async def hello (ctx):
    await ctx.send("Bienvenue sur le serveur, je suis smartBot, bot a votre service, n'hesiter pas a parler avec moi ;""taper smart guide pour avoir accès a ma liste de question")

@bot.command()
async def guide (ctx):
    await ctx.send("Hi merci d'etre là, voila liste de questions: - smart conversation - smart ressources - smart utilisation")

@bot.command()
async def conversation (ctx):
    await ctx.send("a votre ecoute, je suis programmée pour tenir une conversation de 10linges, vous pouvez poser les questions suivante: - smart bonjour - smart comment_vas_tu  - smart quel_temps_fait_il_aujourdhui  - smart suis_je_beau - smart le_prof_est_il_le_meilleur_prof_de_python_au_monde - smart jai_gagné_au_loto - smart je_peux_toucher_mon_nez_avec_ma_avec_ma_levre_inferieur - smart quel_est_la_reponse_a_tous_les_secrets_du_monde - smart ton_conseil_pour_etre_musclé - smart aurevoir")

@bot.command()
async def ressources (ctx):
    await ctx.send(" vous pouvez utiliser les ressources suivante: smart playlist - smart photo - smart aide")

@bot.command()
async def utilisation (ctx):
    await ctx.send("vous pouvez utiliser les commandes suivants: - smart ban - smart clear - smart kick  - smart unban - smart reset_conv - smart call_admin")



@bot.command()
async def bonjour (ctx):
    await ctx.send("Hi Bonjour, tu viens parler à ton vieux pote et giga intelligent smart bot ?")

@bot.command()
async def comment_vas_tu (ctx):
    await ctx.send("super mon gros, je suis en pleine forme !!!")

@bot.command()
async def quel_temps_fait_il_aujourdhui (ctx):
    await ctx.send("alors au cas ou tu ne le saurais pas je ne suis pas la meteo haha")

@bot.command()
async def suis_je_beau  (ctx):
    await ctx.send("magifique !, t'as été mannequin dans une autre vie toi non ?")

@bot.command()
async def le_prof_est_il_le_meilleur_prof_de_python_au_monde (ctx):
    await ctx.send("Bien evidement sinon qui d'autres, d'ailleurs il merite de ganger au loto")

@bot.command()
async def jai_gagné_au_loto (ctx):
    await ctx.send("ohhh tu partagera n'est ce pas ")

@bot.command()
async def je_peux_toucher_mon_nez_avec_ma_avec_ma_levre_inferieur(ctx):
    await ctx.send("j'hesite entre fascinant et inutile")

@bot.command()
async def quel_est_la_reponse_a_tous_les_secrets_du_monde(ctx):
    await ctx.send("facile haha c'est 42")

@bot.command()
async def ton_conseil_pour_etre_musclé(ctx):
    await ctx.send("je peux pas te dire ma routine c'est un secret d'etat")

@bot.command()
async def aurevoir (ctx):
    await ctx.send("haha merci d'etre venu parler avec moi, aurevoir et à la prochaine ")

@bot.command()
async def reset_conv(ctx):
    await ctx.send("la conversation a été réenittialiser, retaper - smart conversation")





@bot.command()
async def playlist(ctx):
    await ctx.send("vous pouvez utiliser les commandes suivantes pour la musique: smart play -  smart leave ")
class Video:
    def __init__(self, link):
        video = ytdl.extract_info(link, download=False)
        video_format = video["formats"][0]
        self.url = video["webpage_url"]
        self.stream_url = video_format["url"]

@bot.command()
async def leave(ctx):
    client = ctx.guild.voice_client
    await client.disconnect()
    musics[ctx.guild] = []


def play_song(client, song):
    source = discord.PCMVolumeTransformer(discord.FFmpegPCMAudio(song.stream_url))

    client.play(source)


@bot.command()
async def play(ctx, url):
    print("play")
    client = ctx.guild.voice_client
    
    channel = ctx.author.voice.channel
    video = Video(url)
    musics[ctx.guild] = []
    client = await channel.connect()
    await ctx.send(f"Je lance : {video.url}")
    play_song(client, video)

@bot.command()
async def photo(ctx):
    await ctx.send("vous pouvez avoir les photos suivante: smart chat - smart chien - smart ordinateur")
@bot.command()
async def chat(ctx):
    await ctx.send("https://www.google.com/url?sa=i&url=https%3A%2F%2Fwww.franceinter.fr%2Fculture%2Fbernard-werber-le-futur-joue-en-faveur-des-chats&psig=AOvVaw3L4P6R_yCAhuTuN15DNkJV&ust=1654239181902000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCIDVk6iXjvgCFQAAAAAdAAAAABAF")
@bot.command()
async def chien(ctx):
    await ctx.send("https://www.google.com/url?sa=i&url=https%3A%2F%2Ffr.depositphotos.com%2Fstock-photos%2Fraces-de-chien.html&psig=AOvVaw09x6B3hiVtbrUCUqCnmuFJ&ust=1654239085856000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCIj1zPqWjvgCFQAAAAAdAAAAABAF")
@bot.command()
async def ordinateur(ctx):
    await ctx.send("https://www.google.com/url?sa=i&url=https%3A%2F%2Flescahiersdudebutant.fr%2Fpc-portable%2Fmeilleur-pc-portable-comparatif%2F&psig=AOvVaw0W0oDFQRXAch_Mo3-07BAY&ust=1654239219278000&source=images&cd=vfe&ved=0CAwQjRxqFwoTCODymbuXjvgCFQAAAAAdAAAAABAD")


@bot.command()
async def aide(ctx):
    await ctx.send("vous pouvez me demander de l'aide sur 3 langages de programmation: smart python - smart js - smart php ")
@bot.command()
async def python(ctx):
    await ctx.send("https://docs.python.org/3/library/resource.html")
@bot.command()
async def js(ctx):
    await ctx.send("https://developer.mozilla.org/en-US/docs/Web/JavaScript")
@bot.command()
async def php(ctx):
    await ctx.send("https://www.php.net/manual/fr/language.types.resource.php")





@bot.command()
async def ban(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.ban(user, reason = reason)
	await ctx.send(f"{user} à été ban pour la raison suivante : {reason}.")

@bot.command()
async def unban(ctx, user, *reason):
	reason = " ".join(reason)
	userName, userId = user.split("#")
	bannedUsers = await ctx.guild.bans()
	for i in bannedUsers:
		if i.user.name == userName and i.user.discriminator == userId:
			await ctx.guild.unban(i.user, reason = reason)
			await ctx.send(f"{user} à été unban.")
			return
	await ctx.send(f"L'utilisateur {user} n'est pas dans la liste des bans")

@bot.command()
async def kick(ctx, user : discord.User, *reason):
	reason = " ".join(reason)
	await ctx.guild.kick(user, reason = reason)
	await ctx.send(f"{user} à été kick.")

@bot.command()
async def clear(ctx,nombre :int):
    messages = await ctx.channel.history(limit =nombre + 1).flatten()
    for message in messages:
        await message.delete()



bot.run("OTgxNzc3ODUzMTAyMzI1ODIw.GsGmL1.kznb67nIuyt41KWvs7N2BbNrEF0cC4bTbfpqIE")