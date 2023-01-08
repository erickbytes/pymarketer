r = requests.request(
    url="https://example.com/stuff?drink=tea",
    method="GET",
    headers={"Content-Type": "application/json", "Cache-Control": "no-cache"},
)
