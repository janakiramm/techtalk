# IBM Cloud Functions with Cloudant Tutorial

For a detailed walkthrough, please follow the [tutorial](https://thenewstack.io/walkthrough-building-serverless-applications-ibm-bluemix/)

## Check available Packages
```
bx wsk package list
```

## Create Cloudant Service
```
bx cf create-service cloudantNoSQLDB Lite salesdb
bx cf create-service-key salesdb myapp
bx cf service-key salesdb myapp

```
## Perform CRUD Operations
```
export CLOUDANT='<URL>'
curl '<URL>'
curl -s -X GET $CLOUDANT  | jq .
curl -s -X GET $CLOUDANT/_all_dbs  | jq .
curl -s -X PUT $CLOUDANT/sales
curl -s -H "Content-type: application/json" -d "{\"name\":\"John Doe\"}" -X POST $CLOUDANT/sales
curl -s -X GET $CLOUDANT/sales/_all_docs   | jq .
curl -s -X DELETE $CLOUDANT/sales/<DOC_ID>?rev=<REV> | jq .
```

## Create Cloudant Package
```
bx wsk package get --summary /whisk.system/cloudant
bx wsk package refresh
bx wsk package list
```

## Create Trigger, Action, and Rule for New Order
```
bx wsk trigger create data-inserted-trigger --feed Bluemix_salesdb_myapp/changes --param dbname sales

bx wsk action create order order.js
bx wsk action invoke --blocking --result --param order 10000 --param manager Jani order
bx wsk action create order-sequence --sequence Bluemix_salesdb_myapp/read,order

bx wsk rule create log-order data-inserted-trigger order-sequence
bx wsk rule enable log-order
```

## Test Order Action
```
bx wsk activation poll
curl -s -H "Content-type: application/json" -d "{\"order\":\"12000\",\"manager\":\"Janakiram\"}" -X POST $CLOUDANT/sales

bx wsk activation list
bx wsk activation result <ID>
```
## Create Trigger, Action, and Rule for High Value Order
```
bx wsk action create high-value-order mail.js
bx wsk action invoke --blocking --result --param order 10000 --param manager Jani high-value-order
bx wsk action create high-value-order-sequence --sequence Bluemix_salesdb_myapp/read,high-value-order
bx wsk rule create log-high-value-order data-inserted-trigger high-value-order-sequence
curl -s -H "Content-type: application/json" -d "{\"order\":\"50000\",\"manager\":\"Janakiram\"}" -X POST $CLOUDANT/sales
```

## Test High Value Order Action
```
bx wsk activation list
bx wsk activation result <ID>
```

## Cleanup
```
bx cf delete-service-key salesdb myapp
bx service delete salesdb
bx wsk trigger delete data-inserted-trigger
bx wsk action delete order
bx wsk action delete order-sequence
bx wsk rule delete log-order
bx wsk action delete high-value-order
bx wsk action delete high-value-order-sequence
bx wsk rule delete log-high-value-order
```
