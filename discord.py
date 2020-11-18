from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/776417294187757568/f0xqLpTY_ksAeuw8WU__AMtAROp21mBSAmAHzru66n0kbOvNWlpzHVQZ0V18Qou65iPB',
                         username="Smyths Toys Monitor")

webhook_blaze = DiscordWebhook(url="https://discord.com/api/webhooks/778745968816291891/dGefV2u6FbAerEBtO85yj17pFL-MrPNwnUig0v2WFwqesWjIGQNn7vI221oWdqNMqeNL",
                               username="Smyths Toys Monitor")

def send_hook(product_title, url, price, image_url):
    embed = DiscordEmbed(title=product_title,
                         description='PRODUCT NOW AVAIALABLE', color=242424)
    embed.set_author(name='Smyths Toys Monitor', url=url)
    #embed.set_footer(text='Embed Footer Text')
    embed.set_timestamp()
    embed.add_embed_field(name='Price', value=price)
    embed.set_thumbnail(url=image_url)
    #embed.add_embed_field(name='Field 2', value='dolor sit')
    #embed.add_embed_field(name='Field 3', value='amet consetetur')
    #embed.add_embed_field(name='Field 4', value='sadipscing elitr')

    webhook.add_embed(embed)
    response = webhook.execute()
    webhook_blaze.add_embed(embed)
    response = webhook_blaze.execute()
