#!/usr/bin/env python3 

"""
Copyright 2023 Host1let: Post Scammer

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the “Software”), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED “AS IS”, WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""

import pyrogram 

import re 

class Changer(object):
    
    def tag(text, change_id):
        if "@" in text:
            try:
                pattern = r'@(\w+)'
                rep_string = re.sub(pattern, f"@{change_id}", text)
                return rep_string
            except:
                pass


    def link(org_text, link_to_find):
        if link_to_find in org_text:
            try:
                pattern = r'{}'.format(link_to_find)
                data = re.find(pattern, org_text).group(1)
                return data
            except:
                pass

def TelegramSearch(api_hash : str, api_id : int, channel_ids : list):
    
    app = pyrogram.Client(__name__, api_id=api_id, api_hash=api_hash)
    
    for ch_id in channel_ids:
        posts = app.get_chat_history(ch_id)
        
        for post in posts:
            print(post.text)

TelegramSearch("f2f8d6ac8122fcab2e714fb0862784a1", 22084142, ['smoothy_chinl'])