Sportsbook webscrapers

GET requests notes:
- Must use browser user-agent
- Seems that all AWS IP addresses are blocked; the following curl works locally but not from EC2 or Lambda

```curl -H "Accept: application/json" -A "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36" https://sportsbook-nash-usmd.draftkings.com/sites/US-MD-SB/api/v5/eventgroups/84240/categories/743/subcategories/6606?format=json -o temp.json```