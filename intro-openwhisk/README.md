# OpenWhisk SendGrid Tutorial

## Create Action
```
npm install
zip -r action.zip *
bx wsk action create sendMail --kind nodejs:6 action.zip
```

## Test Action
```
bx wsk action invoke --result sendMail --param-file parameters.json
```
## Create and Test Trigger
```
bx wsk trigger create Notification
bx wsk trigger list
bx wsk trigger fire Notification
```

## Create and Test Rule
```
bx wsk rule create notifyRule Notification sendMail
bx wsk trigger fire Notification --param-file parameters.json
```

## Invoke from cURL 
```
# Initialize environment variables
sh ./curl.sh
```
