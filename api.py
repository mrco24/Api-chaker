# Python
import halapi
api = halapi.API()
api.authenticate_by_key('REDACTED')

# REST API with curl
curl -X POST -H "HALCorp-Key: REDACTED" https://api.halcorp.biz/userinfo
