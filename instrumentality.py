from firebase import store_instrumentality_message, get_user, merge_user

def store_message(message):
    user = message.author.name + '-' + message.author.discriminator
    server = str(message.author.guild.id)
    store_instrumentality_message(message.content, str(message.id), user, server)

def update_server_user_info():
    pass

def is_user_opted_in(user):
    user_id = user.name + '-' + user.discriminator
    user_document = get_user(user_id, user.guild.id)
    if  user_document is not None and 'instrumentality' in user_document:
        return user_document['instrumentality']
    else:
        return False

def opt_in(user):
    user_id = user.name + '-' + user.discriminator
    merge = {
        u'instrumentality':True
    }
    merge_user(user_id, str(user.guild.id), merge)

def opt_out(user):
    user_id = user.name + '-' + user.discriminator
    merge = {
        u'instrumentality':False
    }
    merge_user(user_id, str(user.guild.id), merge)

    