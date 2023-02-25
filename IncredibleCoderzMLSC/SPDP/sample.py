import http.client

conn = http.client.HTTPSConnection("v1.genr.ai")

payload = "{\n  \"genre\": \"rap\",\n  \"artist\": \"kanye\",\n  \"modifier1\": \"Hello\",\n  \"modifier2\": \"life\",\n  \"modifier3\": \"Unicorns\",\n  \"chord_flag\": false,\n  \"complex_chord_flag\": false,\n  \"key\": \"C\",\n  \"scale\": \"Major\"\n}"

headers = { 'Content-Type': "application/json" }

conn.request("POST", "/api/use-case/generate-lyrics", payload, headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))