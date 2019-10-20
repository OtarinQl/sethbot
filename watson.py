from ibm_watson import PersonalityInsightsV3, ApiException
import json

#Mover esto a variables de entorno
personality_insights = PersonalityInsightsV3(
    version='2017-10-13',
    iam_apikey='pTx7cHCx1r9rW8asgkM1SfJEwT8oGBBCOASAePV-z8Ku',
    url='https://gateway.watsonplatform.net/personality-insights/api'
)

def create_personality(messages):
    try:
        profile = personality_insights.profile(
            json.dumps(messages, ensure_ascii=True),#Json de los mensajes
            'application/json',
            content_type='application/json',
            consumption_preferences=True,
            raw_scores=True
        ).get_result()
        print(json.dumps(profile, indent=2))
    except ApiException as ex:
        print ("Method failed with status code " + str(ex.code) + ": " + ex.message)


