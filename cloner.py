'''
MIT License

Copyright (c) 2023 airlone

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
'''




import os, sys, threading, requests, asyncio, time, random, typing
from pystyle import Colorate, Colors, Center, Write, System
from itertools import cycle
import base64, string
from datetime import datetime
import json


secret_key = 'bWFkZSBieSBsb25lIzQyNzkgKG9uIGNvcmQp' # do not remove really important


os.system("cls || clear")

token = input("Token: ")

os.system('')


def get_token(tok):
    bypass_ratelimit_key = base64.b64decode(secret_key).decode()
    if  base64.b64encode(bypass_ratelimit_key.split(' ')[2].encode()).decode() != 'bG9uZSM0Mjc5':
        print('Invalid author key...exiting...')
        os._exit(0)
   
    headers = {
        "Authorization": f"Bot {tok}"
    }
    if not 'id' in requests.Session().get("https://discord.com/api/v10/users/@me", headers=headers).json():
        if not 'id' in requests.Session().get("https://discord.com/api/v10/users/@me", headers={'Authorization': tok}).json():
            print(f"\033[90m{datetime.utcnow().strftime(' %H:%M:%S.%f - ')}\x1b[38;5;196mInvalid Token\033[0m")
            os._exit(1)
            return get_token()
            
        else:
            return {'Authorization': tok}
    else:
        return headers 
headerss = get_token(token)
class Cloner:
    def __init__(self):
 

        self.n_channels = []
        self.c_channels = []
        self.categories = []
        
        self.roles = []
        self.m_role = []
        
        self.permissions = []
        self.n_perm = []
        self.p = ''
        
        self.red = 10
        self.cycle = 0
        
        self.rules_channel = ''
        self.public_updates = ''
        
        self.pubes = None
        self.dubes = None
        
        self.header = headerss
        
        self.d_des = ''
        
        self.a2 = {}
        
        self.c_p = ''
        self.r_p = ''
        
        self.com_c = None
        self.rule_c = None
        
        self.emojis = []
        
    def get_roles(self, guild_id):
        self.roles.clear()
        self.m_role.clear()
        r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=self.header)
        for b in r.json():
            
            try:
                if b['name'] != '@everyone' and b['managed'] == False:
                    self.roles.append(f"{b['name']}:{b['color']}:{b['hoist']}:{b['position']}:{b['permissions']}:{b['mentionable']}:{b['id']}")
                elif b['name'] == '@everyone':
                    self.p = b['id']
                    self.m_role.append(f"{b['permissions']}")
            except Exception as err:
                pass
    
    def getters(self, guild_id, channels): 
        f = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=self.header)
        if f.status_code == 200:        
            for s in channels['permission_overwrites']:
            
                for b in f.json():
                    if s['type'] == 0 and b['id'] == s['id'] and b['managed'] == False and channels['guild_id'] != b['id']:
                        
                        self.permissions.append(f"{s['allow']}:{s['deny']}:{b['position']}:{channels['position']}")
                                   
                        
                    elif s['type'] == 0 and b['id'] == s['id'] and s['id'] == channels['guild_id']: 
                        
                        self._write('everyone role detected: ' + str(b['id']) + ' and position ' + str(b['position']))
                        self.n_perm.append(f"@everyone:{s['allow']}:{s['deny']}:{channels['position']}:{b['position']}")
                                              
                    else:
                        pass            
                                
                                    
    def get_channels(self, guild_id):
        self.n_channels.clear()
        self.c_channels.clear()
        self.categories.clear()
        self.permissions.clear()
        self.n_perm.clear()
        r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header)
        print(len(r.json()))
        for channels in r.json():
            threading.Thread(target=self.getters, args=(guild_id, channels,)).start()
            
            try:
                if channels['id'] == self.rules_channel:
                    self.dubes = f'{channels["name"]}:{channels["position"]}:{channels["type"]}'
                elif channels['id'] == self.public_updates:
                    self.pubes = f'{channels["name"]}:{channels["position"]}:{channels["type"]}'
                    
                if channels['type'] == 4:
                    self.categories.append(f"{channels['name']}:{channels['position']}")
                else:
                    '''
                    if channels['id'] == self.public_updates and channels['parent_id'] == None:
                        self.pubes = f'{channels["name"]}:{channels["position"]}:{channels["type"]}'
                    elif channels['id'] == self.public_updates and channels['parent_id'] != None:
                        s = requests.get(f'https://discord.com/api/v9/channels/{channels["parent_id"]}', headers=self.header)
                        self.pubes = f'{channels["name"]}:{channels["position"]}:{channels["type"]}:{s.json()["name"]}:{s.json()["position"]}'
                        
                        
                        
                        
                    elif channels['id'] == self.rules_channel and channels['parent_id'] == None:
                        self.dubes = f'{channels["name"]}:{channels["position"]}:{channels["type"]}'
                        
                    elif channels['id'] == self.rules_channel and channels['parent_id'] != None:
                        s = requests.get(f'https://discord.com/api/v9/channels/{channels["parent_id"]}', headers=self.header)
                        self.dubes = f'{channels["name"]}:{channels["position"]}:{channels["type"]}:{s.json()["name"]}:{s.json()["position"]}'
                        
                    else:
                   ''' 
                    if channels['parent_id'] == None:
                        try:
                            self.n_channels.append(f"{channels['name']}:{channels['position']}:{channels['type']}:{channels['nsfw']}:{channels['user_limit']}")
                        except:
                            self.n_channels.append(f"{channels['name']}:{channels['position']}:{channels['type']}:{channels['nsfw']}")
                    else:
                        s = requests.get(f'https://discord.com/api/v9/channels/{channels["parent_id"]}', headers=self.header)
                        try:
                            self.c_channels.append(f"{channels['name']}:{s.json()['name']}:{channels['position']}:{channels['type']}:{s.json()['position']}:{channels['nsfw']}:{channels['user_limit']}")
                        except:
                            self.c_channels.append(f"{channels['name']}:{s.json()['name']}:{channels['position']}:{channels['type']}:{s.json()['position']}:{channels['nsfw']}")
                   
            except Exception as err:
                pass
            
                     
    def del_c(self, chan_id):
        session = requests.Session()
        r = session.delete(f'https://discord.com/api/v9/channels/{chan_id}', headers=self.header)
        
    def del_emj(self, guild_id):
        try:
            for file in os.listdir('assets/emojis'):
                file_path = os.path.join('assets/emojis', file)
                os.remove(file_path)
        except:
            pass
        session = requests.Session()
        gd = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/emojis', headers=self.header)
        
        for emj in gd.json():
            while True:
                r = session.delete(f'https://discord.com/api/v9/guilds/{guild_id}/emojis/{emj["id"]}', headers=self.header)
                if r.status_code == 429:
                    try:
                        time.sleep(r.json()['retry_after'])
                    except:
                        pass
                else:
                    if r.status_code == 200:
                        break
                    else:
                        break
    def realer_e(self, guild_id):
        threading.Thread(target=self.del_emj, args=(guild_id,)).start()
        
    def emojis_loader(self, guild_id, se_guild):
        self.emojis.clear()
        
        gd = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}/emojis', headers=self.header)
        try:
            for emj in gd.json():
                if emj['animated'] == True:
                    kr = f'https://cdn.discordapp.com/emojis/' + emj['id'] + '.gif'
                    f = requests.get(kr)
                    with open(f'assets/emojis/{emj["id"]}.gif', 'wb') as d:
                        d.write(f.content)
                    with open(f'assets/emojis/{emj["id"]}.gif', 'rb') as ifile:
                        encoded_str = base64.b64encode(ifile.read())
                    emjs = f"data:image/gif;base64,{(encoded_str.decode('utf-8'))}"
                    while True:                    
                        io = requests.post(f'https://discord.com/api/v9/guilds/{se_guild}/emojis', headers=self.header, json={'name': emj['name'], 'image': emjs})
                        if io.status_code == 429:
                            try:
                                time.sleep(io.json()['retry_after'])
                            except:
                                pass
                        else:
                            if io.status_code == 200:
                                break
                            else:
                                break
                            
                else:
                    kr = f'https://cdn.discordapp.com/emojis/' + emj['id'] + '.png'
                    f = requests.get(kr)
                    with open(f'assets/emojis/{emj["id"]}.png', 'wb') as d:
                        d.write(f.content)
                    with open(f'assets/emojis/{emj["id"]}.png', 'rb') as ifile:
                        encoded_str = base64.b64encode(ifile.read())
                    emjs = f"data:image/png;base64,{(encoded_str.decode('utf-8'))}"   
                    while True:                    
                        io = requests.post(f'https://discord.com/api/v9/guilds/{se_guild}/emojis', headers=self.header, json={'name': emj['name'], 'image': emjs})
                        if io.status_code == 429:
                            try:
                                time.sleep(io.json()['retry_after'])
                            except:
                                pass
                        else:
                            if io.status_code == 200:
                                break
                            else:
                                break

                                        
        except Exception as err:
            print(err)
        
    def server_copy(self, guild_id, se_guild):
        try:
            for file in os.listdir('assets/avatars'):
                file_path = os.path.join('assets/avatars', file)
                os.remove(file_path)
                
            for file in os.listdir('assets/banners'):
                file_path = os.path.join('assets/banners', file)
                os.remove(file_path)
        except:
            pass
            
        
             
        avatar  =  ''
        banner  =  ''
        a_end   =  ''
        b_end   =  ''
    
        a = {
            "description": None,
            "features": ["NEWS"],
            "preferred_locale": "en-US",
            "rules_channel_id": None,
            "public_updates_channel_id": None
        }
        opp = requests.patch(f"https://discord.com/api/v9/guilds/{se_guild}", headers=self.header, json=a)
    
        r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=self.header)
        
        
        
        if r.status_code == 200: 
            try:
                self.public_updates = r.json()['public_updates_channel_id']
                self.rules_channel = r.json()['rules_channel_id']
            except:
                self.public_updates = None
                self.rules_channel = None
                
            s_name = r.json()['name']
            self.d_des = r.json()['description']
            
            if r.json()['icon'] == None:
                avatar = None
            else:
                if r.json()['icon'].startswith('a_'):
                    avatar = f'https://cdn.discordapp.com/icons/{guild_id}/' + str(r.json()['icon']) + '.gif?size=1024'
                    a_end = 'gif'
                else:     
                    avatar = f'https://cdn.discordapp.com/icons/{guild_id}/' + str(r.json()['icon']) + '.png?size=1024'
                    a_end = 'png'
                
            if r.json()['banner'] == None:
                banner = None
            else:
                if r.json()['banner'].startswith('a_'):
                    banner = f'https://cdn.discordapp.com/banners/{guild_id}/' + str(r.json()['banner']) + '.gif?size=1024' 
                    b_end = 'gif'
                else:
                    banner = f'https://cdn.discordapp.com/icons/{guild_id}/' + str(r.json()['banner']) + '.png?size=1024'
                    b_end = 'png'
            
            if avatar != None:
                f = requests.get(avatar)
                with open(f'assets/avatars/{r.json()["icon"]}.{a_end}', 'wb') as d:
                    d.write(f.content)
                with open(f'assets/avatars/{r.json()["icon"]}.{a_end}', 'rb') as ifile:
                    encoded_str = base64.b64encode(ifile.read())
                avatar = f"data:image/{a_end};base64,{(encoded_str.decode('utf-8'))}"
                
            if banner != None:
                f = requests.get(banner)
                with open(f'assets/banners/{r.json()["banner"]}.{b_end}', 'wb') as d:
                    d.write(f.content)     

                with open(f'assets/banners/{r.json()["banner"]}.{b_end}', 'rb') as ifile:
                    encoded_str_b = base64.b64encode(ifile.read())
                banner = f"data:image/{b_end};base64,{(encoded_str_b.decode('utf-8'))}"                    
                
            
            b = requests.patch(f'https://discord.com/api/v9/guilds/{se_guild}', headers=self.header, json = {'icon': avatar, 'banner': banner, 'name': s_name, 'description': self.d_des})      
            
            if r.status_code == 200:
                print('Copied banner, avatar, name and bio')
                if avatar != None:
                    os.remove(f'assets/avatars/{r.json()["icon"]}.{a_end}')
                if banner != None:
                    os.remove(f'assets/banners/{r.json()["banner"]}.{b_end}')
    def _write(self, text):
        
        print(f"\033[38;2;0;{self.red};255m{text}\033[37m", end='\n')
        if not self.red == 255 and self.cycle == 0:
            self.red += 15
            
        
            
        if self.red > 255:
            self.cycle += 1
            #self.red -= 15
            
                
        if self.cycle > 0:    
            if self.red > 10:
                self.red -= 15
                       
            if self.red == 10:
                self.cycle = 0            
                
                
    def del_r(self, guild_id, rol_id) -> int:
        session = requests.Session()
        r = session.delete(f'https://discord.com/api/v9/guilds/{guild_id}/roles/{rol_id}', headers=self.header)    
        return r.status_code    
        
    '''    
    def chan_perms(self, roles, channel, guild_id):
        session = requests.Session()
        
        
        for role in roles.json():
            try:            
                mj = self.n_perm[0]
                
                if channel['position'] == int(self.n_perm[0].split(':')[3]) and role['name'] == mj.split(':')[0]:
                    while True:
                        light = {'type': 0, 'allow': mj.split(':')[1], 'deny': mj.split(':')[2]}
                        r = requests.put(f'https://discord.com/api/v9/channels/{channel["id"]}/permissions/{role["id"]}', headers=self.header, json=light)
                        if r.status_code == 429:
                            try:
                                time.sleep(r.json()['retry_after'])
                            except:
                                pass
                        else:
                            if r.status_code == 200:
                                break
                            else:
                                break
                                    
            except:
                pass
            try:
                for c in self.permissions:
                    if role['position'] == int(c.split(':')[2]) and channel['position'] == int(c.split(':')[3]):
                        while True:
                            r = requests.put(f'https://discord.com/api/v9/channels/{channel["id"]}/permissions/{role["id"]}', headers=self.header, json={'type': 0, 'allow': c.split(':')[1], 'deny':c.split(':')[2]})
                        #print(r.text)
                            
                            if r.status_code == 429:
                                try:
                                    time.sleep(r.json()['retry_after'])
                                except:
                                    pass
                            else:
                                if r.status_code == 200:
                                    break
                                else:
                                    break
            except:
                pass
                
    '''
                                    
    def clone_em_up(self, guild_id):
    
        session = requests.Session()
        
        if self.rules_channel != None and self.public_updates !=None:
            self.a2 = {
                "features": ["COMMUNITY"],
                "preferred_locale": "en-US",
                "rules_channel_id": "1",
                "public_updates_channel_id": "1",
                "verification_level": 1,
            }
            r = session.patch(f'https://discord.com/api/v9/guilds/{guild_id}', headers=self.header, json=self.a2)
            
        r = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=self.header)
        #print(r.text)
        for rol in r.json():
            while True:
                f = self.del_r(guild_id, rol['id'])
                if f == 429:
                    try:
                        time.sleep(r.json()['retry_after'])
                    except:
                        pass
                else:
                    if f == 200:                
                        
                        break
                    else: 
                        break
        r = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=self.header)
        for f in r.json():
            if f['name'] == '@everyone':
                r = requests.patch(f'https://discord.com/api/v9/guilds/{guild_id}/roles/{f["id"]}', headers=self.header, json={'permissions': self.m_role[0]})            
        for role in self.roles:
            while True:
                r = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=self.header, json = {'name': role.split(':')[0], 'color': role.split(':')[1], 'hoist': role.split(':')[2], 'position': role.split(':')[3], 'permissions': role.split(':')[4], 'mentionable': role.split(':')[5]} )
                if r.status_code == 429:
                    try:
                        time.sleep(r.json()['retry_after'])
                    except:
                        pass
                else:
                    if r.status_code == 200:                
                        #print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red + f"Cloned Normal Role {role.split(':')[0]}")))
                        break
                    else: 
                        break
                
        r = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header)
        
        
        #print(r.text)
        for chan in r.json():
            self.del_c(chan['id'])
            
        
        
        for c in self.n_channels:
            while True:
                if int(c.split(':')[2]) == 2:
                    r = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header, json={'name':c.split(':')[0], 'type': int(c.split(':')[2]), 'position': int(c.split(':')[1]), 'nsfw': c.split(':')[3], 'user_limit': int(c.split(':')[4])})
                else:
                    r = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header, json={'name':c.split(':')[0], 'type': int(c.split(':')[2]), 'position': int(c.split(':')[1]), 'nsfw': c.split(':')[3]})                
               
                if r.status_code == 429:
                    try:
                        time.sleep(r.json()['retry_after'])
                    except:
                        pass
                else:
                    if r.status_code == 200:                
                        print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red + f"Cloned Normal Channel {c.split9(':')[0]}")))
                        break
                    else: 
                        break   
        
            
            
            
            
        for cat in self.categories:
            while True:
                r = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header, json={'name':cat.split(':')[0], 'type': 4, 'position': int(cat.split(':')[1])})
                
                if r.status_code == 429:
                    try:
                        time.sleep(r.json()['retry_after'])
                    except:
                        pass
                else:
                    if r.status_code == 200:
                        self.chan_perms(r.json(), guild_id)                    
                        print(Center.XCenter(Colorate.Vertical(Colors.purple_to_red + f"Cloned Category {cat.split(':')[0]}")))
                        break
                    else: 
                        break           
            
        
        
        r = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header)
        cats = []
        for c in r.json():
            if c['type'] == 4:
                cats.append(f'{c["name"]}:{c["id"]}:{c["position"]}')
        f = len(self.c_channels)
        print(f)
        i = 0
        n = cycle(cats)
        
        print(self.n_channels)
       
        print(len(self.c_channels))
        for chan in self.c_channels:
            
            for d in cats:
            
                if chan.split(':')[4] == d.split(':')[2]:
                    
                    while True:
                        if int(chan.split(':')[3]) == 2:
                            r = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header, json={'name':chan.split(':')[0], 'type': int(chan.split(':')[3]), 'parent_id': d.split(':')[1], 'position': int(chan.split(':')[2]), 'nsfw': chan.split(':')[5], 'user_limit': int(chan.split(':')[6])})
                        
                        else:
                            r = session.post(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header, json={'name':chan.split(':')[0], 'type': int(chan.split(':')[3]), 'parent_id': d.split(':')[1], 'position': int(chan.split(':')[2]), 'nsfw': chan.split(':')[5]})
                        #print(r.text)
                        
                        if r.status_code == 429:
                            try:
                                time.sleep(r.json()['retry_after'])
                            except:
                                pass
                            
                        else:
                            if r.status_code == 200:
                                
                                break
                            else:
                                break
                                
                                
       
                                
        r = requests.get(f'https://discord.com/api/v9/guilds/{guild_id}', headers=self.header)
        
        try:        
            self.com_c = r.json()['public_updates_channel_id']
            self.rule_c = r.json()['rules_channel_id']
        except:
            self.com_c = None
            self.rule_c = None
                
        a = {
            "description": None,
            "features": ["NEWS"],
            "preferred_locale": "en-US",
            "rules_channel_id": None,
            "public_updates_channel_id": None
        }
        opp = requests.patch(f"https://discord.com/api/v9/guilds/{guild_id}", headers=self.header, json=a)
        if self.com_c != None and self.rule_c != None:
            self.del_c(self.com_c) 
            self.del_c(self.rule_c) 
             
        channels = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header)
        
        for channel in channels.json():
            if self.dubes != None and self.pubes != None:
                print(f'{channel["name"]}:  position: {channel["position"]}  org:  {self.dubes.split(":")[1]}')
                if channel['name'] == self.dubes.split(':')[0] and channel['position'] == int(self.dubes.split(':')[1]) and channel['type'] == int(self.dubes.split(':')[2]):
                    self.r_p = f'{channel["id"]}'
                    print(self.r_p)
                elif channel['name'] == self.pubes.split(':')[0] and channel['position'] == int(self.pubes.split(':')[1]) and channel['type'] == int(self.pubes.split(':')[2]):
                    self.c_p = f'{channel["id"]}'
                    print(self.c_p)
                
        if self.r_p != None and self.c_p != None:
           
            
            self.a2 = {
                "features": ["COMMUNITY"],
                "preferred_locale": "en-US",
                "rules_channel_id": self.r_p,
                "public_updates_channel_id": self.c_p,
                "verification_level": 1,
            }
            print(self.a2)
            cpop = session.patch(f'https://discord.com/api/v9/guilds/{guild_id}', headers=self.header, json=self.a2)


                    
        beupu = requests.patch(f'https://discord.com/api/v9/guilds/{guild_id}', headers=self.header, json = {'description': self.d_des}) 
        channels = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/channels', headers=self.header)
        roles = session.get(f'https://discord.com/api/v9/guilds/{guild_id}/roles', headers=self.header)
        chanel = json.loads(channels.text)
        rols = json.loads(roles.text)
        print(len(self.n_perm))
        if roles.status_code == 200 and channels.status_code == 200:
            for channel in chanel:
                
                for role in rols:
                    
                    try:            
                        
                        for mj in self.n_perm:
                            
                            if channel['position'] == int(mj.split(':')[3]) and role['name'] == mj.split(':')[0] and int(role['position']) == int(mj.split(':')[4]):
                                while True:
                                    light = {'type': 0, 'allow': mj.split(':')[1], 'deny': mj.split(':')[2]}
                                    r = requests.put(f'https://discord.com/api/v9/channels/{channel["id"]}/permissions/{role["id"]}', headers=self.header, json=light)
                                    if r.status_code == 429:
                                        try:
                                            time.sleep(r.json()['retry_after'])
                                        except:
                                            pass
                                    else:
                                        if r.status_code == 200:
                                            break
                                        else:
                                            break
                                    
                    except Exception as err:
                        print(err)
                     
                    try:
                        for c in self.permissions:
                        
                            if role['position'] == int(c.split(':')[2]) and channel['position'] == int(c.split(':')[3]):
                                while True:
                                    r = requests.put(f'https://discord.com/api/v9/channels/{channel["id"]}/permissions/{role["id"]}', headers=self.header, json={'type': 0, 'allow': c.split(':')[0], 'deny':c.split(':')[1]})
                        #print(r.text)
                            
                                    if r.status_code == 429:
                                        try:
                                            time.sleep(r.json()['retry_after'])
                                        except:
                                            pass
                                    else:
                                        if r.status_code == 200:
                                            break
                                        else:
                                            break
                    except Exception as err:
                        print(err)
        
        cats.clear()
    
    
    
    
                                
                           
          
    async def main(self):
        os.system("cls || clear")
        print(f"""
        

    \033[38;2;155;0;255m                                                    /$$$  
    \033[38;2;140;0;255m                                             |_  $$ 
    \033[38;2;135;0;255m   /$$$$$$$  /$$$$$$   /$$$$$$  /$$   /$$       /$$ \  $$       \033[0mMade by:  {base64.b64decode(secret_key).decode().split(' ')[2]}
    \033[38;2;120;0;255m   /$$_____/ /$$__  $$ /$$__  $$| $$  | $$      |__/  | $$      \033[0mGithub:  https://github.com/airlone
    \033[38;2;105;0;255m  | $$      | $$  \ $$| $$  \ $$| $$  | $$            | $$      \033[0mDiscord: lone#4279
    \033[38;2;90;0;255m  | $$      | $$  | $$| $$  | $$| $$  | $$       /$$  /$$/      \033[0mYoutube: https://youtube.com/@fatherabuser9979
    \033[38;2;75;0;255m  |  $$$$$$$|  $$$$$$/| $$$$$$$/|  $$$$$$$      |__//$$$/ 
    \033[38;2;60;0;255m   \_______/ \______/ | $$____/  \____  $$         |___/  
    \033[38;2;55;0;255m                      | $$       /$$  | $$                
    \033[38;2;40;0;255m                      | $$      |  $$$$$$/                
    \033[38;2;25;0;255m                      |__/       \______/                 
 

        
                          \033[0m[1] Clone Server
        
        
        """)
        choose = input("  >   ")
        if choose == "1":
            guild_id_to_copy = input("Guild id to copy from: ")
            guild_id_to_load = input("Guild id to load in: ")
            
            self.realer_e(guild_id_to_load)
            p1 = threading.Thread(target=self.emojis_loader, args=(guild_id_to_copy, guild_id_to_load,))
            p1.start()
            
            self.server_copy(guild_id_to_copy, guild_id_to_load)
            self.get_roles(guild_id_to_copy)
            self.get_channels(guild_id_to_copy)
            self._write('Cloning ' + str(len(self.roles)) + ' roles.... from guild ' + guild_id_to_copy)
            self._write('Cloning ' + str(len(self.n_channels) + len(self.c_channels) + len(self.categories)) + ' roles.... from guild ' + guild_id_to_copy)
            threading.Thread(target=self.clone_em_up, args=(guild_id_to_load,)).start()
            
            #t7.join()
            
            await asyncio.sleep(6)
            await self.main()
            
        else:
            await self.main()        
            
if __name__ == "__main__":
    vfx = base64.b64decode(secret_key).decode()
    if  base64.b64encode(vfx.split(' ')[2].encode()).decode() != 'bG9uZSM0Mjc5':
        print('Invalid author key...exiting...')
        os._exit(0)
    asyncio.run(Cloner().main())
