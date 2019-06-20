import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

# Use a service account
cred = credentials.Certificate('firebase-credentials.json')
firebase_admin.initialize_app(cred)

db = firestore.client()


def store_instrumentality_message(content: str, message_id: str, user_id: str, server_id: str):
    user_ref = db.collection(u'servers').document(server_id).collection(
        u'users').document(user_id).collection(u'messages')
    user_ref.document(message_id).set({
        u'content': content
    })


def get_user(user_id, server_id):
    user_ref = db.collection(u'servers').document(str(server_id)).collection(u'users').document(user_id)
    return user_ref.get().to_dict()


def merge_user(user_id, server_id, merge):
    user_ref = db.collection(u'servers').document(server_id).collection(u'users').document(user_id)
    user_ref.set(merge, merge=True)

# doc_ref = db.collection(u'users').document(u'alovelace')
# doc_ref.set({
#     u'first': u'Ada',
#     u'last': u'Lovelace',
#     u'born': 1815
# })

# doc_ref = db.collection(u'users').document(u'aturing')
# doc_ref.set({
#     u'first': u'Alan',
#     u'middle': u'Mathison',
#     u'last': u'Turing',
#     u'born': 1912
# })
