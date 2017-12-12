from facebookads.adobjects.adaccount import AdAccount
from facebookads.adobjects.adsinsights import AdsInsights
from facebookads.api import FacebookAdsApi
from facebookads.adobjects.adaccountuser import AdAccountUser
from facebookads.adobjects.campaign import Campaign

# Get keys from my code file
keys = []

with open('secret_keys') as file:
    for line in file:
        key = line
        keys.append(key)
access_token = keys[0]
ad_account_id = keys[1]
app_secret = keys[2]
app_id = keys[3]

# Call Facebook Api
FacebookAdsApi.init(access_token=access_token)

# Add after FacebookAdsApi.init
me = AdAccountUser(fbid='me')
my_account = me.get_ad_accounts()[0]
Account_Id = my_account['id']

# Set up Account class
class Account(object):
    def __init__(self, account_id):
        self.account_id = account_id


# Add new Account ID
new_acc = Account(account_id=Account_Id)



campaign = Campaign(new_acc.account_id)
params = {
    'date_preset' : 'this_year'
}

fields = [
        'campaign_name',
        'adset_name',
        'adset_id',
        'impressions',
        'spend',
        'reach',
        'actions',
        'action_values'
    ]

insights = campaign.get_insights(fields, params)


print insights
