from discord_webhook import DiscordWebhook, DiscordEmbed

webhook = DiscordWebhook(url='https://discord.com/api/webhooks/776417294187757568/f0xqLpTY_ksAeuw8WU__AMtAROp21mBSAmAHzru66n0kbOvNWlpzHVQZ0V18Qou65iPB',
                         username="Yasser")



def send_hook(product_title, url, price, image_url):
    embed = DiscordEmbed(title=product_title,
                         description='PRODUCT NOW AVAIALABLE', color=242424)
    embed.set_author(name='Yasser\'s Webhook', url=url)
    #embed.set_footer(text='Embed Footer Text')
    embed.set_timestamp()
    embed.add_embed_field(name='Price', value=price)
    embed.set_thumbnail(
        url=image_url)
    #embed.add_embed_field(name='Field 2', value='dolor sit')
    #embed.add_embed_field(name='Field 3', value='amet consetetur')
    #embed.add_embed_field(name='Field 4', value='sadipscing elitr')

    webhook.add_embed(embed)
    response = webhook.execute()
