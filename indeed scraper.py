from apify_client import ApifyClient

client = ApifyClient("apify_api_uMdQOL9Fq3LPSy6WN2LATQ4OHGYL1w2V8fVg")

# Prepare the Actor input
run_input = {
    "position": "web developer",
    "country": "US",
    "location": "San Francisco",
    "maxItems": 150,
}

# Run the Actor and wait for it to finish
run = client.actor("misceres/indeed-scraper").call(run_input=run_input)

# Fetch and print Actor results from the run's dataset (if there are any)
print("💾 Check your data here: https://console.apify.com/storage/datasets/" + run["defaultDatasetId"])
for item in client.dataset(run["defaultDatasetId"]).iterate_items():
    print(item)


# 📚 Want to learn more 📖? Go to → https://docs.apify.com/api/client/python/docs/quick-start