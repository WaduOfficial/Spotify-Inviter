#Credits to Wadu
import discord
from discord.ext.commands import Bot
import asyncio, json, requests
from bs4 import BeautifulSoup
import os, time, re, subprocess
with open('config.json') as (f):
    data = json.load(f)
TOKEN = data['token']
BOT_PREFIX = data['prefix']
client = Bot(command_prefix= BOT_PREFIX)

def grab_accounts(US, GB, DE, CA, AU, IT, NZ, MX, key, BE, FR, ID, SG, BR, MY, PT, IL, DK, NL, ES, SE, NO, TR):
    f = open('Accounts/US.txt', 'r')
    for line in f:
        clean = line.split('\n')
        US.append(clean[0])

    f.close()
    f = open('Accounts/GB.txt', 'r')
    for line in f:
        clean = line.split('\n')
        GB.append(clean[0])

    f.close()
    f = open('Accounts/DE.txt', 'r')
    for line in f:
        clean = line.split('\n')
        DE.append(clean[0])

    f.close()
    f = open('Accounts/CA.txt', 'r')
    for line in f:
        clean = line.split('\n')
        CA.append(clean[0])

    f.close()
    f = open('Accounts/AU.txt', 'r')
    for line in f:
        clean = line.split('\n')
        AU.append(clean[0])

    f.close()
    f = open('Accounts/IT.txt', 'r')
    for line in f:
        clean = line.split('\n')
        IT.append(clean[0])

    f.close()
    f = open('Accounts/NZ.txt', 'r')
    for line in f:
        clean = line.split('\n')
        NZ.append(clean[0])

    f.close()
    f = open('Accounts/MX.txt', 'r')
    for line in f:
        clean = line.split('\n')
        MX.append(clean[0])

    f.close()
    f = open('keys.txt', 'r')
    for line in f:
        clean = line.split('\n')
        key.append(clean[0])

    f.close()
    f = open('Accounts/BE.txt', 'r')
    for line in f:
        clean = line.split('\n')
        BE.append(clean[0])

    f.close()
    f = open('Accounts/FR.txt', 'r')
    for line in f:
        clean = line.split('\n')
        FR.append(clean[0])

    f.close()
    f = open('Accounts/ID.txt', 'r')
    for line in f:
        clean = line.split('\n')
        ID.append(clean[0])

    f.close()
    f = open('Accounts/SG.txt', 'r')
    for line in f:
        clean = line.split('\n')
        SG.append(clean[0])

    f.close()
    f = open('Accounts/BR.txt', 'r')
    for line in f:
        clean = line.split('\n')
        BR.append(clean[0])

    f.close()
    f = open('Accounts/MY.txt', 'r')
    for line in f:
        clean = line.split('\n')
        MY.append(clean[0])

    f.close()
    f = open('Accounts/PT.txt', 'r')
    for line in f:
        clean = line.split('\n')
        PT.append(clean[0])

    f.close()
    f = open('Accounts/IL.txt', 'r')
    for line in f:
        clean = line.split('\n')
        IL.append(clean[0])

    f.close()
    f = open('Accounts/DK.txt', 'r')
    for line in f:
        clean = line.split('\n')
        DK.append(clean[0])

    f.close()
    f = open('Accounts/NL.txt', 'r')
    for line in f:
        clean = line.split('\n')
        NL.append(clean[0])

    f.close()
    f = open('Accounts/ES.txt', 'r')
    for line in f:
        clean = line.split('\n')
        ES.append(clean[0])

    f.close()
    f = open('Accounts/SE.txt', 'r')
    for line in f:
        clean = line.split('\n')
        SE.append(clean[0])

    f.close()
    f = open('Accounts/NO.txt', 'r')
    for line in f:
        clean = line.split('\n')
        NO.append(clean[0])

    f.close()
    f = open('Accounts/TR.txt', 'r')
    for line in f:
        clean = line.split('\n')
        TR.append(clean[0])

    f.close()


def keyGrab(key):
    f = open('keys.txt', 'r')
    for line in f:
        clean = line.split('\n')
        key.append(clean[0])

    f.close()


def keyRemove(key):
    os.remove('keys.txt')
    f = open('keys.txt', 'a')
    for ELEM in key:
        f.write(ELEM + '\n')

    f.close()


@client.event
async def on_ready():
	await client.change_presence(game=discord.Game(name=data['BotStatus']))
	print('bot is ready \nCredits to Wadu')


@client.command(pass_context=True)
async def redeem(ctx, arg1, arg2, arg3):
    await client.delete_message(ctx.message)
    allowed_countries = [
     'US', 'GB', 'DE', 'CA', 'AU', 'IT', 'NZ', 'MX', 'BE', 'FR', 'ID', 'SG', 'BR', 'MY', 'PT', 'IL', 'DK', 'NL', 'ES', 'SE', 'NO', 'TR']
    accounts = []
    keys = []
    country = arg1.upper()
    keyGrab(keys)
    if country in allowed_countries:
        f = open('Accounts/' + str(country) + '.txt', 'r')
        for line in f:
            clean = line.split('\n')
            accounts.append(clean[0])

        f.close()
    if country not in allowed_countries:
        return await (client.say('Sorry But the Country you Specified is Not Currently Offered'))
    if arg3 not in keys:
        return await (client.say('Sorry but you entered an invalid product key.'))
    if arg3 in keys:
        keys.remove(arg3)
        check = re.compile('(^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\\.[a-zA-Z0-9-.]+$)')
        mat = check.match(str(arg2))
        if mat:
            result = None
            while result != ',"success":true}':
                if len(accounts) == 0:
                    await client.say('Sorry We Are Out of Stock on That Country')
                    os.remove('Accounts/' + str(country) + '.txt')
                    f = open('Accounts/' + str(country) + '.txt', 'a')
                    for ELEM in accounts:
                        f.write(ELEM + '\n')

                    f.close()
                    break
                account = accounts.pop()
                combo = account.split(':')
                USER = combo[0]
                PASS = combo[1]
                try:
                    with requests.Session() as (c):
                        url = 'https://accounts.spotify.com/en/login?continue=https:%2F%2Fwww.spotify.com%2Fint%2Faccount%2Foverview%2F'
                        headers = {'Accept':'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',  'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/71.0.3578.98 Safari/537.36'}
                        page = c.get(url, headers=headers)
                        CSRF = page.cookies['csrf_token']
                        headers = {'Accept':'*/*',  'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1',  'Referer':'https://accounts.spotify.com/en/login/?continue=https:%2F%2Fwww.spotify.com%2Fus%2Fgooglehome%2Fregister%2F&_locale=en-US'}
                        url = 'https://accounts.spotify.com/api/login'
                        login_data = {'remember':'true',  'username':USER,  'password':PASS,  'csrf_token':CSRF}
                        cookies = dict(__bon='MHwwfC0xNDAxNTMwNDkzfC01ODg2NDI4MDcwNnwxfDF8MXwx')
                        login = c.post(url, headers=headers, data=login_data, cookies=cookies)
                        if '{"displayName":"' in login.text:
                            url = 'https://www.spotify.com/us/account/overview/'
                            capture = c.get(url, headers=headers)
                            csr = capture.headers['X-Csrf-Token']
                            url = 'https://www.spotify.com/us/family/api/master-invite-by-email/'
                            headers = {'Accept':'*/*',  'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 10_0_1 like Mac OS X) AppleWebKit/602.1.50 (KHTML, like Gecko) Version/10.0 Mobile/14A403 Safari/602.1',  'x-csrf-token':csr}
                            login_data = {'firstName':'thomas',  'lastName':'Payne',  'email':arg2}
                            invite = c.post(url, headers=headers, json=login_data)
                            print(invite.text)
                            if '"success":true}' in invite.text:
                                await client.say(arg2 + ' has been successfully invited to a ' + country + ' Family Plan')
                                accounts.append(combo[0] + ':' + combo[1])
                                print(combo[0] + ':' + combo[1])
                                keyRemove(keys)
                                result = ',"success":true}'
                                channel = discord.utils.get(ctx.message.server.channels, name='logs')
                                await client.send_message(channel, arg2 + ' has been invited to a ' + country + ' Plan | using the key: ' + arg3 + ' | invited by the account: ' + combo[0] + ':' + combo[1] + ' | USER Who Redeemed Key: ' + str(ctx.message.author))
                                os.remove('Accounts/' + str(country) + '.txt')
                                f = open('Accounts/' + str(country) + '.txt', 'a')
                                for ELEM in accounts:
                                    f.write(ELEM + '\n')

                                f.close()
                                break
                            if 'message":"Invite limit reached' in invite.text:
                                result = None
                            if 'message":"No family plan found for user' in invite.text:
                                result = None
                        if '{"error":"errorInvalidCredentials"}' in login.text:
                            result = None
                except:
                    pass

        if not mat:
            return await (client.say('Sorry But an Invalid Email Was Given'))


@client.command()
async def stock():
    US_stock = []
    GB_stock = []
    DE_stock = []
    CA_stock = []
    AU_stock = []
    IT_stock = []
    NZ_stock = []
    MX_stock = []
    BE_stock = []
    FR_stock = []
    ID_stock = []
    SG_stock = []
    BR_stock = []
    MY_stock = []
    PT_stock = []
    IL_stock = []
    DK_stock = []
    NL_stock = []
    ES_stock = []
    SE_stock = []
    NO_stock = []
    TR_stock = []
    key = []
    grab_accounts(US_stock, GB_stock, DE_stock, CA_stock, AU_stock, IT_stock, NZ_stock, MX_stock, key, BE_stock, FR_stock, ID_stock, SG_stock, BR_stock, MY_stock, PT_stock, IL_stock, DK_stock, NL_stock, ES_stock, SE_stock, NO_stock, TR_stock)
    embed = discord.Embed(title='Stock',
      colour=discord.Colour.blue())
    embed.set_author(name='Inviter Bot', icon_url='https://cdn.discordapp.com/avatars/513839414322135062/b759fed29c2186046bfd6b7eff0bba5f.webp?size=128')
    embed.add_field(name='US', value=len(US_stock), inline=True)
    embed.add_field(name='GB', value=len(GB_stock), inline=True)
    embed.add_field(name='DE', value=len(DE_stock), inline=True)
    embed.add_field(name='CA', value=len(CA_stock), inline=True)
    embed.add_field(name='AU', value=len(AU_stock), inline=True)
    embed.add_field(name='IT', value=len(IT_stock), inline=True)
    embed.add_field(name='NZ', value=len(NZ_stock), inline=True)
    embed.add_field(name='MX', value=len(MX_stock), inline=True)
    embed.add_field(name='BE', value=len(BE_stock), inline=True)
    embed.add_field(name='FR', value=len(FR_stock), inline=True)
    embed.add_field(name='ID', value=len(ID_stock), inline=True)
    embed.add_field(name='SG', value=len(SG_stock), inline=True)
    embed.add_field(name='BR', value=len(BR_stock), inline=True)
    embed.add_field(name='MY', value=len(MY_stock), inline=True)
    embed.add_field(name='PT', value=len(PT_stock), inline=True)
    embed.add_field(name='IL', value=len(IL_stock), inline=True)
    embed.add_field(name='DK', value=len(DK_stock), inline=True)
    embed.add_field(name='NL', value=len(NL_stock), inline=True)
    embed.add_field(name='ES', value=len(ES_stock), inline=True)
    embed.add_field(name='SE', value=len(SE_stock), inline=True)
    embed.add_field(name='NO', value=len(NO_stock), inline=True)
    embed.add_field(name='TR', value=len(TR_stock), inline=True)
    await client.say(embed=embed)



client.run(TOKEN)