| ID    | Test Name           | Steps                      | Expected Result           |
| ----- | ------------------- | -------------------------- | ------------------------- |
| TC001 | Verify Genre Filter | Select “Action” from Genre | Action movies displayed   |
| TC002 | Pagination          | Click Next page            | New results load          |
| TC003 | Invalid Slug        | Access `/popular` URL      | Page fails gracefully     |
| TC004 | API Popular Movies  | GET `/movie/popular`       | Response 200 with results |

