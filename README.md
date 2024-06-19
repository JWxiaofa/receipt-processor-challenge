# Receipt Processor
implemented using Python Flask

## How to run the app
After clone the current repo, first make sure to start the Docker, then use the command below to run the app. Requirements are listed in requirements.txt.

```bash
docker build -t flask-test-app .
docker run -p 5001:5001 flask-test-app
```

Then open another terminal to access the API:

To send post request:
```bash
$ curl -X POST -H "Content-Type: application/json" -d '{
  "retailer": "Target",
  "purchaseDate": "2022-01-01",
  "purchaseTime": "13:01",
  "items": [
    {"shortDescription": "Mountain Dew 12PK", "price": "6.49"},
    {"shortDescription": "Emils Cheese Pizza", "price": "12.25"},
    {"shortDescription": "Knorr Creamy Chicken", "price": "1.26"},
    {"shortDescription": "Doritos Nacho Cheese", "price": "3.35"},
    {"shortDescription": "Klarbrunn 12-PK 12 FL OZ", "price": "12.00"}
  ],
  "total": "35.35"
}' http://localhost:5001/receipts/process
```
You will get a response like this:
```bash
{
  "id": "2b643392-aca4-4eda-928f-79cd3236aab6"
}
```

Copy the id and use it as parameter to access '/receipts/{id}/points':
```bash
$ curl -X GET http://localhost:5001/receipts/<copy the id here>/points
$ curl -X GET http://localhost:5001/receipts/2b643392-aca4-4eda-928f-79cd3236aab6/points
```

Then you will get the result like this:
```bash
{
  "points": 28
}

```