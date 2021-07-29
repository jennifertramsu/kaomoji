import os
import random

#creating discord connection
import discord
from dotenv import load_dotenv

from discord.ext import commands

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

#client

'''
client = discord.Client()

@client.event
async def on_ready():
    print(f'{client.user.name} has connected to Discord!')

client.run(TOKEN)

'''

#bot

bot = commands.Bot(command_prefix = '~')

@bot.event

async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

#kaomoji repository

kaomoji_joy = [
        '(* ^ ω ^)', '(´ ∀ ` *)', '٩(◕‿◕｡)۶', '☆*:.｡.o(≧▽≦)o.｡.:*☆',
        '(o^▽^o)',	'(⌒▽⌒)☆', '<(￣︶￣)>', '。.:☆*:･\'(*⌒―⌒*)))',
        'ヽ(・∀・)ﾉ', '(´｡• ω •｡`)', '(￣ω￣)', ';:゛;｀;･(°ε° )',
        '(o･ω･o)', '(＠＾◡＾)', 'ヽ(*・ω・)ﾉ', '(o_ _)ﾉ彡☆',
        '(^人^)', '(o´▽`o)', '(*´▽`*)', '｡ﾟ( ﾟ^∀^ﾟ)ﾟ｡', 
        '( ´ ω ` )', '(((o(*°▽°*)o)))', '(≧◡≦)', '(o´∀`o)',
        '(´• ω •`)', '(＾▽＾)', '(⌒ω⌒)', '∑d(°∀°d)',
        '╰(▔∀▔)╯', '(─‿‿─)', '(*^‿^*)', 'ヽ(o^ ^o)ﾉ',
        '(✯◡✯)', '(◕‿◕)', '(*≧ω≦*)', '(☆▽☆)', '(⌒‿⌒)', 
        '＼(≧▽≦)／', 'ヽ(o＾▽＾o)ノ', '☆ ～(\'▽^人)',
        '(*°▽°*)', '٩(｡•́‿•̀｡)۶', '(✧ω✧)', 'ヽ(*⌒▽⌒*)ﾉ',
        '(´｡• ᵕ •｡`)', '( ´ ▽ ` )', '(￣▽￣)', '╰(*´︶`*)╯',
        'ヽ(>∀<☆)ノ', 'o(≧▽≦)o', '(☆ω☆)', '(っ˘ω˘ς )', 
        '＼(￣▽￣)／', '(*¯︶¯*)', '＼(＾▽＾)／', '٩(◕‿◕)۶', 
        '(o˘◡˘o)', '\(★ω★)/', '\(^ヮ^)/', '(〃＾▽＾〃)', 
        '(╯✧▽✧)╯', 'o(>ω<)o', 'o( ❛ᴗ❛ )o', '｡ﾟ(TヮT)ﾟ｡', 
        '( ‾́ ◡ ‾́ )', '(ﾉ´ヮ`)ﾉ*:･ﾟ', '(b ᵔ▽ᵔ)b', '(๑˃ᴗ˂)ﻭ',
        '(๑˘︶˘๑)',	'( ˙꒳​˙ )', '(*꒦ິ꒳꒦ີ)', '°˖✧◝(⁰▿⁰)◜✧˖°', 
        '(´･ᴗ･ ` )', '(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧', '(„• ֊ •„)', '(.❛ ᴗ ❛.)', 
        '(⁀ᗢ⁀)', '(￢‿￢ )', '(¬‿¬ )', '(*￣▽￣)b', 
        '( ˙▿˙ )', '(¯▿¯)'
    ]

kaomoji_love = [
    '(ﾉ´ з `)ノ', '(♡μ_μ)', '(*^^*)♡', '☆⌒ヽ(*\'､^*)chu',
    '(♡-_-♡)', '(￣ε￣＠)', 'ヽ(♡‿♡)ノ', '( ´ ∀ `)ノ～ ♡', 
    '(─‿‿─)♡', '(´｡• ᵕ •｡`) ♡', '(*♡∀♡)', '(｡・//ε//・｡)', 
    '(´ ω `♡)', '♡( ◡‿◡ )', '(◕‿◕)♡', '(/▽＼*)｡o○♡', 
    '(ღ˘⌣˘ღ)', '(♡°▽°♡)', '♡(｡- ω -)', '♡ ～(\'▽^人)',
    '(´• ω •`) ♡', '(´ ε ` )♡', '(´｡• ω •｡`)', '♡	( ´ ▽ ` ).｡ｏ♡',
    '╰(*´︶`*)╯♡', '(*˘︶˘*).｡.:*♡', '(♡˙︶˙♡)', '♡＼(￣▽￣)／♡', 
    '(≧◡≦) ♡', '(⌒▽⌒)♡', '(*¯ ³¯*)♡', '(っ˘з(˘⌣˘ ) ♡',
    '♡ (˘▽˘>ԅ( ˘⌣˘)', '( ˘⌣˘)♡(˘⌣˘ )', '(/^-^(^ ^*)/ ♡', '٩(♡ε♡)۶',    
    'σ(≧ε≦σ) ♡', '♡ (⇀ 3 ↼)', '♡ (￣З￣)', '(❤ω❤)', 
    '(˘∀˘)/(μ‿μ) ❤', '❤ (ɔˆз(ˆ⌣ˆc)', '(´♡‿♡`)', '(°◡°♡)', 
    'Σ>―(〃°ω°〃)♡→', '(´,,•ω•,,)♡'
]

kaomoji_embarrassment = [
    '(⌒_⌒;)', '(o^ ^o)', '(*/ω＼)', '(*/。＼)',
    '(*/_＼)', '(*ﾉωﾉ)', '(o-_-o)', '(*μ_μ)', 
    '( ◡‿◡ *)', '(ᵔ.ᵔ)', '(*ﾉ∀`*)', '(//▽//)',
    '(//ω//)', '(ノ*°▽°*)', '(*^.^*)', '(*ﾉ▽ﾉ)',
    '(￣▽￣*)ゞ', '(⁄ ⁄•⁄ω⁄•⁄ ⁄)', '(*/▽＼*)', '(⁄ ⁄>⁄ ▽ ⁄<⁄ ⁄)', 
    '(„ಡωಡ„)', '(ง ื▿ ื)ว', '( 〃▽〃)'
]

kaomoji_sympathy = [
    '(ノ_<。)ヾ(´ ▽ ` )', '｡･ﾟ･(ﾉД`)ヽ(￣ω￣ )', 'ρ(- ω -、)ヾ(￣ω￣; )',
    'ヽ(￣ω￣(。。 )ゝ', '(*´ I `)ﾉﾟ(ﾉД｀ﾟ)ﾟ｡', 'ヽ(~_~(・_・ )ゝ',
    '(ﾉ_；)ヾ(´ ∀ ` )', '(; ω ; )ヾ(´∀`* )', '(*´ー)ﾉ(ノд`)',
    '(´-ω-`( _ _ )', '(っ´ω`)ﾉ(╥ω╥)', '(ｏ・_・)ノ”(ノ_<、)'
]

kaomoji_dissatisfaction = [
    '(＃＞＜)', '(；⌣̀_⌣́)', '☆ｏ(＞＜；)○', '(￣ ￣|||)',
    '(；￣Д￣)', '(￣□￣」)', '(＃￣0￣)', '(＃￣ω￣)',
    '(￢_￢;)', '(＞ｍ＜)', '(」°ロ°)」', '(〃＞＿＜;〃)',
    '(＾＾＃)', '(︶︹︺)', '(￣ヘ￣)', '<(￣ ﹌ ￣)>',
    '(￣︿￣)', '(＞﹏＜)', '(--_--)', '凸(￣ヘ￣)',
    'ヾ( ￣O￣)ツ', '(⇀‸↼‶)', 'o(>< )o', '(」＞＜)」',
    '(ᗒᗣᗕ)՞', '눈_눈)'
]

kaomoji_anger  = [
    '(＃`Д´)', '(`皿´＃)', '( ` ω ´ )', 'ヽ( `д´*)ノ',
    '(・`ω´・)', '(`ー´)', 'ヽ(`⌒´メ)ノ', '凸(`△´＃)',
    '( `ε´ )', 'ψ( ` ∇ ´ )ψ', 'ヾ(`ヘ´)ﾉﾞ', 'ヽ(‵﹏´)ノ',
    '(ﾒ` ﾛ ´)', '(╬`益´)', '┌∩┐(◣_◢)┌∩┐', '凸( ` ﾛ ´ )凸', 
    'Σ(▼□▼メ)', '(°ㅂ°╬)', 'ψ(▼へ▼メ)～→', '(ノ°益°)ノ',
    '(҂ `з´ )', '(‡▼益▼)', '(҂` ﾛ ´)凸', '((╬◣﹏◢))',
    '٩(╬ʘ益ʘ╬)۶', '(╬ Ò﹏Ó)', '＼＼٩(๑`^´๑)۶／／', '(凸ಠ益ಠ)凸',
    '↑_(ΦwΦ)Ψ', '←~(Ψ▼ｰ▼)∈', '୧((#Φ益Φ#))୨', '٩(ఠ益ఠ)۶',
    '(ﾉಥ益ಥ)ﾉ'
]

kaomoji_sad = [
    '(ノ_<。)', '(-_-)', '(´-ω-`)', '.･ﾟﾟ･(／ω＼)･ﾟﾟ･.',
    '(μ_μ)', '(ﾉД`)', '(-ω-、)', '。゜゜(´Ｏ`) ゜゜。', 
    'o(TヘTo)', '( ; ω ; )', '(｡╯︵╰｡)', '｡･ﾟﾟ*(>д<)*ﾟﾟ･｡',
    '( ﾟ，_ゝ｀)', '(个_个)', '	(╯︵╰,)', '｡･ﾟ(ﾟ><ﾟ)ﾟ･｡',
    '( ╥ω╥ )', '(╯_╰)', '(╥_╥)', '.｡･ﾟﾟ･(＞_＜)･ﾟﾟ･｡.',
    '(／ˍ・、)', '(ノ_<、)', '(╥﹏╥)', '｡ﾟ(｡ﾉωヽ｡)ﾟ｡',
    '(つω`｡)', '(｡T ω T｡)', '(ﾉω･､)', '･ﾟ･(｡>ω<｡)･ﾟ･',
    '(T_T)', '(>_<)', '(っ˘̩╭╮˘̩)っ', '｡ﾟ･ (>﹏<) ･ﾟ｡',
    'o(〒﹏〒)o', '(｡•́︿•̀｡)', '(ಥ﹏ಥ)'
]

kaomoji_pain = [
    '~(>_<~)', '☆⌒(> _ <)', '☆⌒(>。<)', '(☆_@)'
    '(×_×)', '(x_x)', '(×_×)⌒☆', '(x_x)⌒☆',
    '(×﹏×)', '☆(＃××)', '(＋_＋)', '[ ± _ ± ]',
    '٩(× ×)۶', '_:(´ཀ`」 ∠):_'
]

kaomoji_fear = [
    '(ノωヽ)', '(／。＼)', '(ﾉ_ヽ)', '..・ヾ(。＞＜)シ',
    '(″ロ゛)', '(;;;*_*)', '(・人・)', '＼(〇_ｏ)／',
    '(/ω＼)', '(/_＼)', '〜(＞＜)〜', 'Σ(°△°|||)',
    '(((＞＜)))', '{{ (>_<) }}', '＼(º □ º l|l)/', '〣( ºΔº )〣',
    '▓▒░(°◡°)░▒▓'
]

kaomoji_indifference = [
    'ヽ(ー_ー )ノ', 'ヽ(´ー` )┌', '┐(‘～` )┌', 'ヽ(　￣д￣)ノ',
    '┐(￣ヘ￣)┌', 'ヽ(￣～￣　)ノ', '╮(￣_￣)╭', 'ヽ(ˇヘˇ)ノ',
    '┐(￣～￣)┌', '┐(︶▽︶)┌', '╮(￣～￣)╭', '¯\_(ツ)_/¯',
    '┐( ´ д ` )┌', '╮(︶︿︶)╭', '┐(￣∀￣)┌', '┐( ˘ ､ ˘ )┌',
    '╮(︶▽︶)╭', '╮( ˘ ､ ˘ )╭', '┐( ˘_˘ )┌', '╮( ˘_˘ )╭',
    '┐(￣ヮ￣)┌', 'ᕕ( ᐛ )ᕗ'
]

kaomoji_confusion =[
    '(￣ω￣;)', 'σ(￣、￣〃)', '(￣～￣;)', '(-_-;)・・・',
    '┐(\'～`;)┌', '(・_・ヾ', '(〃￣ω￣〃ゞ', '┐(￣ヘ￣;)┌',
    '(・_・;)', '(￣_￣)・・・', '╮(￣ω￣;)╭', '(¯ . ¯;)',
    '(＠_＠)', '(・・;)ゞ', 'Σ(￣。￣ﾉ)', '(・・ ) ?',
    '(•ิ_•ิ)?', '(◎ ◎)ゞ', '(ーー;)', 'ლ(ಠ_ಠ ლ)',
    'ლ(¯ロ¯"ლ)', '(¯ . ¯٥)', '(¯ ¯٥)'
]

kaomoji_doubt = [  
    '(￢_￢)', '(→_→)', '(￢ ￢)', '(￢‿￢ )',
    '(¬_¬ )', '(←_←)', '(¬ ¬ )', '(¬‿¬ )',
    '(↼_↼)', '(⇀_⇀)'
]

kaomoji_surprise = [
    'w(°ｏ°)w', 'ヽ(°〇°)ﾉ', 'Σ(O_O)', 'Σ(°ロ°)',
    '(⊙_⊙)', '(o_O)', '(O_O;)', '(O.O)',
    '(°ロ°) !', '(o_O) !', '(□_□)', 'Σ(□_□)',
    '∑(O_O;)', '( : ౦ ‸ ౦ : )'
]

kaomoji_hugging = [
    '(づ￣ ³￣)づ', '(つ≧▽≦)つ', '(つ✧ω✧)つ', '(づ ◕‿◕ )づ',
    '(⊃｡•́‿•̀｡)⊃', '(つ . •́ _ʖ •̀ .)つ', '(っಠ‿ಠ)っ', '(づ◡﹏◡)づ',
    '⊂(´• ω •`⊂)', '⊂(･ω･*⊂)', '⊂(￣▽￣)⊃', '⊂( ´ ▽ ` )⊃',
    '( ~*-*)~'
]

kaomoji_winking = [
    '(^_~)', '( ﾟｏ⌒)', '(^_-)≡☆', '(^ω~)',
    '(>ω^)', '(~人^)', '(^_-)', '( -_・)',
    '(^_<)〜☆', '(^人<)〜☆', '☆⌒(≧▽​° )', '☆⌒(ゝ。∂)',
    '(^_<)', '(^_−)☆', '(･ω<)☆', '(^.~)☆',
    '(^.~)'
]

kaomoji_sorry = [
    'm(_ _)m', '(シ_ _)シ', 'm(. .)m', '<(_ _)>',
    '人(_ _*)', '(*_ _)人', 'm(_ _;m)', '(m;_ _)m',
    '(シ. .)シ'
]

kaomoji_sleeping = [
    '[(－－)]..zzZ', '(－_－) zzZ', '(∪｡∪)｡｡｡zzZ', '(－ω－) zzZ',
    '(￣o￣) zzZZzzZZ', '(( _ _ ))..zzzZZ', '(￣ρ￣)..zzZZ', '(－.－)...zzz',
    '(＿ ＿*) Z z z', '(x . x) ~~zzZ'
]

kaomoji_special = [
    '( ͡° ͜ʖ ͡°)', '( ͡° ʖ̯ ͡°)', '( ͠° ͟ʖ ͡°)', '( ͡ᵔ ͜ʖ ͡ᵔ)',
    '( . •́ _ʖ •̀ .)', '( ఠ ͟ʖ ఠ)', '( ͡ಠ ʖ̯ ͡ಠ)', '( ಠ ʖ̯ ಠ)',
    '( ಠ ͜ʖ ಠ)', '( ಥ ʖ̯ ಥ)', '( ͡• ͜ʖ ͡• )', '( ･ิ ͜ʖ ･ิ)'
    '( ͡ ͜ʖ ͡ )', '(≖ ͜ʖ≖)', '(ʘ ʖ̯ ʘ)', '(ʘ ͟ʖ ʘ)',
    '(ʘ ͜ʖ ʘ)', '(;´༎ຶٹ༎ຶ`)'
]

kaomoji_friends = [
    'ヾ(・ω・)メ(・ω・)ノ', 'ヽ(∀° )人( °∀)ノ', 'ヽ( ⌒o⌒)人(⌒-⌒ )ﾉ', 
    '(*^ω^)八(⌒▽⌒)八(-‿‿- )ヽ', '＼(＾∀＾)メ(＾∀＾)ノ', 'ヾ(￣ー￣(≧ω≦*)ゝ',
    'ヽ( ⌒ω⌒)人(=^‥^= )ﾉ', 'ヽ(≧◡≦)八(o^ ^o)ノ', '(*・∀・)爻(・∀・*)',
    '｡*:☆(・ω・人・ω・)｡:゜☆｡', 'o(^^o)(o^^o)(o^^o)(o^^)o', '(((￣(￣(￣▽￣)￣)￣)))',
    '(°(°ω(°ω°(☆ω☆)°ω°)ω°)°)', 'ヾ(・ω・`)ノヾ(´・ω・)ノ', 'Ψ( `∀)(∀´ )Ψ',
    '(っ˘▽˘)(˘▽˘)˘▽˘ς)', '(((*°▽°*)八(*°▽°*)))', '☆ヾ(*´・∀・)ﾉヾ(・∀・`*)ﾉ☆',
    '(*＾ω＾)人(＾ω＾*)', '٩(๑･ิᴗ･ิ)۶٩(･ิᴗ･ิ๑)۶', '(☞°ヮ°)☞ ☜(°ヮ°☜)',
    '＼(▽￣ \ (￣▽￣) / ￣▽)／', '\( ˙▿˙ )/\( ˙▿˙ )/'
]

kaomoji_enemies = [
    'ヽ( ･∀･)ﾉ_θ彡☆Σ(ノ `Д´)ノ', '(*´∇`)┌θ☆(ﾉ>_<)ﾉ', '( ￣ω￣)ノﾞ⌒☆ﾐ(o _ _)o',
    '(*`0´)θ☆(メ°皿°)ﾉ', '(o¬‿¬o )...☆ﾐ(*x_x)', '(╬￣皿￣)=○＃(￣#)３￣)',
    '(; -_-)――――――C<―_-)', '＜( ￣︿￣)︵θ︵θ︵☆(＞口＜－)', '(￣ε(#￣)☆╰╮o(￣▽￣///)',
    'ヽ(>_<ヽ) ―⊂|=0ヘ(^‿^ )', 'ヘ(>_<ヘ) ￢o(￣‿￣ﾒ)', ',,((( ￣□)_／ ＼_(○￣ ))),,',
    '(҂` ﾛ ´)︻デ═一 ＼(º □ º l|l)/', '(╯°Д°)╯︵ /(.□ . ＼)', '(¬_¬'')ԅ(￣ε￣ԅ)',
    '/( .□.)＼ ︵╰(°益°)╯︵ /(.□. /)', '(ﾉ-.-)ﾉ….((((((((((((●~* ( >_<)', '!!(ﾒ￣ ￣)_θ☆°0°)/',
    '(`⌒*)O-(`⌒´Q)', '(((ง’ω’)و三 ง’ω’)ڡ≡　☆⌒ﾐ((x_x)', '(งಠ_ಠ)ง　σ( •̀ ω •́ σ)',
    '(っ•﹏•)っ ✴==≡눈٩(`皿´҂)ง', '(｢• ω •)｢ (⌒ω⌒`)', '( °ᴗ°)~ð (/❛o❛\)'
]

kaomoji_list = [kaomoji_joy, kaomoji_embarrassment, kaomoji_love, kaomoji_sympathy, 
                kaomoji_dissatisfaction, kaomoji_anger, kaomoji_sad, kaomoji_pain, 
                kaomoji_fear, kaomoji_indifference, kaomoji_confusion, kaomoji_doubt, 
                kaomoji_surprise, kaomoji_hugging, kaomoji_winking, kaomoji_sorry, 
                kaomoji_sleeping, kaomoji_special, kaomoji_friends, kaomoji_enemies]

#commands

@bot.command(name = "teehee", help = 'Responds with a random kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(random.choice(kaomoji_list))
    await ctx.send(response)
    
@bot.command(name = 'uwu', help = 'Responds with a random joy kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_joy)
    await ctx.send(response)
    
@bot.command(name = 'doki', help = 'Responds with a random love kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_love)
    await ctx.send(response)
    
@bot.command(name = 'yamete', help = 'Responds with a random embarrassment kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_embarrassment)
    await ctx.send(response)
    
@bot.command(name = 'F', help = 'Responds with a random sympathy kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_sympathy)
    await ctx.send(response)
    
@bot.command(name = 'tsk', help = 'Responds with a random dissatisfaction kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_dissatisfaction)
    await ctx.send(response)
    
@bot.command(name = 'YAH', help = 'Responds with a random anger kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_anger)
    await ctx.send(response)
    
@bot.command(name = 'ono', help = 'Responds with a random sad kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_sad)
    await ctx.send(response)
    
@bot.command(name = 'uhu', help = 'Responds with a random pain kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_pain)
    await ctx.send(response)

@bot.command(name = 'OWO!', help = 'Responds with a random fear kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_fear)
    await ctx.send(response)
    
@bot.command(name = 'ehh', help = 'Responds with a random indifference kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_indifference)
    await ctx.send(response)
    
@bot.command(name = 'owo?', help = 'Responds with a random confusion kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_confusion)
    await ctx.send(response)
    
@bot.command(name = 'ehh?', help = 'Responds with a random doubt kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_doubt)
    await ctx.send(response)
    
@bot.command(name = 'owo!', help = 'Responds with a random surprise kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_surprise)
    await ctx.send(response)
    
@bot.command(name = 'hug', help = 'Responds with a random hugging kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_hugging)
    await ctx.send(response)
    
@bot.command(name = 'wink', help = 'Responds with a random winking kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_winking)
    await ctx.send(response)
    
@bot.command(name = 'gomen', help = 'Responds with a random sorry kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_sorry)
    await ctx.send(response)
    
@bot.command(name = 'yawn', help = 'Responds with a random sleeping kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_sleeping)
    await ctx.send(response)
    
@bot.command(name = 'hehe', help = 'Responds with a random special kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_special)
    await ctx.send(response)
    
@bot.command(name = 'friend!', help = 'Responds with a random friend kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_friends)
    await ctx.send(response)

@bot.command(name = 'oy', help = 'Responds with a random enemies kaomoji')

async def kaomoji_random(ctx):
    response = random.choice(kaomoji_enemies)
    await ctx.send(response)

bot.run(TOKEN)

