export TYPE='Content-Type: application/json'
export AUTH='Authorization: Basic '`bx wsk property get --auth | awk '{printf("%s", $3)}' | base64 `
export NAMESPACE=<OW_NAMESPACE>
export API_ENDPOINT=<API_ENDPOINT>
curl -k -s -X POST -d '{"from": "FROM_EMAIL_ID", "to": "TO_EMAIL_ID","subject":"OpenWhisk Alert","content":"Hello from Serverless"}' -H "$TYPE" -H "$AUTH" https://$API_ENDPOINT/api/v1/namespaces/$NAMESPACE/actions/sendMail?blocking=true
