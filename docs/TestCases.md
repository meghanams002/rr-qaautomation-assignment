# Test Cases

| ID | Area | Description | Steps | Expected |
|----|------|--------------|--------|-----------|
| TC01 | UI | Verify "Popular" filter | Click Popular tab | Titles visible |
| TC02 | UI | Pagination works | Click Next Page | New titles load |
| TC03 | API | Trending API reachable | Call API | Status 200 |
| TC04 | API | Trending API has results | Parse JSON | results[] > 0 |
