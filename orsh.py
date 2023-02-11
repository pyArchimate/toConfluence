from msal import PublicClientApplication
app = PublicClientApplication(
    "your_client_id",
    authority="https://login.microsoftonline.com/Enter_the_Tenant_Name_Here")
accounts = app.get_accounts(username="xavier.mayeur@ing.com")
result = app.acquire_token_interactive(  # It automatically provides PKCE protection
         scopes=config["scope"])