# Shortly
A URL shortening service that converts long URLs into shorter, manageable links. It also provides analytics for the shortened URLs.


## Functional Requirements
### In Scope

- [ ] Allow users to submit a long URL and receive a shortened version.
    - [ ] Optionally, enable users to specify a custom alias for their shortened URL.
    - [ ] Optionally, enable users to set an expiration date for their shortened URL.
- [ ] Provide users with the ability to access the original URL using the shortened URL.

### Out of scope
 - Authentication
 - Analytics on link clicks (example: click counts, geographic data).

 ## Non-functional Requirements
### In Scope
- [ ] Ensure uniqueness for short codes (no two long URLs should map to the same short URL).
- [ ] Redirection should occur with minimal delay (< 100ms).
- [ ] Ensure system reliability and availability of 99.99% (availability > consistency).
- [ ] Scale to support 1 billion shortened URLs and 100 million daily active users (DAU).

### Out of scope
- Data consistency in real-time analytics.
- Advanced security features like spam detection and malicious URL filtering.
