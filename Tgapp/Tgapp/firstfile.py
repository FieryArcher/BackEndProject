import json

import telepot
from xml.etree import cElementTree
import requests

def parse_planetpy_rss():
    """Parses first 10 items from http://planetpython.org/rss20.xml"""
    response = requests.get('http://planetpython.org/rss20.xml')
    parsed_xml = cElementTree.fromstring(response.content)
    items=[]
    for node in parsed_xml.iter():
        if node.tag == 'item':
            item = {}
            for item_node in list(node):
                if item_node.tag == 'title':
                    item['title'] = item_node.text
                if item_node.tag == 'link':
                    item['link'] = item_node.text
            items.append(item)
    return items[:10]

TOKEN='5288278553:AAET4HjuA2rlAqrn7Rkun-dQ9sgIgCyw5ow'
TelegramBot = telepot.Bot(TOKEN)
def _display_help():
    return render_to_string('help.md')
def _display_planetpy_feed():
    return render_to_string('feed.md', {'items': parse_planetpy_rss()})
class CommandReceiveView(View):
    def post(self, request, bot_token):
        if bot_token != TOKEN:
            return HttpResponseForbidden('Invalid token')
        commands = {
            '/start': _display_help,
            'help': _display_help,
            'feed': _display_planetpy_feed,
        }
        try:
            payload = json.loads(request.body.decode('utf-8'))
        except ValueError:
            return HttpResponseBadRequest('Invalid request body')
        else:
            chat_id = payload['message']['chat']['id']
            cmd = payload['message'].get('text')  # command
            func = commands.get(cmd.split()[0].lower())
            if func:
                TelegramBot.sendMessage(chat_id, func(), parse_mode='Markdown')
            else:
                TelegramBot.sendMessage(chat_id, 'I do not understand you, Sir!')
        return JsonResponse({}, status=200)
    @method_decorator(csrf_exempt)
    def dispatch(self, request, *args, **kwargs):
        return super(CommandReceiveView, self).dispatch(request, *args, **kwargs)

print(TelegramBot.getUpdates())