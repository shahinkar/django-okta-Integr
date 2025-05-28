from rest_framework import authentication
from rest_framework import exceptions
from okta_jwt_verifier  import AccessTokenVerifier
import asyncio

class OktaAuthentication(authentication.BaseAuthentication):
    
   def authenticate(self, request):
          
         access_token = request.META.get('HTTP_AUTHORIZATION')
         
         if not access_token:
                raise exceptions.AuthenticationFailed('Authentication failed.')
         
         loop = asyncio.new_event_loop()
         jwt_verifier = AccessTokenVerifier(issuer='https://dev-test.okta.com/oauth2/default', audience='api://default')
         loop.run_until_complete(jwt_verifier.verify(access_token.replace('Bearer', '').strip()))
         print('Token validated successfully.')